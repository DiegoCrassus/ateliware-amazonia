import requests
from amazon.api.settings import Config
from amazon.api.project.exception import DataAquisitionException


class Table(Config):
    def __init__(self):
        Config.__init__(self)
        self.distance = 0
        self.started = False
        self.weights = self.get_weights()

        if not self.started:
            raise DataAquisitionException

    def get_weights(self):
        weights = requests.get(self.URL_WEIGHTS).json()
        if weights:
            self.started = True
            return weights
        else:
            self.started = False

    def forward(self, ancor):
        if ancor not in self.weights.keys():
            raise ValueError(f"Given value '{ancor}' is invalid!")

        else:
            return self.weights[ancor]

    def table_positions(self):
        return list(set(self.weights.keys()))
