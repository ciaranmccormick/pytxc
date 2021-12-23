from datetime import time

from pydantic import BaseModel

from .txc import Element


class TicketMachine(BaseModel):
    journey_code: str

    @classmethod
    def from_element(cls, element: Element):
        return cls(journey_code=element.find_text("./txc:JourneyCode"))


class Operational(BaseModel):
    ticket_machine: TicketMachine

    @classmethod
    def from_element(cls, element: Element):
        machine = element.find("./txc:TicketMachine")
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
    def from_element(cls, element: Element):
        operator_ref = element.find_text("./txc:OperatorRef")
        vehicle_journey_code = element.find_text("./txc:VehicleJourneyCode")
        service_ref = element.find_text("./txc:ServiceRef")
        line_ref = element.find_text("./txc:LineRef")
        journey_pattern_ref = element.find_text("./txc:JourneyPatternRef")
        departure_time = element.find_text("./txc:DepartureTime")
        return cls(
            operator_ref=operator_ref,
            vehicle_journey_code=vehicle_journey_code,
            service_ref=service_ref,
            line_ref=line_ref,
            journey_pattern_ref=journey_pattern_ref,
            departure_time=departure_time,
        )
