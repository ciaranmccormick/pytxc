from pytxc.routes import Route, RouteLink, RouteSection
from tests.constants import NSPACE


def test_parse_route(snapshot):
    """Can we parse a well formed Route."""
    string = f"""
    <Route {NSPACE} id="RT39" CreationDateTime="2020-11-22T11:00:00"
        ModificationDateTime="2021-12-17T11:08:35"
        Modification="revise" RevisionNumber="159">
      <PrivateCode>35st-39</PrivateCode>
      <Description>Stockton - Wolviston Court</Description>
      <RouteSectionRef>RS1</RouteSectionRef>
    </Route>
    """
    route = Route.from_string(string)
    snapshot.assert_match(route.json(indent=2))


def test_parse_route_no_description(snapshot):
    """Can we parse a Route without a Description."""
    string = f"""
    <Route {NSPACE} id="RT39" CreationDateTime="2020-11-22T11:00:00"
        ModificationDateTime="2021-12-17T11:08:35"
        Modification="revise" RevisionNumber="159">
      <PrivateCode>35st-39</PrivateCode>
      <RouteSectionRef>RS1</RouteSectionRef>
    </Route>
    """
    route = Route.from_string(string)
    snapshot.assert_match(route.json(indent=2))


def test_parse_route_link_no_mapping(snapshot):
    """Can we parse a RouteLink without a Track string."""
    string = f"""
      <RouteLink {NSPACE} id="RL113" CreationDateTime="2020-11-22T11:00:00"
        ModificationDateTime="2021-12-17T11:08:35" Modification="revise"
        RevisionNumber="159">
        <From>
          <StopPointRef>077072746A</StopPointRef>
        </From>
        <To>
          <StopPointRef>077072574B</StopPointRef>
        </To>
        <Distance>696</Distance>
      </RouteLink>
    """
    route = RouteLink.from_string(string)
    snapshot.assert_match(route.json(indent=2))


def test_parase_route_section(snapshot):
    """Can we parse a route section containing well formed route links."""
    string = f"""
    <RouteSection {NSPACE} id="RS1">
      <RouteLink id="RL113" CreationDateTime="2020-11-22T11:00:00"
        ModificationDateTime="2021-12-17T11:08:35" Modification="revise"
        RevisionNumber="159">
        <From>
          <StopPointRef>077072746A</StopPointRef>
        </From>
        <To>
          <StopPointRef>077072574B</StopPointRef>
        </To>
        <Distance>696</Distance>
      </RouteLink>
      <RouteLink id="RL2" CreationDateTime="2020-11-22T11:00:00"
        ModificationDateTime="2021-12-17T11:08:35" Modification="revise"
        RevisionNumber="159">
        <From>
          <StopPointRef>077072001X</StopPointRef>
        </From>
        <To>
          <StopPointRef>077072405B</StopPointRef>
        </To>
        <Distance>172</Distance>
      </RouteLink>
    </RouteSection>
    """
    route = RouteSection.from_string(string)
    snapshot.assert_match(route.json(indent=2))
