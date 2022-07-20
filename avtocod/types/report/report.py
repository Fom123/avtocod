from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import Field

from avtocod.types.base import AvtocodObject
from avtocod.types.report.report_entities.accidents import Accidents, Pledges
from avtocod.types.report.report_entities.additional_info import AdditionalInfo
from avtocod.types.report.report_entities.calculate import Calculate
from avtocod.types.report.report_entities.fines import Fines
from avtocod.types.report.report_entities.gots_action import GotsAuctions
from avtocod.types.report.report_entities.identifiers import Identifiers
from avtocod.types.report.report_entities.last_generation_stat import LastGenerationStat
from avtocod.types.report.report_entities.market_price import MarketPrices
from avtocod.types.report.report_entities.metadata import Metadata
from avtocod.types.report.report_entities.mileages import Mileages
from avtocod.types.report.report_entities.owner import Ownership
from avtocod.types.report.report_entities.photos import Images
from avtocod.types.report.report_entities.query import Query
from avtocod.types.report.report_entities.state import State
from avtocod.types.report.report_entities.stealings import Stealings
from avtocod.types.report.report_entities.tech_data import TechData
from avtocod.types.report.report_entities.utilization import Utilizations
from avtocod.types.report.short_information import ShortInformation
from avtocod.types.reusable import CountItems
from avtocod.utils.utils import rgetattr


class ContentData(AvtocodObject):
    pledges: Optional[Pledges] = None
    mileages: Optional[Mileages] = None
    metadata: Optional[Metadata] = Field(None, alias="_metadata")
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
    fines: Optional[Fines] = None

    commercial_use: Optional[CountItems] = None
    additional_info: Optional[AdditionalInfo] = None
    service_history: Optional[CountItems] = None
    diagnostic_cards: Optional[CountItems] = None
    recall_campaigns: Optional[CountItems] = None
    identifiers_masked: Optional[Identifiers] = None
    images: Optional[Images] = None
    market_prices: Optional[MarketPrices] = None

    carfax: Optional[Dict[str, Any]] = None  # TODO
    registration_actions: Optional[Dict[str, Any]] = None  # TODO
    restrictions: Optional[Dict[str, Any]] = None  # TODO
    ads: Optional[Dict[str, Any]] = None  # TODO
    customs: Optional[Dict[str, Any]] = None  # TODO
    repairs: Optional[Dict[str, Any]] = None  # TODO
    leasing: Optional[Dict[str, Any]] = None  # TODO
    taxi: Optional[Dict[str, Any]] = None  # TODO
    insurance: Optional[Dict[str, Any]] = None  # TODO
    leasings: Optional[Dict[str, Any]] = None  # TODO


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
    last_generation_stat: Optional[LastGenerationStat] = None


class Report(AvtocodObject):
    uuid: str
    """Unique id of avtocod report"""

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
            photos = [photo.uri for photo in photos]

        return ShortInformation(
            uuid=uuid,  # type: ignore
            car_time=car_time,
            title=title,
            query_type=query_type,
            gos_number=gos_number,
            vin=vin,
            photos=photos,
            logotype=logotype,
        )  # unpack all the filtered variables


# __all__ = ["Review"] # cuz I don't want to export all types in tests
