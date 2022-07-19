from typing import Literal

QueryType = Literal["VIN", "BODY", "GRZ"]


class QueryNumber:
    VIN: Literal["VIN"] = "VIN"
    BODY: Literal["BODY"] = "BODY"
    GRZ: Literal["GRZ"] = "GRZ"


__all__ = ["QueryNumber", "QueryType"]
