from pathlib import Path

import pytest
from lxml import etree

DATA_DIR = Path(__file__).parent / "data"


@pytest.fixture(scope="session")
def dataset_response():
    """Fixture for returning a zipped dataset."""
    zipped_dataset = DATA_DIR / "fecs.zip"
    with zipped_dataset.open("rb") as f:
        yield f.read()


@pytest.fixture(scope="session")
def txc_file():
    """Yield a transxchange file."""
    stockton_35 = DATA_DIR / "stockton_35.xml"
    with stockton_35.open("r") as f:
        yield f


@pytest.fixture(scope="session")
def txc_file_content():
    """Yield the contents of a transxchange file."""
    stockton_35 = DATA_DIR / "stockton_35.xml"
    with stockton_35.open("rb") as f:
        yield f.read()


@pytest.fixture(scope="session")
def txc_root(txc_file_content):
    return etree.fromstring(txc_file_content)
