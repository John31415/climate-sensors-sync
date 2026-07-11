from .json_utils import read_json
import pandas as pd


class DataProcessor:
    def __init__(self, path_network_A: str, path_network_B: str) -> None:
        self.path_network_A = path_network_A
        self.path_network_B = path_network_B

    def process_data(self) -> pd.DataFrame:
        network_A = read_json(self.path_network_A)
        network_B = read_json(self.path_network_B)

        # create DataFrames
        df_A = self._create_df_A(network_A)
        df_B = self._create_df_B(network_B)

        # aligned data
        df = pd.concat([df_A, df_B], axis=1).sort_index(axis=1)

        # normalize sub-columns
        cities = df.columns.get_level_values("city").unique()
        variables = df.columns.get_level_values("variable").unique()
        mul_idx = pd.MultiIndex.from_product(
            [cities, variables], names=["city", "variable"]
        )
        df_normalized = df.reindex(columns=mul_idx).sort_index(axis=1)

        return df_normalized

    def _create_df_A(self, network_A: dict) -> pd.DataFrame:
        df_A = pd.DataFrame(network_A).sort_index()
        df_A.columns = pd.MultiIndex.from_product(
            [df_A.columns, ["air_quality"]], names=["city", "variable"]
        )
        df_A.sort_index().sort_index(axis=1)
        return df_A

    def _create_df_B(self, network_B: dict) -> pd.DataFrame:
        structured_data = {}
        for city, sensor_B in network_B.items():
            for date, met_vars in sensor_B.items():
                for var, value in met_vars.items():
                    if (city, var) not in structured_data:
                        structured_data[(city, var)] = {}
                    structured_data[(city, var)][date] = value
        df_B = pd.DataFrame(structured_data)
        df_B.columns = pd.MultiIndex.from_tuples(
            [tuple(col) for col in df_B.columns], names=["city", "variable"]
        )
        df_B.sort_index().sort_index(axis=1)
        return df_B
