"""
Здесь необходимо реализовать Facade.

Фасад должен скрывать работу как минимум с:
- цифровым адаптером;
- ClockFormatter;
- ClockHistory.
"""

from datetime import datetime

from adapters.digital_clock_adapter import DigitalClockAdapter
from services import ClockFormatter, ClockHistory


class ClockFacade:

    def __init__(self, clock: DigitalClockAdapter | None = None) -> None:
        self._clock = clock if clock is not None else DigitalClockAdapter()
        self._formatter = ClockFormatter()
        self._history = ClockHistory()

    def set_current_date_time(self, value: datetime) -> None:
        self._clock.set_date_time(value)
        self._history.add(value)

    def get_current_date_time(self) -> datetime:
        return self._clock.get_date_time()

    def get_formatted_date_time(self, fmt: str = "%d.%m.%Y %H:%M:%S") -> str:
        return self._formatter.format(self.get_current_date_time(), fmt)

    def get_history(self) -> tuple[datetime, ...]:
        return self._history.all()

    def get_clock(self) -> DigitalClockAdapter:
        return self._clock
