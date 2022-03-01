# Usage

`pytxc` can be used to interact with TransXChange files using python.

```python
from pytxc import Timetable
from pathlib import Path


>> filepath = "path/to/transxchange/file.xml"
>> timetable = Timetable.from_file_path(Path(filepath))
>> timetable.header
Header(
    creation_date_time=datetime.datetime(2020, 11, 22, 11, 0),
    modification_date_time=datetime.datetime(2021, 12, 17, 11, 8, 35),
    file_name="file.xml",
    modification="revise",
    schema_version="2.4",
    revision_number=159,
)
```
