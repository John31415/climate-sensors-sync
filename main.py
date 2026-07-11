from src import *
from datetime import date

CITIES = [
    "Madrid",
    "Barcelona",
    "Sevilla",
    "Valencia",
    "Granada",
    "Zamora",
    "Teruel",
    "Alicante",
]

START_DATE = date(2026, 12, 1)
END_DATE = date(2026, 12, 31)


def main() -> None:
    generator = Generator(CITIES, START_DATE, END_DATE)
    generator.gen_networks()


if __name__ == "__main__":
    main()
