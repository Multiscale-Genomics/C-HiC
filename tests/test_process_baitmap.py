"""
.. See the NOTICE file distributed with this work for additional information
   regarding copyright ownership.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import print_function

import os
import pytest  # pylint: disable=unused-import

from basic_modules.metadata import Metadata
from process_baitmap import process_baitmap


def test_process_baitmap():
    """
    Test for process_rmapBaitmap pipeline.
    This pipeline generate .baitmap files,
    input files for CHiCAGO pipeline
    """
    import sys
    sys._run_from_cmdl = True  # pylint: disable=protected-access

    path = os.path.join(os.path.dirname(__file__), "data/")

    configuration = {
        "execution": path
    }

    input_files = {
        "genome_idx": path + "test_baitmap/bwa.tar.gz",
        "probes_fa": path + "test_baitmap/baits.fa",
        "Rtree_file_dat": path + "test_rmap/rtree_file.dat",
        "Rtree_file_idx": path + "test_rmap/rtree_file.idx",
        "genome_fa": path + "test_baitmap/chr21_hg19.fa",
        "chr_handler": path + "test_baitmap/chr_handler.txt"
    }

    output_files = {
        "bait_sam":  path + "test_baitmap/baits.sam",
        "out_bam": path + "test_baitmap/baits.bam",
        "out_baitmap": path + "test_run_chicago/test.baitmap"
    }

    metadata = {
        "genome_idx": Metadata(
            "index_bwa", "tar", input_files["genome_idx"], [input_files["genome_fa"]],
            {
                "assembly": "test",
                "tool": "bwa_indexer"
            }, 9606
            ),
        "genome_fa": Metadata(
            "hg38", "fasta", input_files["genome_fa"], [],
            {
                "assembly": "test",
                "tool": "bwa_indexer",
                "RE": {"HindIII": 'A|AGCTT'}
            }, 9606),

        "probes_fa": Metadata(
            "C-HiC probes", "fasta", input_files["probes_fa"], [],
            {
                "assembly": "test",
                "tool": "bwa_indexer"
            }, 9606),

        "Rtree_file_dat": Metadata(
            "Rtree files", "dat", input_files["Rtree_file_dat"], [],
            {"genome": path + "test_rmap/chr21_hg19.fa",
             "RE": {"HindIII": 'A|AGCTT'}},
            9606
            ),

        "Rtree_file_idx": Metadata(
            "Rtree files", "idx", input_files["Rtree_file_idx"], [],
            {"genome": path + "test_rmap/chr21_hg19.fa",
             "RE": {"HindIII": 'A|AGCTT'}},
            9606
            )
    }

    process_baitmap_handl = process_baitmap(configuration)
    process_baitmap_handl.run(input_files, metadata, output_files)

    assert os.path.getsize(output_files["out_baitmap"]) > 0
