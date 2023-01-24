# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    "test_operational 1"
] = """{
  "attributes": null,
  "ticket_machine": {
    "attributes": null,
    "journey_code": "7"
  },
  "block": null
}"""

snapshots[
    "test_parsing_operating_period 1"
] = '{"attributes": null, "regular_day_type": {"attributes": null, "days_of_week": [], "holidays_only": true}, "bank_holiday_operation": {"attributes": null, "days_of_operation": ["ChristmasEve", "NewYearsEve"], "days_of_non_operation": ["ChristmasDay", "BoxingDay", "GoodFriday", "NewYearsDay", "LateSummerBankHolidayNotScotland", "MayDay", "EasterMonday", "SpringBank", "ChristmasDayHoliday", "BoxingDayHoliday", "NewYearsDayHoliday"]}}'
