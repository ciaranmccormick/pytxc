"""datasets.py."""
import zipfile
from collections import OrderedDict
from pathlib import Path
from typing import IO, List, Optional

from pytxc.txc import TransXChange


class Dataset:
    def __init__(self, timetables: List[TransXChange]):
        self.timetables = OrderedDict(
            {
                timetable.attributes.file_name: timetable
                for timetable in timetables
                if timetable.attributes is not None
            }
        )

    def __len__(self) -> int:
        """Return the number of TransXChange files in a Dataset."""
        return len(self.timetables.keys())

    def __getitem__(self, item) -> TransXChange:
        """Return a TransXChange timetable by index."""
        return list(self.timetables.values())[item]

    def get_timetable_by_name(self, name: str) -> Optional[TransXChange]:
        """Return a TransXChange timetable by filename."""
        return self.timetables.get(name, None)

    @classmethod
    def from_zip_file(cls, file: IO[bytes]) -> "Dataset":
        """Return a Dataset from a zip file."""
        timetables = []
        with zipfile.ZipFile(file) as zip_file:
            filenames = [name for name in zip_file.namelist() if name.endswith("xml")]
            for filename in filenames:
                with zip_file.open(filename) as txc_file:
                    timetables.append(
                        TransXChange.from_string(txc_file.read().decode("utf-8"))
                    )
        return cls(timetables)

    @classmethod
    def from_zip_path(cls, path: Path) -> "Dataset":
        """Return a Dataset from a path to a zipfile."""
        with path.open("rb") as zip_file:
            return cls.from_zip_file(zip_file)

    @classmethod
    def from_zip_path_str(cls, path: str) -> "Dataset":
        """Return a Dataset from string path to a zipfile"""
        return cls.from_zip_path(Path(path))

    @classmethod
    def from_xml_file(cls, xml_file: str) -> "Dataset":
        """Return a Dataset from an xml file."""
        timetable = TransXChange.from_string(xml_file)
        return cls([timetable])

    @classmethod
    def from_xml_file_path(cls, path: Path) -> "Dataset":
        """Return a Dataset from an xml file path."""
        with path.open("r", encoding="utf-8") as xml_file:
            return cls.from_xml_file(xml_file.read())

    @classmethod
    def from_xml_file_path_str(cls, path: str) -> "Dataset":
        """Return a Dataset from an xml file path string."""
        return cls.from_xml_file_path(Path(path))
