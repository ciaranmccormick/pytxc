from pathlib import Path

import pytest

DATA_DIR = Path(__file__).parent / "data"


@pytest.fixture()
def dataset_response():
    zipped_dataset = DATA_DIR / "fecs.zip"
    with zipped_dataset.open("rb") as f:
        yield f.read()


@pytest.fixture()
def txc_file():
    stockton_35 = DATA_DIR / "stockton_35.xml"
    with stockton_35.open("r") as f:
        yield f


@pytest.fixture()
def txc_file_content():
    stockton_35 = DATA_DIR / "stockton_35.xml"
    with stockton_35.open("rb") as f:
        yield f.read()
