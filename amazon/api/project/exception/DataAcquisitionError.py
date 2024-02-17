from amazon.api.project.constants import Message


class DataAquisitionException(Exception):
    def __init__(self):
        super().__init__(Message.ERROR_FAIL_DATA_ACQUISITION)
