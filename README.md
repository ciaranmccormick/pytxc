# pytxc

## Quick start

### Installation

Use `pip` to install `pytxc`.

```console
python -m pip install pytxc
```

### Usage

The `Timetable` class is used to parse and interact with
TransXChange files.


```python
from pathlib import Path
from pytxc import Timetable


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

The `StopPoint`s in a TransXChange can be accessed through the `stop_points`
attribute.

```python
>> timetable.stop_points[0]

AnnotatedStopPointRef(
    stop_point_ref=StopPointRef(text="077072002S"),
    common_name="High Street Stand S",
)
```

Similarly, `RouteSections` can be accessed using the `route_sections` attribute.

```python
>> timetable.route_sections[0]

RouteSection(id='RS1')
```

The naming conventions used for the Python objects will more or less match those
of TransXChange for example, the first `JourneyPattern` of a `StandardService` is
usually found in a `Service` of the `Services` block.
Using `pytxc` it can be accessed as follows,

```python
>> timetable.services[0].standard_services[0].journey_patterns[0]

JourneyPattern(
    id="JP1",
    CreationDateTime="2020-11-22T11:00:00",
    ModificationDateTime="2021-12-17T11:08:35",
    Modification="revise",
    RevisionNumber="159",
)
```

When interacting with references, `pytxc` provides a `resolve` method to find
the original element in the TransXChange file. For example if a `JourneyPattern`
contains a `RouteRef` then calling `resolve` on the `route_ref` object will
return the original `Route` object.

```python
>> jp = timetable.services[0].standard_services[0].journey_patterns[0]
>> jp.route_ref.resolve()

Route(private_code='35st-40', description='Stockton - Wolviston Court')
```
