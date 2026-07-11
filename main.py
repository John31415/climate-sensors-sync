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

PATH_NETWORK_A = "data/network_A.json"
PATH_NETWORK_B = "data/network_B.json"


def main() -> None:
    # generate scenario
    generator = Generator(CITIES, START_DATE, END_DATE, PATH_NETWORK_A, PATH_NETWORK_B)
    generator.gen_networks()

    # process data
    processor = DataProcessor(PATH_NETWORK_A, PATH_NETWORK_B)
    df = processor.process_data()


if __name__ == "__main__":
    main()
