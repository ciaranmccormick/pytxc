"""
test_files.py
Tests of the parser against various "flavours" of TransXChange files.
"""
from pathlib import Path

import pytest

from pytxc.txc import TransXChange

DATA_DIR = Path(__file__).parent / "data"


class TestStagecoachCheseterLine1:
    @pytest.fixture()
    def timetable(self):
        file_path = DATA_DIR / "1-None--STCR-CZ-2021-10-03-TXC_CZ20211003-BODS_V1_1.xml"
        timetable = TransXChange.from_file_path(file_path)
        yield timetable

    def test_header_details(self, snapshot, timetable: TransXChange):
        """
        CreationDateTime -> 2020-11-22T11:00:00
        FileName -> 1-None--STCR-CZ-2021-10-03-TXC_CZ20211003-BODS_V1_1.xml
        Modification -> revise
        ModificationDateTime -> 2021-10-19T13:27:51
        RevisionNumber -> 72
        SchemaVersion -> 2.4
        """
        snapshot.assert_match(timetable.json())
