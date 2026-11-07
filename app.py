from datetime import datetime

from facades import ClockFacade


def main() -> None:
    facade = ClockFacade()
    now = datetime(2026, 9, 24, 12, 34, 56)

    facade.set_current_date_time(now)
    print("Фасад для подсистемы часов создан.")
    print(f"Текущая дата и время: {facade.get_current_date_time()}")
    print(f"Форматированное представление: {facade.get_formatted_date_time()}")
    print(f"История изменений: {facade.get_history()}")


if __name__ == "__main__":
    main()
