from pytxc.journeys.vehicles import VehicleJourney
from tests.constants import NSPACE


def test_vehicle_journey(snapshot):
    string = f"""
    <VehicleJourney {NSPACE}>
        <OperatorRef>tkt_oid</OperatorRef>
        <Operational>
            <TicketMachine>
            <JourneyCode>1001</JourneyCode>
            </TicketMachine>
        </Operational>
        <VehicleJourneyCode>1001</VehicleJourneyCode>
        <ServiceRef>PC1116467:8</ServiceRef>
        <LineRef>ADER:PC1116467:8:1A</LineRef>
        <JourneyPatternRef>jp_1</JourneyPatternRef>
        <DepartureTime>05:12:00</DepartureTime>
    </VehicleJourney>
    """
    vehicle_journey = VehicleJourney.from_string(string)
    snapshot.assert_match(vehicle_journey.json())
