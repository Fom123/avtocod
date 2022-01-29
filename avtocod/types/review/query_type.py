from typing import Literal

QueryType = Literal["VIN", "BODY", "GRZ"]


class QueryNumber:
    VIN: str = "VIN"
    BODY: str = "BODY"
    GRZ: str = "GRZ"
