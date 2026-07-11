import random
from datetime import date, timedelta
import pandas as pd
from .json_utils import write_json


class Generator:
    def __init__(self, cities: list[str], start_date: date, end_date: date) -> None:
        self.cities = cities

        self.start_date = start_date
        self.end_date = end_date

        self.date_range = pd.date_range(start_date, end_date, freq="D")

    def gen_networks(
        self,
        min_air_quality: float = 10,
        max_air_quality: float = 70,
        min_temp: float = 10,
        max_temp: float = 30,
        min_hum: float = 40,
        max_hum: float = 90,
    ) -> None:
        # generate networks
        network_A = self._gen_network_A(min_air_quality, max_air_quality)
        network_B = self._gen_network_B(min_temp, max_temp, min_hum, max_hum)

        # add noise to data
        self._delete_weekends_B(network_B)
        self._nan_A(network_A)
        self._delete_city(network_B)

        # persist data
        write_json("data/network_A.json", network_A)
        write_json("data/network_B.json", network_B)

    def _gen_network_A(
        self, min_air_quality: float = 10, max_air_quality: float = 70
    ) -> dict:
        range_air_quality = max_air_quality - min_air_quality
        network_A = {}
        for city in self.cities:
            sensor_A = {}
            for date in self.date_range:
                sensor_A[str(date)] = (
                    min_air_quality + range_air_quality * random.random()
                )
            network_A[city] = sensor_A
        return network_A

    def _gen_network_B(
        self,
        min_temp: float = 10,
        max_temp: float = 30,
        min_hum: float = 40,
        max_hum: float = 90,
    ) -> dict:
        network_B = {}
        for city in self.cities:
            sensor_B = {}
            for date in self.date_range:
                met_vars = {
                    "temperature": self._gen_rand_var(min_temp, max_temp),
                    "humidity": self._gen_rand_var(min_hum, max_hum),
                }
                sensor_B[str(date)] = met_vars
            network_B[city] = sensor_B
        return network_B

    def _delete_weekends_B(self, network_B: dict) -> None:
        """Delete weekends"""
        for _, sensor_B in network_B.items():
            dates_to_drop = []
            for day, (date, _) in enumerate(sensor_B.items()):
                if day % 7 < 2:
                    dates_to_drop.append(date)
            for date in dates_to_drop:
                del sensor_B[date]

    def _nan_A(self, network_A: dict) -> None:
        """Add None to random consecutive days"""
        random.shuffle(self.cities)
        for city in self.cities[: int(len(self.cities) / 4)]:
            start_date = self._gen_rand_date(self.start_date, self.end_date)
            week = pd.date_range(
                start_date,
                min(start_date + timedelta(7), self.end_date),
                freq="D",
            )
            for date in week:
                network_A[city][str(date)] = None

    def _delete_city(self, network_B: dict) -> None:
        """Delete random city"""
        del network_B[random.choice(self.cities)]

    def _gen_rand_var(self, min_val: float, max_val: float) -> float:
        range_val = max_val - min_val
        rand_val = min_val + range_val * random.random()
        return round(rand_val, 1)

    def _gen_rand_date(self, start: date, end: date) -> date:
        range_days = (end - start).days
        rand_delta_days = random.randint(0, range_days)
        rand_day = start + timedelta(rand_delta_days)
        return rand_day
