from lxml import etree

from pytxc.journeys.patterns import (
    JourneyPattern,
    JourneyPatternSection,
    JourneyPatternTimingLink,
)
from tests.constants import NSPACE


def test_journey_pattern(snapshot):
    """Can we parse a well formed JourneyPattern."""
    xml = f"""
    <JourneyPattern {NSPACE} id="JP1" CreationDateTime="2020-11-22T11:00:00"
      ModificationDateTime="2021-12-17T11:08:35" Modification="revise"
      RevisionNumber="159">
      <DestinationDisplay>Stockton High Street Stand J</DestinationDisplay>
      <OperatorRef>1</OperatorRef>
      <Direction>outbound</Direction>
      <RouteRef>RT40</RouteRef>
      <JourneyPatternSectionRefs>JPS94</JourneyPatternSectionRefs>
    </JourneyPattern>
    """
    element = etree.fromstring(xml)
    journey_pattern = JourneyPattern.from_txc(element)
    snapshot.assert_match(journey_pattern.dict())


def test_parsing_journey_pattern_sections(snapshot):
    """Can we parse a well formed JourneyPatternSection."""
    xml = f"""
    <JourneyPatternSection {NSPACE} id="JPS95">
      <JourneyPatternTimingLink id="JPTL31">
        <From SequenceNumber="1" id="JPSU61">
          <Activity>pickUpAndSetDown</Activity>
          <DynamicDestinationDisplay>Stockton</DynamicDestinationDisplay>
          <StopPointRef>077072002S</StopPointRef>
          <TimingStatus>principalTimingPoint</TimingStatus>
          <FareStageNumber>112</FareStageNumber>
        </From>
        <To SequenceNumber="2" id="JPSU62">
          <Activity>pickUpAndSetDown</Activity>
          <DynamicDestinationDisplay>Stockton</DynamicDestinationDisplay>
          <StopPointRef>077072001X</StopPointRef>
          <TimingStatus>principalTimingPoint</TimingStatus>
        </To>
        <RouteLinkRef>RL1</RouteLinkRef>
        <RunTime>PT0M0S</RunTime>
      </JourneyPatternTimingLink>
    </JourneyPatternSection>
    """
    element = etree.fromstring(xml)
    journey_pattern = JourneyPatternSection.from_txc(element)
    snapshot.assert_match(journey_pattern.dict())


def test_parse_journey_pattern_timing_link(snapshot):
    """Can we parse a well formed JourneyPatternTimingLink."""
    xml = f"""
      <JourneyPatternTimingLink {NSPACE} id="JPTL32">
        <From SequenceNumber="2" id="JPSU63">
          <Activity>pickUpAndSetDown</Activity>
          <DynamicDestinationDisplay>Stockton</DynamicDestinationDisplay>
          <StopPointRef>077072001X</StopPointRef>
          <TimingStatus>principalTimingPoint</TimingStatus>
        </From>
        <To SequenceNumber="3" id="JPSU64">
          <Activity>pickUpAndSetDown</Activity>
          <DynamicDestinationDisplay>Stockton</DynamicDestinationDisplay>
          <StopPointRef>077072405B</StopPointRef>
          <TimingStatus>otherPoint</TimingStatus>
        </To>
        <RouteLinkRef>RL2</RouteLinkRef>
        <RunTime>PT0M0S</RunTime>
      </JourneyPatternTimingLink>
    """
    element = etree.fromstring(xml)
    timing_link = JourneyPatternTimingLink.from_txc(element)
    snapshot.assert_match(timing_link.json())