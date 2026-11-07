"""
Здесь необходимо реализовать Adapter.

Класс должен реализовать interfaces.BaseDigitalClock и использовать
существующий clocks.AnalogClock через композицию.
"""

from datetime import datetime

from clocks import AnalogClock
from consts import DayNightDivision
from interfaces import BaseDigitalClock


class DigitalClockAdapter(BaseDigitalClock):

    def __init__(self, analog_clock: AnalogClock | None = None) -> None:
        self._analog_clock = analog_clock if analog_clock is not None else AnalogClock()

    @staticmethod
    def _to_analog_values(date: datetime) -> tuple[float, float, float, DayNightDivision]:
        hour = date.hour
        minute = date.minute
        second = date.second
        day_night_division = DayNightDivision.AM if hour < 12 else DayNightDivision.PM
        hour_12 = hour % 12

        hour_angle = hour_12 * 30.0 + minute * 0.5 + second / 120.0
        minute_angle = minute * 6.0 + second * 0.1
        second_angle = second * 6.0

        return hour_angle, minute_angle, second_angle, day_night_division

    @staticmethod
    def _from_analog_values(
        hour_angle: float,
        minute_angle: float,
        second_angle: float,
        day_night_division: DayNightDivision,
        year: int,
        month: int,
        day: int,
    ) -> datetime:
        normalized_hour_angle = hour_angle % 360.0
        second = int(round((second_angle % 360.0) / 6.0)) % 60
        minute = int(round((minute_angle - second * 0.1) / 6.0)) % 60
        hour_12 = int(normalized_hour_angle // 30.0) % 12

        if day_night_division is DayNightDivision.AM:
            hour = 0 if hour_12 == 0 and normalized_hour_angle == 0 else hour_12
        else:
            hour = 12 if hour_12 == 0 and normalized_hour_angle == 0 else hour_12 + 12

        if hour == 24:
            hour = 0

        return datetime(year, month, day, hour, minute, second)

    def set_date_time(self, date: datetime) -> None:
        hour_angle, minute_angle, second_angle, day_night_division = self._to_analog_values(date)
        self._analog_clock.set_date_time(
            year=date.year,
            month=date.month,
            day=date.day,
            hour_angle=hour_angle,
            minute_angle=minute_angle,
            second_angle=second_angle,
            day_night_division=day_night_division,
        )

    def get_date_time(self) -> datetime:
        return self._from_analog_values(
            hour_angle=self._analog_clock.get_hour_angle(),
            minute_angle=self._analog_clock.get_minute_angle(),
            second_angle=self._analog_clock.get_second_angle(),
            day_night_division=self._analog_clock.get_day_night_division(),
            year=self._analog_clock.get_year(),
            month=self._analog_clock.get_month(),
            day=self._analog_clock.get_day(),
        )
