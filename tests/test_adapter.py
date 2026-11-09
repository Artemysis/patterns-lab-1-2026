from datetime import datetime

from adapters import DigitalClockAdapter
from consts import DayNightDivision


def test_adapter_sets_and_gets_datetime() -> None:
    adapter = DigitalClockAdapter()
    value = datetime(2026, 9, 24, 12, 34, 56)

    adapter.set_date_time(value)

    assert adapter.get_date_time() == value
    assert adapter._analog_clock.get_day_night_division() is DayNightDivision.PM
    assert adapter._analog_clock.get_hour_angle() == (12 % 12) * 30.0 + 34 * 0.5 + 56 / 120.0
    assert adapter._analog_clock.get_minute_angle() == 34 * 6.0 + 56 * 0.1
    assert adapter._analog_clock.get_second_angle() == 56 * 6.0


def test_adapter_handles_midnight_and_noon() -> None:
    adapter = DigitalClockAdapter()

    adapter.set_date_time(datetime(2026, 9, 24, 0, 0, 0))
    assert adapter.get_date_time() == datetime(2026, 9, 24, 0, 0, 0)
    assert adapter._analog_clock.get_day_night_division() is DayNightDivision.AM

    adapter.set_date_time(datetime(2026, 9, 24, 12, 0, 0))
    assert adapter.get_date_time() == datetime(2026, 9, 24, 12, 0, 0)
    assert adapter._analog_clock.get_day_night_division() is DayNightDivision.PM

