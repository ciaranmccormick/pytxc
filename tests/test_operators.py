from lxml import etree

from pytxc.operators import Operator

NSPACE = 'xmlns="http://www.transxchange.org.uk/"'


def test_parsing_operators(snapshot):
    """Verify that a well structured Operator is parsed correctly."""
    xml = f"""
    <Operator {NSPACE} id="1" CreationDateTime="2020-11-22T11:00:00"
        ModificationDateTime="2021-12-17T11:08:35" Modification="revise"
        RevisionNumber="159">
      <NationalOperatorCode>SCTE</NationalOperatorCode>
      <OperatorCode>SOT</OperatorCode>
      <OperatorShortName>Stagecoach</OperatorShortName>
      <OperatorNameOnLicence>Cleveland Transit Ltd</OperatorNameOnLicence>
      <TradingName>Stagecoach North East</TradingName>
      <LicenceNumber>PB0001987</LicenceNumber>
      <Garages>
        <Garage>
          <GarageCode>NEBY</GarageCode>
          <GarageName>Byker Depot</GarageName>
          <Location id="L1975">
            <Longitude>-1.563148</Longitude>
            <Latitude>54.983598</Latitude>
          </Location>
        </Garage>
        <Garage>
          <GarageCode>NESU</GarageCode>
          <GarageName>Sunderland Depot</GarageName>
          <Location id="L1980">
            <Longitude>-1.381518</Longitude>
            <Latitude>54.913485</Latitude>
          </Location>
        </Garage>
      </Garages>
    </Operator>
    """
    element = etree.fromstring(xml)
    operator = Operator.from_txc(element)
    snapshot.assert_match(operator.json())


def test_parsing_operators_missing_elements(snapshot):
    """We still want Operator to parse even with some optional elements missing."""
    xml = f"""
    <Operator {NSPACE} id="1" CreationDateTime="2020-11-22T11:00:00"
        ModificationDateTime="2021-12-17T11:08:35" Modification="revise"
        RevisionNumber="159">
      <NationalOperatorCode>SCTE</NationalOperatorCode>
      <OperatorShortName>Stagecoach</OperatorShortName>
      <LicenceNumber>PB0001987</LicenceNumber>
    </Operator>
    """
    element = etree.fromstring(xml)
    operator = Operator.from_txc(element)
    snapshot.assert_match(operator.json())
