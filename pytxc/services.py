from datetime import date, datetime
from typing import List, Optional

from .elements import Element, Ref
from .journeys import JourneyPattern


class Line(Element):
    def __repr__(self) -> str:
        return f"Line(id={self.id!r}, line_name={self.line_name!r})"

    @property
    def line_name(self) -> Optional[str]:
        path = "LineName"
        return self.find_text(path)


class LineRef(Ref):
    path = "Services/Service/Lines/Line"

    def resolve(self) -> Line:
        return super()._resolve(Line)


class OperatingPeriod(Element):
    def __repr__(self) -> str:
        return (
            f"OperatingPeriod(start_date={self.start_date!r}, "
            f"end_date={self.end_date!r})"
        )

    @property
    def start_date(self) -> Optional[date]:
        path = "StartDate"
        date_str = self.find_text(path)
        if date_str is not None:
            return datetime.fromisoformat(date_str).date()

        return None

    @property
    def end_date(self) -> Optional[date]:
        path = "EndDate"
        date_str = self.find_text(path)
        if date_str is not None:
            return datetime.fromisoformat(date_str).date()

        return None


class StandardService(Element):
    def __repr__(self) -> str:
        return (
            f"StandardService(origin={self.origin!r}, "
            f"destination={self.destination!r})"
        )

    @property
    def origin(self) -> Optional[str]:
        path = "Origin"
        return self.find_text(path)

    @property
    def destination(self) -> Optional[str]:
        path = "Destination"
        return self.find_text(path)

    @property
    def use_all_stop_points(self) -> Optional[bool]:
        path = "UseAllStopPoints"
        result = self.find_text(path)
        if result is not None:
            return result == "true"

        return None

    @property
    def journey_patterns(self) -> List[JourneyPattern]:
        path = "JourneyPattern"
        return [JourneyPattern(element) for element in self.find_all(path)]


class Service(Element):
    def __repr__(self) -> str:
        return f"Service(service_code={self.service_code!r})"

    @property
    def service_code(self) -> Optional[str]:
        path = "ServiceCode"
        return self.find_text(path)

    @property
    def lines(self) -> List[Line]:
        path = "Lines/Line"
        return [Line(element) for element in self.find_all(path)]

    @property
    def operating_period(self) -> Optional[OperatingPeriod]:
        path = "OperatingPeriod"
        element = self.find(path)
        if element is not None:
            return OperatingPeriod(element)
        return None

    @property
    def standard_services(self) -> List[StandardService]:
        path = "StandardService"
        return [StandardService(element) for element in self.find_all(path)]


class ServiceRef(Ref):
    path = "Services/Service"

    def resolve(self) -> Service:
        return super()._resolve(Service)
