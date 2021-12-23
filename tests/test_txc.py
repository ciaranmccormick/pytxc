from datetime import datetime
from pathlib import Path
from types import GeneratorType
from typing import Optional

import pytest

from pytxc import TransXChange
from pytxc.txc import Element

HERE = Path(__file__)
DATA = HERE.parent / "data"


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("./txc:StopPoints/txc:AnnotatedStopPointRef/txc:StopPointRef", "077072002S"),
        ("./txc:BLAH", None),
    ],
)
def test_element_find(path: str, expected: Optional[str]):
    """
    GIVEN the stockton 35 TransXChange file.
    WHEN calling `find` with a path.
    THEN the first element in the file should be returned unless it doesn't exist
    THEN None is returned.
    """
    stockton_35 = DATA / "stockton_35.xml"
    element = Element.from_path(stockton_35)
    stop_point = element.find(path)

    if stop_point is not None:
        actual = stop_point.text
    else:
        actual = None

    assert actual == expected


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("./txc:StopPoints/txc:AnnotatedStopPointRef", 48),
        ("./txc:BLAH", 0),
    ],
)
def test_element_find_all(path: str, expected: int):
    """
    GIVEN the stockton 35 TransXChange file.
    WHEN calling `find_all` with a path.
    THEN all elements in the file should be returned.
    """
    stockton_35 = DATA / "stockton_35.xml"
    element = Element.from_path(stockton_35)
    stop_points = element.find_all(path)
    assert expected == len(stop_points)


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("./txc:StopPoints/txc:AnnotatedStopPointRef/txc:StopPointRef", "077072002S"),
        ("./txc:BLAH", None),
    ],
)
def test_element_find_text(path: str, expected: Optional[str]):
    """
    GIVEN the stockton 35 TransXChange file.
    WHEN calling `find_text` with a path.
    THEN the text of the element in the file should be returned unless it's missing
    THEN None should be returned.
    """
    stockton_35 = DATA / "stockton_35.xml"
    element = Element.from_path(stockton_35)
    actual = element.find_text(path)
    assert actual == expected


def test_txc_attributes():
    """
    GIVEN the stockton 35 TransXChange file.
    WHEN calling `attributes`.
    THEN a dict containing the TXC file header should be returned.
    """
    expected = {
        "creation_date_time": datetime.fromisoformat("2020-11-22T11:00:00"),
        "file_name": "35st-None--SCTE-ST-2021-12-12-TXC_SOT_PB_ALL_20211121-BODS_V1_1.xml",
        "modification": "revise",
        "modification_date_time": datetime.fromisoformat("2021-12-17T11:08:35"),
        "revision_number": 159,
        "schema_version": "2.4",
    }
    txc = TransXChange.from_filepath(DATA / "stockton_35.xml")
    assert txc.attributes == expected


def test_element_get_root():
    """
    GIVEN the stockton 35 TransXChange file.
    WHEN calling `get_root` on a child element.
    THEN the root TransXChange element should be returned.
    """
    stockton_35 = DATA / "stockton_35.xml"
    element = Element.from_path(stockton_35)
    path = "./txc:StopPoints/txc:AnnotatedStopPointRef"
    child = element.find(path)
    if child is not None:
        root = child.get_root()
        assert root.tag.endswith("TransXChange")


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("./txc:StopPoints/txc:AnnotatedStopPointRef", 48),
        ("./txc:BLAH", 0),
    ],
)
def test_element_iter_find(path: str, expected: int):
    """
    GIVEN the stockton 35 TransXChange file.
    WHEN calling `iter_find` with a path.
    THEN a generator of all elements in the file should be returned.
    """
    stockton_35 = DATA / "stockton_35.xml"
    element = Element.from_path(stockton_35)
    stop_points = element.iter_find(path)
    assert isinstance(stop_points, GeneratorType)
    assert expected == len(list(stop_points))
