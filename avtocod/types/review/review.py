from datetime import datetime
from typing import Any, List, Optional

from avtocod.types.base import AvtocodObject, DateUpdate
from avtocod.types.review.identifiers import Identifiers
from avtocod.types.review.short_information import ShortInformation
from avtocod.types.review.tech_data import TechData
from avtocod.utils import filter_payload, rgetattr


class Query(AvtocodObject):
    body: Optional[str] = None
    type: Optional[str] = None
    storages: Optional[List[Any]] = None
    schema_version: Optional[str] = None


class CountItems(AvtocodObject):
    count: Optional[int] = None
    items: Optional[List[Any]] = None
    _comment: Optional[str] = None


class Actuality(AvtocodObject):
    date: Optional[str] = None


class FilledBy(AvtocodObject):
    source: Optional[str] = None


class Item(AvtocodObject):
    _id: Optional[int] = None
    mileage: Optional[int] = None
    actuality: Optional[Actuality] = None
    filled_by: Optional[FilledBy] = None


class Mileages(CountItems):
    items: Optional[List[Item]] = None


class Utilizations(CountItems):
    was_utilized: Optional[bool] = None


class GotsAuctions(AvtocodObject):
    items: Optional[List[Any]] = None
    _comment: Optional[str] = None


class GeoOwner(AvtocodObject):
    city: Optional[str] = None
    region: Optional[str] = None


class OwnerInfo(AvtocodObject):
    geo: Optional[GeoOwner] = None
    type: Optional[str] = None
    enforcement_proceedings: Any


class Segment(AvtocodObject):
    euro: Optional[List[Any]] = None


class Category(AvtocodObject):
    code: Optional[str] = None
    description: Optional[str] = None


class Org(AvtocodObject):
    name: Optional[str] = None


class DatePassport(AvtocodObject):
    receive: Optional[str] = None


class Passport(AvtocodObject):
    org: Optional[Org] = None
    date: Optional[DatePassport] = None
    number: Optional[str] = None
    has_dublicate: Optional[bool] = None


class Modifications(AvtocodObject):
    was_modificated: Optional[bool] = None


class VehicleInfo(AvtocodObject):
    notes: Optional[List[str]] = None
    owner: Optional[OwnerInfo] = None
    segment: Optional[Segment] = None
    category: Optional[Category] = None
    exported: Optional[bool] = None
    passport: Optional[Passport] = None
    modifications: Optional[Modifications] = None


class IdentifiersInfo(AvtocodObject):
    vin: Optional[List[Any]] = None


class AdditionalInfo(AvtocodObject):
    vehicle: Optional[VehicleInfo] = None
    identifiers: Optional[IdentifiersInfo] = None
    _comment: str


class VehicleMasked(AvtocodObject):
    pts: Optional[str] = None
    sts: Optional[str] = None
    body: Optional[str] = None
    chassis: Optional[str] = None
    reg_num: Optional[str] = None


class IdentifiersMasked(AvtocodObject):
    vehicle: Optional[VehicleMasked] = None
    _comment: Optional[str] = None


class Source(AvtocodObject):
    _id: Optional[str] = None
    state: Optional[str] = None
    extended_state: Optional[str] = None


class State(AvtocodObject):
    sources: Optional[List[Source]]


class Photos(AvtocodObject):
    date: Optional[DateUpdate] = None
    count: Optional[int] = None
    items: Optional[List[Any]] = None
    _comment: Optional[str] = None


class Pledges(AvtocodObject):
    date: Optional[DateUpdate] = None
    count: Optional[int] = None
    items: Optional[List[Any]] = None
    _comment: Optional[str] = None


class Regions(AvtocodObject):
    yearly: Optional[List[Any]] = None


class Current(AvtocodObject):
    city: Optional[List[Any]] = None
    region: Optional[List[Any]] = None
    yearly: Optional[List[Any]] = None


class MoscowRegion(AvtocodObject):
    yearly: Optional[List[Any]] = None


class Tax(AvtocodObject):
    moscow: Optional[MoscowRegion] = None
    regions: Optional[Regions] = None


class Price(AvtocodObject):
    moscow: Optional[MoscowRegion] = None
    current: Optional[Current] = None
    moscow_region: Optional[MoscowRegion] = None


class Regional(AvtocodObject):
    value: Optional[float] = None


class Coefficients(AvtocodObject):
    regional: Optional[Regional] = None


class Osago(AvtocodObject):
    price: Optional[Price] = None
    _comment: Optional[str] = None
    coefficients: Optional[Coefficients] = None


class Calculate(AvtocodObject):
    tax: Optional[Tax] = None
    osago: Optional[Osago] = None
    _comment: Optional[str] = None


class DateHistory(AvtocodObject):
    start: str
    end: Optional[str] = None


class OwnerHistory(AvtocodObject):
    type: Optional[str] = None
    company: Optional[Any] = None


class LastOperation(AvtocodObject):
    code: Optional[str] = None
    description: Optional[str] = None


class ItemHistory(AvtocodObject):
    _id: Optional[int] = None
    date: Optional[DateHistory] = None
    owner: Optional[OwnerHistory] = None
    last_operation: Optional[LastOperation] = None


class HistoryOwnership(AvtocodObject):
    date: Optional[DateUpdate] = None
    count: Optional[int] = None
    items: Optional[List[ItemHistory]] = None
    _comment: Optional[str] = None


class Ownership(AvtocodObject):
    history: Optional[HistoryOwnership] = None


class Stealings(CountItems):
    date: Optional[DateUpdate] = None
    is_wanted: Optional[bool] = None


class Items(AvtocodObject):
    _id: Optional[int] = None
    uri: Optional[str] = None


class Images(AvtocodObject):
    photos: Optional[Photos] = None


class Application(AvtocodObject):
    uid: Optional[str] = None
    version: Optional[str] = None


class Metadata(AvtocodObject):
    _comment: Optional[str] = None
    application: Optional[Application] = None


class Accidents(AvtocodObject):
    history: Optional[Pledges] = None
    insurance: Optional[DateUpdate] = None
    has_accidents: Optional[bool] = None


class ContentData(AvtocodObject):
    pledges: Optional[Pledges] = None
    mileages: Optional[Mileages] = None
    _metadata: Optional[Metadata] = None
    accidents: Optional[Accidents] = None
    calculate: Optional[Calculate] = None
    car_price: Optional[CountItems] = None
    ownership: Optional[Ownership] = None
    stealings: Optional[Stealings] = None
    tech_data: Optional[TechData] = None
    identifiers: Optional[Identifiers] = None
    arbitration: Optional[CountItems] = None
    report_meta: Optional[List[Any]] = None
    pledges_nbki: Optional[CountItems] = None
    utilizations: Optional[Utilizations] = None
    gots_auctions: Optional[GotsAuctions] = None

    commercial_use: Optional[CountItems] = None
    additional_info: Optional[AdditionalInfo] = None
    service_history: Optional[CountItems] = None
    diagnostic_cards: Optional[CountItems] = None
    recall_campaigns: Optional[CountItems] = None
    identifiers_masked: Optional[IdentifiersMasked] = None
    images: Optional[Images] = None


class Content(AvtocodObject):
    uid: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[str] = None
    query: Optional[Query] = None
    state: Optional[State] = None
    comment: Optional[str] = None
    content: Optional[ContentData] = None
    active_to: Optional[datetime] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    domain_uid: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    vehicle_id: Optional[str] = None
    active_from: Optional[str] = None
    progress_ok: Optional[int] = None
    requested_at: Optional[str] = None
    progress_wait: Optional[int] = None
    progress_error: Optional[int] = None
    report_type_uid: Optional[str] = None


class Review(AvtocodObject):
    uuid: Optional[str] = None
    """Unique id of avtocod review"""

    client_uuid: Optional[str] = None
    """Id of the client who requested the information"""
    content: Optional[Content] = None
    """Content Information"""

    is_ready: bool
    is_completed: bool
    tags_ids: List[Any]
    stage: str
    auto_index: int
    analytical_mileage: int

    max_wait_to_ready_time: Optional[int] = None
    wait_to_ready_time: Optional[int] = None

    guarantee_status: str
    generation_start_time: datetime
    additional_blocks: List[Any]
    created_at: datetime
    updated_at: datetime

    @property
    def information(self) -> ShortInformation:
        """
        function which provides you the basic information about car

        :return: ShortInformation object with None attributes if not found
        """

        def filter_args(*args: Any) -> str:
            return ".".join(args)

        content = ["content", "content"]
        identifiers = content + ["identifiers"]
        vehicle = identifiers + ["vehicle"]
        tech_data = content + ["tech_data"]
        brand = tech_data + ["brand"]

        uuid = getattr(self, "uuid", None)
        query_type = rgetattr(self, filter_args("content", "query", "type"), default=None)
        car_time = rgetattr(self, filter_args(*tech_data, "year"), default=None)
        vin = rgetattr(self, filter_args(*vehicle, "vin"), default=None)
        gos_number = rgetattr(self, filter_args(*vehicle, "reg_num"), default=None)
        logotype = rgetattr(self, filter_args(*brand, "logotype", "uri"), default=None)
        title = rgetattr(self, filter_args(*brand, "name", "original"), default=None)
        photos = rgetattr(
            self,
            filter_args(*identifiers, "images", "photos", "items", "item"),
            default=None,
        )

        if photos:
            photo = photos[0].uri

        payload = filter_payload(
            **locals(),
            exclude=[
                "photos",
                "brand",
                "tech_data",
                "vehicle",
                "identifiers",
                "content",
            ],
        )  # filter all our variables before passing it
        return ShortInformation(**payload)  # unpack all the filtered variables


__all__ = ["Review"]
