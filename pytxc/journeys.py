from datetime import time

from lxml.etree import _Element
from pydantic import BaseModel

from pytxc.constants import NAMESPACES


class TicketMachine(BaseModel):
    journey_code: str

    @classmethod
    def from_element(cls, element: _Element):
        return cls(
            journey_code=element.findtext("./txc:JourneyCode", namespaces=NAMESPACES)
        )


class Operational(BaseModel):
    ticket_machine: TicketMachine

    @classmethod
    def from_element(cls, element: _Element):
        machine = element.find("./txc:TicketMachine", namespaces=NAMESPACES)
        if machine is not None:
            machine = TicketMachine.from_element(machine)
        return cls(ticket_machine=machine)


class VehicleJourney(BaseModel):
    departure_time: time
    journey_pattern_ref: str
    line_ref: str
    operator_ref: str
    service_ref: str
    vehicle_journey_code: str

    @classmethod
    def from_element(cls, element: _Element):
        operator_ref = element.findtext("./txc:OperatorRef", namespaces=NAMESPACES)
        vehicle_journey_code = element.findtext(
            "./txc:VehicleJourneyCode", namespaces=NAMESPACES
        )
        service_ref = element.findtext("./txc:ServiceRef", namespaces=NAMESPACES)
        line_ref = element.findtext("./txc:LineRef", namespaces=NAMESPACES)
        journey_pattern_ref = element.findtext(
            "./txc:JourneyPatternRef", namespaces=NAMESPACES
        )
        departure_time = element.findtext("./txc:DepartureTime", namespaces=NAMESPACES)
        return cls(
            operator_ref=operator_ref,
            vehicle_journey_code=vehicle_journey_code,
            service_ref=service_ref,
            line_ref=line_ref,
            journey_pattern_ref=journey_pattern_ref,
            departure_time=departure_time,
        )
