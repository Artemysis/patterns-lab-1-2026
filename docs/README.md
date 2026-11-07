# Диаграмма архитектуры
classDiagram
    class BaseDigitalClock {
        +set_date_time(date: datetime)
        +get_date_time() datetime
    }

    class BaseAnalogClock {
        +set_date_time(year, month, day, hour_angle, minute_angle, second_angle, day_night_division)
        +get_hour_angle() float
        +get_minute_angle() float
        +get_second_angle() float
        +get_year() int
        +get_month() int
        +get_day() int
        +get_day_night_division() DayNightDivision
    }

    class AnalogClock {
        +set_date_time(...)
        +get_hour_angle() float
        +get_minute_angle() float
        +get_second_angle() float
        +get_year() int
        +get_month() int
        +get_day() int
        +get_day_night_division() DayNightDivision
    }

    class DigitalClockAdapter {
        -_analog_clock: AnalogClock
        +set_date_time(date: datetime)
        +get_date_time() datetime
    }

    class ClockFormatter {
        +format(value: datetime, fmt: str) str
    }

    class ClockHistory {
        -_items: list[datetime]
        +add(value: datetime)
        +all() tuple[datetime]
    }

    class ClockFacade {
        -_clock: DigitalClockAdapter
        -_formatter: ClockFormatter
        -_history: ClockHistory
        +set_current_date_time(value: datetime)
        +get_current_date_time() datetime
        +get_formatted_date_time(fmt: str) str
        +get_history() tuple[datetime]
    }

    class DigitalClockDisplay {
        -_clock: BaseDigitalClock
        +render() str
    }

    BaseAnalogClock <|-- AnalogClock
    BaseDigitalClock <|-- DigitalClockAdapter
    AnalogClock <-- DigitalClockAdapter
    DigitalClockAdapter --> ClockFacade
    ClockFormatter --> ClockFacade
    ClockHistory --> ClockFacade
    BaseDigitalClock <-- DigitalClockDisplay
```
