# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    "test_days_of_operation 1"
] = '{"attributes": null, "regular_day_type": {"attributes": null, "days_of_week": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "holidays_only": false}, "bank_holiday_operation": null}'

snapshots[
    "test_operating_profile 1"
] = '{"attributes": null, "regular_day_type": {"attributes": null, "days_of_week": [], "holidays_only": true}, "bank_holiday_operation": {"attributes": null, "days_of_operation": ["GoodFriday", "LateSummerBankHolidayNotScotland", "MayDay", "EasterMonday", "SpringBank"], "days_of_non_operation": ["ChristmasDay", "BoxingDay", "NewYearsDay", "ChristmasDayHoliday", "BoxingDayHoliday", "NewYearsDayHoliday", "ChristmasEve", "NewYearsEve"]}}'

snapshots[
    "test_services 1"

snapshots[
    "test_standard_service 1"

snapshots[
    "test_standard_service_none_use_all_stop_points 1"
] = '{"attributes": null, "origin": "Great Yarmouth", "destination": "Burgh Castle", "use_all_stop_points": null, "journey_pattern": [], "vias": ["Bradwell"]}'