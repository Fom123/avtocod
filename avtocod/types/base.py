import logging
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any, Dict
from unittest.mock import sentinel

from pydantic import BaseModel, Extra, root_validator

if TYPE_CHECKING:
    from avtocod.avtocod import AvtoCod

new_issue = "https://github.com/Fom123/avtocod"
logger = logging.getLogger(__name__)


def utcformat(dt: datetime, timespec: str = "seconds") -> str:
    """convert datetime to string in UTC format (YYYY-mm-ddTHH:MM:SS.mmmZ)"""
    return dt.astimezone(timezone.utc).isoformat("T", timespec)


class AvtocodObject(BaseModel):
    def __getitem__(self, item: Any) -> Any:  # for backwards compatibility
        return super().__getattribute__(item)

    @property
    def avtocod(self) -> "AvtoCod":
        """Returning an instance of :class:`AvtoCod`"""
        from avtocod.avtocod import AvtoCod

        instance = AvtoCod.get_current()

        if instance is None:
            raise RuntimeError(
                "Can't get client instance from context. "
                "You can fix this by setting the current instance: "
                "`AvtoCod.set_current(...)`"
            )
        return instance

    @root_validator(pre=True)
    def unknown_fields(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        all_required_field_names = {field.alias for field in cls.__fields__.values()}
        unknown_fields = {k: v for k, v in values.items() if k not in all_required_field_names}
        if unknown_fields:
            logger.warning(
                "Found unknown fields received from API! Please copy warn message and send to "
                "%s (github issue), thank you!",
                new_issue,
            )
            logger.warning("Type: %s; fields: %s", str(cls), unknown_fields)
        return values

    class Config:
        use_enum_values = True
        orm_mode = True
        extra = Extra.allow
        validate_assignment = True
        allow_mutation = False
        allow_population_by_field_name = True
        json_encoders = {datetime: utcformat}


class MutableAvtocodObject(AvtocodObject):
    class Config:
        allow_mutation = True


UNSET: Any = (
    sentinel.UNSET
)  # special sentinel object which used in situation when None might be a useful value
