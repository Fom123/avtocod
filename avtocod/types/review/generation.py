from avtocod.types.base import AvtocodObject


class ReviewGeneration(AvtocodObject):
    uuid: str
    channel: str
    max_generation_time: int


class ReviewUpgrade(AvtocodObject):
    channel: str
    max_wait_to_ready_time: int


__all__ = ["ReviewGeneration", "ReviewUpgrade"]
