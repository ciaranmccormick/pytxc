import zipfile
from pathlib import Path

import pytest
import requests_mock
from requests import RequestException

from pytxc import Dataset
from pytxc.datasets import DATASET_DOWNLOAD_URL, ParseException

DATA_DIR = Path(__file__).parent / "data"


def test_dataset_from_zip_path_str():
    zipped_dataset = DATA_DIR / "fecs.zip"
    dataset = Dataset.from_zip_path_str(zipped_dataset.as_posix())
    assert len(dataset) == 15


def test_dataset_from_url(dataset_response):
    id_ = 6972
    url = DATASET_DOWNLOAD_URL.format(id=id_)
    with requests_mock.Mocker() as m:
        m.get(url, content=dataset_response)
        dataset = Dataset.from_bods_id(id_)
    assert len(dataset) == 15


def test_dataset_from_url_exception():
    id_ = 6972
    url = DATASET_DOWNLOAD_URL.format(id=id_)
    with requests_mock.Mocker() as m:
        m.get(url, exc=RequestException)
        with pytest.raises(ParseException) as excinfo:
            Dataset.from_bods_id(id_)
        assert str(excinfo.value) == f"Unable to retrieve data set from {url}"


def test_get_timetable_by_name():
    dataset = Dataset.from_zip_path(DATA_DIR / "fecs.zip")
    filename = "5-FECS_5--FECS-COASTAL-2022-02-20-CO1L-BODS_V1_1.xml"
    timetable = dataset.get_timetable_by_name(filename)
    assert timetable is not None
    assert timetable.header.file_name == filename
    assert timetable.header.revision_number == 66
    assert timetable.header.schema_version == "2.4"

    filename = "blah.xml"
    timetable = dataset.get_timetable_by_name(filename)
    assert timetable is None


def test_index_dataset():
    zipped_dataset = DATA_DIR / "fecs.zip"
    with zipfile.ZipFile(zipped_dataset) as zf:
        expected = zf.namelist()[0]
    dataset = Dataset.from_zip_path_str(zipped_dataset.as_posix())
    assert dataset[0].header.file_name == expected


def test_dataset_from_xml_file():
    xml_file_path = DATA_DIR / "stockton_35.xml"
    dataset = Dataset.from_xml_file_path_str(xml_file_path.as_posix())
    assert len(dataset) == 1
    expected_filename = (
        "35st-None--SCTE-ST-2021-12-12-TXC_SOT_PB_ALL_20211121-BODS_V1_1.xml"
    )
    assert dataset[0].header.file_name == expected_filename


def test_dataset_from_path_xml():
    xml_file_path = DATA_DIR / "stockton_35.xml"
    dataset = Dataset.from_path(xml_file_path)
    assert len(dataset) == 1
    expected_filename = (
        "35st-None--SCTE-ST-2021-12-12-TXC_SOT_PB_ALL_20211121-BODS_V1_1.xml"
    )
    assert dataset[0].header.file_name == expected_filename


def test_dataset_from_path_zip():
    zipped_dataset = DATA_DIR / "fecs.zip"
    dataset = Dataset.from_path(zipped_dataset)
    assert len(dataset) == 15
