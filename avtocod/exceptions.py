from __future__ import annotations

from typing import TYPE_CHECKING, Any, Mapping, Union, List, Tuple

if TYPE_CHECKING:
    from avtocod.methods import AvtocodMethod, AvtocodType


class AvtocodException(Exception):
    pass


class Unauthorized(AvtocodException):
    pass


class NetworkError(AvtocodException):
    pass


class CouldNotFindCar(AvtocodException):
    pass


class InvalidRequest(AvtocodException):
    pass


class SubscriptionNotFound(AvtocodException):
    pass


class AccountBanned(AvtocodException):
    pass


class SessionExpired(AvtocodException):
    pass


class NotEnoughRepairBalance(AvtocodException):
    pass


class ReportNotFound(AvtocodException):
    pass


class InternalError(AvtocodException):
    pass


class ValidationError(AvtocodException):
    pass


class InvalidArgument(AvtocodException):
    pass


class ReportGenerationLimitExceeded(AvtocodException):
    pass


class PipelineException(AvtocodException):
    def __init__(
        self,
        *args: Any,
        results_and_error: List[Tuple[AvtocodMethod[AvtocodType], Union[AvtocodType, AvtocodException]]],
    ):
        self.results_and_error = results_and_error
        super().__init__(*args)
