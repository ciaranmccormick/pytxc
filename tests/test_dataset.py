from pathlib import Path

from pytxc.datasets import Dataset

DATA_DIR = Path(__file__).parent / "data"


def test_dataset_from_zip_path_str():
    """Ensure we can load datasets by providing a string."""
    zipped_dataset = DATA_DIR / "fecs.zip"
    dataset = Dataset.from_zip_path_str(zipped_dataset.as_posix())
    assert len(dataset) == 15


def test_get_timetable_by_name(snapshot):
    """Ensure we can load a data from a zip path."""
    dataset = Dataset.from_zip_path(DATA_DIR / "fecs.zip")
    filename = "5-FECS_5--FECS-COASTAL-2022-02-20-CO1L-BODS_V1_1.xml"
    timetable = dataset.get_timetable_by_name(filename)
    assert timetable
    snapshot.assert_match(timetable.json())


def test_index_dataset(snapshot):
    """Ensure that a dataset is index correctly by index"""
    zipped_dataset = DATA_DIR / "fecs.zip"
    dataset = Dataset.from_zip_path_str(zipped_dataset.as_posix())
    snapshot.assert_match(dataset[0].json())


def test_dataset_from_xml_file(snapshot):
    """Ensure that we can load a dataset by string path to an xml."""
    xml_file_path = DATA_DIR / "stockton_35.xml"
    dataset = Dataset.from_xml_file_path_str(xml_file_path.as_posix())
    assert len(dataset) == 1
    snapshot.assert_match(dataset[0].json())
