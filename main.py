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

    # diagnostics
    diagnostic = Diagnostic(df)

    # report
    report("Percent of missing data per city", diagnostic.prc_miss_city())
    report("Percent of dates with full data per city", diagnostic.prc_dates_full_data())
    report("Risk Index", diagnostic.risk_index())
    report("Max", diagnostic.city_var_max(df))
    report("Min", diagnostic.city_var_min(df))
    report("Mean", diagnostic.city_var_mean(df))
    report("Standard deviation", diagnostic.city_var_std(df))
    report(
        "City with most extreme enviromental conditions",
        diagnostic.extreme_city(diagnostic.risk_index()),
    )


if __name__ == "__main__":
    main()
