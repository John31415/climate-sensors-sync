import pandas as pd


class Diagnostic:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def prc_miss_city(self) -> pd.Series:
        return (self.df.isna().mean() * 100.0).round(1)

    def prc_dates_full_data(self) -> pd.Series:
        cities = self.df.columns.get_level_values("city").unique()
        cnt = {city: self.df[city].notna().all(axis=1).mean() * 100 for city in cities}
        return pd.Series(cnt).round(1)

    def risk_index(
        self, w_air_q: float = 0.5, w_temp: float = 0.3, w_hum: float = 0.2
    ) -> pd.DataFrame:
        city_date_risk = {}
        cities = self.df.columns.get_level_values("city").unique()
        for city in cities:
            air_q = w_air_q * self._air_q_penalty(self.df[city]["air_quality"])
            temp = w_temp * self._temp_penalty(self.df[city]["temperature"])
            hum = w_hum * self._hum_penalty(self.df[city]["humidity"])
            risk_index = air_q + temp + hum
            city_date_risk[city] = risk_index
        df_risk_index = pd.DataFrame(city_date_risk)
        return df_risk_index

    def city_var_mean(self, df: pd.DataFrame) -> pd.Series:
        return df.mean()

    def city_var_std(self, df: pd.DataFrame) -> pd.Series:
        return df.std()

    def city_var_min(self, df: pd.DataFrame) -> pd.Series:
        return df.min()

    def city_var_max(self, df: pd.DataFrame) -> pd.Series:
        return df.max()

    def extreme_city(self, risk_index: pd.DataFrame) -> str:
        return str(self.city_var_max(risk_index).idxmax())

    def _air_q_penalty(self, air_q: pd.Series) -> pd.Series:
        air_q_safe = 25
        penalty_air_q = ((air_q - air_q_safe) / air_q_safe).clip(lower=0)
        return penalty_air_q.clip(upper=1)

    def _temp_penalty(self, temp: pd.Series) -> pd.Series:
        temp_ideal = 21.0
        temp_tolerance = 7.0
        penalty_temp = ((temp - temp_ideal) / temp_tolerance) ** 2
        return penalty_temp.clip(upper=1)

    def _hum_penalty(self, hum: pd.Series) -> pd.Series:
        hum_ideal = 50
        hum_tolerance = 25
        penalty_hum = ((hum - hum_ideal) / hum_tolerance) ** 2
        return penalty_hum.clip(upper=1)
