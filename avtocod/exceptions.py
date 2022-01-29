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


class ValidationError(AvtocodException):
    pass
