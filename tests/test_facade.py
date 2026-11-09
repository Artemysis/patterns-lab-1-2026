from datetime import datetime

from facades import ClockFacade


def test_facade_sets_and_formats_history() -> None:
    facade = ClockFacade()
    value = datetime(2026, 9, 24, 12, 34, 56)

    facade.set_current_date_time(value)

    assert facade.get_current_date_time() == value
    assert facade.get_formatted_date_time() == "24.09.2026 12:34:56"
    assert facade.get_history() == (value,)


def test_facade_keeps_multiple_history_entries() -> None:
    facade = ClockFacade()
    first = datetime(2026, 9, 24, 12, 34, 56)
    second = datetime(2026, 9, 25, 1, 2, 3)

    facade.set_current_date_time(first)
    facade.set_current_date_time(second)

    assert facade.get_history() == (first, second)
