import datetime

import pytest

from avtocod.types import Identifiers, Report, TechData, Vehicle
from avtocod.types.report.report import Content, ContentData
from avtocod.types.report.report_entities.accidents import (
    Accidents,
    Geo,
    ItemsOfPledges,
    ItemVehicle,
    Pledges,
)
from avtocod.types.report.report_entities.additional_info import (
    AdditionalInfo,
    Category,
    DatePassport,
    GeoOwner,
    IdentifiersInfo,
    Modifications,
    OwnerInfo,
    Passport,
    Segment,
    VehicleInfo,
)
from avtocod.types.report.report_entities.calculate import Calculate, Coefficients, Osago, Tax
from avtocod.types.report.report_entities.fines import (
    Article,
    Bank,
    Fines,
    FinesItems,
    Fssp,
    Location,
    Number,
    Payment,
    User,
    Wire,
)
from avtocod.types.report.report_entities.gots_action import GotsAuctions
from avtocod.types.report.report_entities.last_generation_stat import LastGenerationStat
from avtocod.types.report.report_entities.market_price import (
    Ads,
    AdsItem,
    GeoAd,
    MarketPrices,
    RelatedAd,
    VehicleAd,
)
from avtocod.types.report.report_entities.metadata import Application, Metadata
from avtocod.types.report.report_entities.mileages import Actuality, FilledBy, Item, Mileages
from avtocod.types.report.report_entities.owner import (
    HistoryOwnership,
    ItemHistory,
    LastOperation,
    OwnerHistory,
    Ownership,
)
from avtocod.types.report.report_entities.photos import (
    Images,
    PhotoItemVehicle,
    Photos,
    PhotosItem,
)
from avtocod.types.report.report_entities.query import Query
from avtocod.types.report.report_entities.state import Source, State
from avtocod.types.report.report_entities.stealings import Stealings
from avtocod.types.report.report_entities.tech_data import (
    Bodies,
    BodiesModification,
    Body,
    Brand,
    Chassis,
    Color,
    Drive,
    Engine,
    Fuel,
    Generations,
    Logotype,
    Model,
    OriginalNormalizedName,
    Power,
    Standarts,
    Transmission,
    Type,
    Weight,
    Wheel,
)
from avtocod.types.report.report_entities.utilization import Utilizations
from avtocod.types.reusable import (
    Count,
    CountItems,
    Current,
    DateDate,
    DateEnd,
    DateEndPercent,
    DateEvent,
    DatePublish,
    DateStartEnd,
    DateUpdate,
    Issued,
    MaxMin,
    Name,
    PositionAndPositionId,
    PriceWithRegion,
    Regions,
    StartEnd,
    Total,
    TypeA,
    TypeAndTypeId,
    Value,
)


@pytest.fixture(scope="function")
def report():
    return Report(
        uuid="2245ff3c-70b6-41ba-986b-c43a6633a335",
        client_uuid="141f3f95-3ff2-4fa5-8ee3-edfb361018ee",
        content=Content(
            uid="avtocod_profi_full_report_KNAFU611BA5295980@avtocod",
            name="NONAME",
            tags="",
            query=Query(body="KNAFU611BA5295980", type="VIN", storages=[], schema_version="1.0"),
            state=State(
                sources=[
                    Source(id="images.archive", state="OK", extended_state="OK"),
                    Source(id="images.avtonomer", state="OK", extended_state="OK"),
                    Source(id="carsharing.registry", state="OK", extended_state="OK"),
                    Source(id="fines.base", state="OK", extended_state="OK"),
                    Source(id="base", state="OK", extended_state="OK"),
                    Source(id="references.base", state="OK", extended_state="OK"),
                    Source(id="fssp.base", state="OK", extended_state="OK"),
                    Source(id="gibdd.restrict", state="OK", extended_state="OK"),
                    Source(id="gibdd.wanted", state="OK", extended_state="OK"),
                    Source(id="dtp.registry", state="OK", extended_state="OK"),
                    Source(id="customs.base", state="OK", extended_state="OK"),
                    Source(id="gibdd.dtp", state="OK", extended_state="OK"),
                    Source(id="gibdd.history", state="OK", extended_state="OK"),
                    Source(id="gibdd.eaisto", state="OK", extended_state="OK"),
                    Source(id="pledge", state="OK", extended_state="OK"),
                    Source(id="av.taxi", state="OK", extended_state="OK"),
                    Source(id="service.history", state="OK", extended_state="OK"),
                    Source(id="gibdd.fines", state="OK", extended_state="OK"),
                    Source(id="mileages.registry", state="OK", extended_state="OK"),
                    Source(id="recall.campaigns.registry", state="OK", extended_state="OK"),
                    Source(id="service.history.fitservice", state="OK", extended_state="OK"),
                    Source(id="ads.price.base", state="OK", extended_state="OK"),
                    Source(id="restrictions.registry", state="OK", extended_state="OK"),
                    Source(id="rsaosago.base", state="OK", extended_state="OK"),
                    Source(id="fines.base.ext", state="OK", extended_state="OK"),
                    Source(id="ads.price", state="OK", extended_state="OK"),
                    Source(id="ads.base", state="OK", extended_state="OK"),
                    Source(id="arbitration.history", state="OK", extended_state="OK"),
                ]
            ),
            comment="",
            content=ContentData(
                pledges=Pledges(
                    date=DateUpdate(update=datetime.datetime(2021, 12, 23, 0, 0)),
                    count=0,
                    items=[],
                    comment="Обременения на ТС",
                ),
                mileages=Mileages(
                    count=4,
                    items=[
                        Item(
                            id=4026845476,
                            mileage=118010,
                            actuality=Actuality(date="2021-12-02 20:34:24"),
                            filled_by=FilledBy(source="gibdd.eaisto"),
                            date={"event": "2017-06-22 00:00:00"},
                        ),
                        Item(
                            id=3598092514,
                            mileage=165000,
                            actuality=Actuality(date="2021-12-23 17:31:55"),
                            filled_by=FilledBy(source="images.archive"),
                            date={"event": "2019-01-24 00:00:00"},
                        ),
                        Item(
                            id=3079681658,
                            mileage=178400,
                            actuality=Actuality(date="2021-12-02 20:34:24"),
                            filled_by=FilledBy(source="gibdd.eaisto"),
                            date={"event": "2019-06-11 00:00:00"},
                        ),
                        Item(
                            id=3139863094,
                            mileage=215000,
                            actuality=Actuality(date="2021-12-02 20:34:24"),
                            filled_by=FilledBy(source="gibdd.eaisto"),
                            date={"event": "2020-12-02 00:00:00"},
                        ),
                    ],
                    comment="Пробеги",
                    date=None,
                ),
                metadata=Metadata(
                    comment="Мета-данные, не связанные с отчетом",
                    application=Application(
                        uid="processing@production-avtocodb2c-processing-queue-report_entities-facts-worker5cp7b",
                        version="60.2.0-",
                    ),
                    functions=None,
                ),
                accidents=Accidents(
                    history=Pledges(
                        date=DateUpdate(update=datetime.datetime(2021, 12, 23, 16, 56, 23)),
                        count=2,
                        items=[
                            ItemsOfPledges(
                                id=2058896394,
                                geo=Geo(
                                    city=None, house=None, region="Санкт-Петербург", street=None
                                ),
                                org=[],
                                type="Столкновение",
                                state="Повреждено",
                                damage=[],
                                number="400104624",
                                vehicle=ItemVehicle(
                                    year=2010, brand=Name(name="Kia"), model=Name(name="Cerato")
                                ),
                                accident=DateDate(date=datetime.datetime(2017, 9, 30, 4, 40)),
                                actuality=DateDate(date=datetime.datetime(2021, 12, 23, 19, 56)),
                                participants=Total(total=2),
                                other_participants=[],
                            ),
                            ItemsOfPledges(
                                id=761567625,
                                geo=Geo(
                                    city=None, house=None, region="Санкт-Петербург", street=None
                                ),
                                org=[],
                                type="Столкновение",
                                state="Повреждено",
                                damage=[],
                                number="400071712",
                                vehicle=ItemVehicle(
                                    year=2010, brand=Name(name="Kia"), model=Name(name="Cerato")
                                ),
                                accident=DateDate(date=datetime.datetime(2017, 7, 5, 13, 45)),
                                actuality=DateDate(date=datetime.datetime(2021, 12, 23, 19, 56)),
                                participants=Total(total=2),
                                other_participants=[],
                            ),
                        ],
                        comment="История ДТП",
                    ),
                    insurance={
                        "date": [],
                        "count": 0,
                        "items": [],
                        "_comment": "История повреждений из страховых компаний",
                    },
                    has_accidents=True,
                ),
                calculate=Calculate(
                    tax=Tax(moscow=Regions(yearly=[]), regions=Regions(yearly=[])),
                    osago=Osago(
                        price=PriceWithRegion(
                            moscow=Regions(yearly=[]),
                            current=Current(city=[], region=[], yearly=[]),
                            moscow_region=Regions(yearly=[]),
                            amount=None,
                            currency=None,
                        ),
                        comment="Калькулятор ОСАГО",
                        coefficients=Coefficients(regional=Value(value="1.8")),
                    ),
                    comment="Калькуляторы",
                ),
                car_price=CountItems(
                    count=0,
                    items=[],
                    comment="Приблизительные стоимости аналогичных автомобилей",
                    date=None,
                ),
                ownership=Ownership(
                    history=HistoryOwnership(
                        date=DateUpdate(update=datetime.datetime(2021, 12, 23, 17, 4, 29)),
                        count=5,
                        items=[
                            ItemHistory(
                                id=2749355478,
                                date=DateStartEnd(
                                    start=datetime.datetime(2017, 7, 29, 0, 0),
                                    end=datetime.datetime(2021, 12, 6, 0, 0),
                                ),
                                owner=OwnerHistory(type="PERSON", company=[]),
                                last_operation=LastOperation(
                                    code="07", description="Прекращение регистрации в том числе"
                                ),
                            ),
                            ItemHistory(
                                id=2223879070,
                                date=DateStartEnd(
                                    start=datetime.datetime(2015, 5, 29, 0, 0),
                                    end=datetime.datetime(2017, 7, 29, 0, 0),
                                ),
                                owner=OwnerHistory(type="PERSON", company=[]),
                                last_operation=LastOperation(
                                    code="03",
                                    description="Изменение собственника (владельца) в результате совершения сделки, вступления в наследство, слияние и разделение капитала у юридического лица, переход права по договору лизинга, судебные решения и др.",
                                ),
                            ),
                            ItemHistory(
                                id=1720030057,
                                date=DateStartEnd(
                                    start=datetime.datetime(2014, 3, 14, 0, 0),
                                    end=datetime.datetime(2015, 5, 29, 0, 0),
                                ),
                                owner=OwnerHistory(type="PERSON", company=[]),
                                last_operation=LastOperation(
                                    code="06",
                                    description="Выдача взамен утраченных или пришедших в негодность государственных регистрационных знаков, регистрационных документов, паспортов транспортных средств.",
                                ),
                            ),
                            ItemHistory(
                                id=438555087,
                                date=DateStartEnd(
                                    start=datetime.datetime(2012, 5, 3, 0, 0),
                                    end=datetime.datetime(2014, 3, 14, 0, 0),
                                ),
                                owner=OwnerHistory(type="PERSON", company=[]),
                                last_operation=LastOperation(
                                    code="06",
                                    description="Выдача взамен утраченных или пришедших в негодность государственных регистрационных знаков, регистрационных документов, паспортов транспортных средств.",
                                ),
                            ),
                            ItemHistory(
                                id=996667948,
                                date=DateStartEnd(
                                    start=datetime.datetime(2010, 9, 30, 0, 0),
                                    end=datetime.datetime(2012, 4, 6, 0, 0),
                                ),
                                owner=OwnerHistory(type="PERSON", company=[]),
                                last_operation=LastOperation(
                                    code="62",
                                    description="В связи с прекращением права собственности (отчуждение, конфискация ТС)",
                                ),
                            ),
                        ],
                        comment="История владения",
                    )
                ),
                stealings=Stealings(
                    count=0,
                    items=[],
                    comment="Проверка на угон",
                    date=DateUpdate(update=datetime.datetime(2021, 12, 23, 16, 56, 23)),
                    is_wanted=False,
                ),
                tech_data=TechData(
                    type=Type(
                        code="22",
                        name="Комби (хэтчбек)",
                        type_id="ID_BODY_TYPE_HATCHBACK",
                        comment="Тип (Вид) ТС",
                    ),
                    year=2010,
                    brand=Brand(
                        id="ID_MARK_KIA",
                        name=OriginalNormalizedName(original="Киа Серато", normalized="Kia"),
                        logotype=Logotype(uri="https://vl.imgix.net/img/kia-logo.png"),
                        comment="Марка",
                    ),
                    drive=Drive(
                        type="Заднеприводной",
                        type_id="ID_DRIVING_WHEELS_TYPE_REAR",
                        comment="Привод",
                    ),
                    model=Model(
                        id="ID_MARK_KIA_MODEL_CERATO",
                        name=OriginalNormalizedName(original="CERATO", normalized="Cerato"),
                        comment="Модель",
                    ),
                    wheel=Wheel(
                        comment="Рулевое колесо",
                        position="LEFT",
                        position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                        position_code="1",
                    ),
                    engine=Engine(
                        fuel=Fuel(type="Бензиновый", type_id="ID_ENGINE_TYPE_PETROL"),
                        power=Power(hp=126, kw=92),
                        number="242135",
                        volume=1591,
                        model=Name(name="G4F1"),
                        standarts=Standarts(emission=[]),
                        comment="Двигатель",
                    ),
                    weight=Weight(max=1720, netto=1293, comment="Масса"),
                    body=Body(
                        color=Color(name="Серый", type="Белый"), number=None, comment="Кузов"
                    ),
                    date=DateUpdate(update=datetime.datetime(2021, 12, 23, 17, 31, 55)),
                    chassis=Chassis(number=None, comment="Шасси"),
                    generations=[
                        Generations(
                            id=4645742,
                            name="II",
                            years=StartEnd(end=2013, start=2008),
                            bodies=[
                                Bodies(
                                    id=4645746,
                                    type="Седан",
                                    modifications=[
                                        BodiesModification(
                                            id=20028,
                                            name="Модификация 1.6 MT",
                                            drive=TypeA(type="ПЕРЕДНИЙ"),
                                            engine=Engine(
                                                fuel=Fuel(type="Бензиновый", type_id=None),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            transmission=TypeA(type="MANUAL"),
                                        ),
                                        BodiesModification(
                                            id=20027,
                                            name="Модификация 1.6 AT",
                                            drive=TypeA(type="ПЕРЕДНИЙ"),
                                            engine=Engine(
                                                fuel=Fuel(type="Бензиновый", type_id=None),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            transmission=TypeA(type="AUTOMATIC"),
                                        ),
                                    ],
                                ),
                                Bodies(
                                    id=21010997,
                                    type="Хэтчбек 5 дв.",
                                    modifications=[
                                        BodiesModification(
                                            id=21010992,
                                            name="Модификация 1.6 AT",
                                            drive=TypeA(type="ПЕРЕДНИЙ"),
                                            engine=Engine(
                                                fuel=Fuel(type="Бензиновый", type_id=None),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            transmission=TypeA(type="AUTOMATIC"),
                                        ),
                                        BodiesModification(
                                            id=21010993,
                                            name="Модификация 1.6 MT",
                                            drive=TypeA(type="ПЕРЕДНИЙ"),
                                            engine=Engine(
                                                fuel=Fuel(type="Бензиновый", type_id=None),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            transmission=TypeA(type="MANUAL"),
                                        ),
                                    ],
                                ),
                                Bodies(
                                    id=6233720,
                                    type="Купе",
                                    modifications=[
                                        BodiesModification(
                                            id=76892,
                                            name="Модификация 1.6 MT",
                                            drive=TypeA(type="ПЕРЕДНИЙ"),
                                            engine=Engine(
                                                fuel=Fuel(type="Бензиновый", type_id=None),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            transmission=TypeA(type="MANUAL"),
                                        ),
                                        BodiesModification(
                                            id=20034,
                                            name="Модификация 1.6 AT",
                                            drive=TypeA(type="ПЕРЕДНИЙ"),
                                            engine=Engine(
                                                fuel=Fuel(type="Бензиновый", type_id=None),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            transmission=TypeA(type="AUTOMATIC"),
                                        ),
                                    ],
                                ),
                            ],
                            is_restyling=False,
                        )
                    ],
                    manufacturer=[],
                    transmission=Transmission(comment="Трансмиссия"),
                    comment="Характеристики ТС",
                ),
                identifiers=Identifiers(
                    vehicle=Vehicle(
                        pts="16ОК330069",
                        sts="7852934229",
                        vin="KNAFU611BA5295980",
                        body=None,
                        chassis=None,
                        reg_num="Х893ЕК178",
                    ),
                    manufacture=[],
                    comment="Идентификаторы",
                ),
                arbitration=CountItems(
                    count=0,
                    items=[],
                    comment="Проверка судебных дел",
                    date=DateUpdate(update=datetime.datetime(2021, 12, 23, 16, 56, 25)),
                ),
                report_meta=[],
                pledges_nbki=CountItems(
                    count=0,
                    items=[],
                    comment="Обременения на ТС по данным НБКИ",
                    date=DateUpdate(update=None),
                ),
                utilizations=Utilizations(
                    count=0,
                    items=[],
                    comment="Утилизация",
                    date=DateUpdate(update=datetime.datetime(2021, 12, 23, 17, 4, 29)),
                    was_utilized=False,
                ),
                gots_auctions=GotsAuctions(
                    items=[], comment="Размещение ТС на аукционах ГОТС", date=[]
                ),
                fines=Fines(
                    date=DateUpdate(update=datetime.datetime(2021, 12, 23, 16, 56, 25)),
                    count=19,
                    items=[
                        FinesItems(
                            id=210252627,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2021, 7, 8, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811601121010001140",
                                bank=Bank(
                                    bik="016126031",
                                    name="ОТДЕЛЕНИЕ РЯЗАНЬ БАНКА РОССИИ//УФК по Рязанской области г. Рязань",
                                    account=Number(number=3100643000000015900),
                                ),
                                user=User(
                                    kpp="623401001",
                                    tin="6231006522",
                                    name="УФК по Рязанской области (УМВД России по Рязанской области)(УМВД России по Рязанской области)",
                                ),
                                okato=61701000,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810162210739014395"
                                ),
                            ),
                            amount=Total(total=1000),
                            photos=[],
                            vendor=Name(
                                name="УФК по Рязанской области (УМВД России по Рязанской области)(ЦАФАП ГИБДД УМВД России по Рязанской области)"
                            ),
                            article=Article(
                                code="12.9ч.3",
                                description="Превышение установленной скорости движения транспортного средства на величину более 40, но не более 60 километров в час",
                            ),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2021, 7, 28, 0, 0)), percent=50
                            ),
                            location=Location(
                                raw="РЯЗАНСКАЯ ОБЛ. РЯЗАНСКАЯ ОБЛАСТЬ, СПАССКИЙ РАЙОН, 248КМ 442М А Д М5 УРАЛ"
                            ),
                            description="УИН 18810162210739014395 от 2021-07-08 на 1,000.00 руб.",
                            need_payment=False,
                            uin="18810162210739014395",
                        ),
                        FinesItems(
                            id=4243141361,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2021, 5, 28, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811601121010001140",
                                bank=Bank(
                                    bik="014030106",
                                    name="в Северо-Западном главном управлении Центрального Банка Российской Федерации (Северо-Западное ГУ Банка России//УФК по г.Санкт-Петербургу г.Санкт-Петербург)",
                                    account=Number(number=3100643000000017200),
                                ),
                                user=User(
                                    kpp="781345001",
                                    tin="7830002600",
                                    name="УФК по г.Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)",
                                ),
                                okato=40394000,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810178210528132134"
                                ),
                            ),
                            amount=Total(total=500),
                            photos=[],
                            vendor=Name(
                                name="УФК по г.Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО)"
                            ),
                            article=Article(
                                code="12.9ч.2",
                                description="Превышение установленной скорости движения транспортного средства на величину более 20, но не более 40 километров в час",
                            ),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2021, 6, 17, 0, 0)), percent=50
                            ),
                            location=Location(
                                raw="Г. СПБ, ВИТЕБСКИЙ ПР. 107-А, ОТ ДУНАЙСКОГО ПР. К КАД, 2-Я ПРАВАЯ ПОЛОСА"
                            ),
                            description="УИН 18810178210528132134 от 2021-05-28 на 500.00 руб.",
                            need_payment=False,
                            uin="18810178210528132134",
                        ),
                        FinesItems(
                            id=843963400,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2021, 3, 12, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="86811602010020300140",
                                bank=Bank(
                                    bik="014030106",
                                    name="СЕВЕРО-ЗАПАДНОЕ ГУ БАНКА РОССИИ//УФК по г.Санкт-Петербургу г Санкт-Петербург",
                                    account=Number(number=3100643000000017200),
                                ),
                                user=User(
                                    kpp="784101001",
                                    tin="7830001853",
                                    name="УФК по г. Санкт-Петербургу(КОМИТЕТ ПО РАЗВИТИЮ ТРАНСПОРТНОЙ ИНФРАСТРУКТУРЫ САНКТ-ПЕТЕРБУРГА)",
                                ),
                                okato=40908000,
                                payment=Payment(
                                    purpose="Штраф за неоплаченную парковочную сессию. Постановление № 0314821370000000001321886 Место нарушения: СПб, ул. Жуковского (широта:59.93593183,долгота:30.35774817) Дата нарушения:04.03.2021 15:31-16:21"
                                ),
                            ),
                            amount=Total(total=3000),
                            photos=[],
                            vendor=Name(
                                name="КОМИТЕТ ПО РАЗВИТИЮ ТРАНСПОРТНОЙ ИНФРАСТРУКТУРЫ САНКТ-ПЕТЕРБУРГА"
                            ),
                            article=Article(code=None, description=None),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2021, 4, 1, 0, 0)), percent=50
                            ),
                            location=Location(raw=None),
                            description="УИН 0314821370000000001321886 от 2021-03-12 на 3,000.00 руб.",
                            need_payment=False,
                            uin="0314821370000000001321886",
                        ),
                        FinesItems(
                            id=751256555,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2020, 5, 2, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811601121010001140",
                                bank=Bank(
                                    bik="044030001",
                                    name="в Северо-Западном главном управлении Центрального Банка Российской Федерации (Северо-Западное ГУ Банка России)",
                                    account=Number(number=40101810200000010001),
                                ),
                                user=User(
                                    kpp="781345001",
                                    tin="7830002600",
                                    name="УФК по г.Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)",
                                ),
                                okato=40394000,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810178200502156411"
                                ),
                            ),
                            amount=Total(total=500),
                            photos=[],
                            vendor=Name(
                                name="УФК по г.Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО)"
                            ),
                            article=Article(
                                code="12.9ч.2",
                                description="Превышение установленной скорости движения транспортного средства на величину более 20, но не более 40 километров в час",
                            ),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2020, 5, 22, 0, 0)), percent=50
                            ),
                            location=Location(
                                raw="Г. СПБ, ПУЛКОВСКОЕ Ш., НАПРОТИВ Д.60 К.1-М, ОТ КАД К ПЕТЕРБУРГСКОМУ Ш."
                            ),
                            description="УИН 18810178200502156411 от 2020-05-02 на 500.00 руб.",
                            need_payment=False,
                            uin="18810178200502156411",
                        ),
                        FinesItems(
                            id=1841916872,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2019, 9, 26, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811630020016000140",
                                bank=Bank(
                                    bik="044030001",
                                    name="в Северо-Западном главном управлении Центрального Банка Российской Федерации (Северо-Западное ГУ Банка России)",
                                    account=Number(number=40101810200000010001),
                                ),
                                user=User(
                                    kpp="781345001",
                                    tin="7830002600",
                                    name="УФК по г.Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО)",
                                ),
                                okato=40394000,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810178190926144412"
                                ),
                            ),
                            amount=Total(total=500),
                            photos=[],
                            vendor=Name(name="ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО"),
                            article=Article(
                                code="12.9Ч.2",
                                description="Превышение установленной скорости движения транспортного средства на величину более 20, но не более 40 километров в час",
                            ),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2019, 10, 16, 0, 0)), percent=50
                            ),
                            location=Location(
                                raw="Г. СПБ, МИТРОФАНЬЕВСКОЕ Ш., Д.29-В, ОТ КУБИНСКОЙ УЛ. К М. МИТРОФАНЬЕВСКОЙ УЛ."
                            ),
                            description="УИН 18810178190926144412 от 2019-09-26 на 500.00 руб.",
                            need_payment=False,
                            uin="18810178190926144412",
                        ),
                        FinesItems(
                            id=679948100,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2019, 9, 3, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811630020016000140",
                                bank=Bank(
                                    bik="044030001",
                                    name="в Северо-Западном главном управлении Центрального Банка Российской Федерации (Северо-Западное ГУ Банка России)",
                                    account=Number(number=40101810200000010001),
                                ),
                                user=User(
                                    kpp="781345001",
                                    tin="7830002600",
                                    name="УФК по г.Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО)",
                                ),
                                okato=40394000,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810178190903152613"
                                ),
                            ),
                            amount=Total(total=500),
                            photos=[],
                            vendor=Name(name="ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО"),
                            article=Article(
                                code="12.9Ч.2",
                                description="Превышение установленной скорости движения транспортного средства на величину более 20, но не более 40 километров в час",
                            ),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2019, 9, 23, 0, 0)), percent=50
                            ),
                            location=Location(
                                raw="Г. СПБ, НАБ. ОБВОДНОГО КАНАЛА, ВЪЕЗД ПОД НОВО-МОСКОВСКИЙ МОСТ, К ПР. ИЗМАЙЛОВСКИЙ, КРАЙНЯЯ ЛЕВАЯ ПОЛОСА"
                            ),
                            description="УИН 18810178190903152613 от 2019-09-03 на 500.00 руб.",
                            need_payment=False,
                            uin="18810178190903152613",
                        ),
                        FinesItems(
                            id=3155877620,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2019, 3, 21, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811630020016000140",
                                bank=Bank(
                                    bik="044030001",
                                    name="в Северо-Западном главном управлении Центрального Банка Российской Федерации (Северо-Западное ГУ Банка России)",
                                    account=Number(number=40101810200000010001),
                                ),
                                user=User(
                                    kpp="781345001",
                                    tin="7830002600",
                                    name="УФК по г.Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО)",
                                ),
                                okato=40394000,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810178190321032216"
                                ),
                            ),
                            amount=Total(total=500),
                            photos=[],
                            vendor=Name(name="ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО"),
                            article=Article(
                                code="12.9Ч.2",
                                description="Превышение установленной скорости движения транспортного средства на величину более 20, но не более 40 километров в час",
                            ),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2019, 4, 10, 0, 0)), percent=50
                            ),
                            location=Location(raw=None),
                            description="УИН 18810178190321032216 от 2019-03-21 на 500.00 руб.",
                            need_payment=False,
                            uin="18810178190321032216",
                        ),
                        FinesItems(
                            id=2883021250,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2018, 10, 25, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811630020016000140",
                                bank=Bank(
                                    bik="044030001",
                                    name="в Северо-Западном главном управлении Центрального Банка Российской Федерации (Северо-Западное ГУ Банка России)",
                                    account=Number(number=40101810200000010001),
                                ),
                                user=User(
                                    kpp="781345001",
                                    tin="7830002600",
                                    name="УФК по г.Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО)",
                                ),
                                okato=40394000,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810178181025002520"
                                ),
                            ),
                            amount=Total(total=500),
                            photos=[],
                            vendor=Name(name="ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО"),
                            article=Article(
                                code="12.9Ч.2",
                                description="Превышение установленной скорости движения транспортного средства на величину более 20, но не более 40 километров в час",
                            ),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2018, 11, 14, 0, 0)), percent=50
                            ),
                            location=Location(raw=None),
                            description="УИН 18810178181025002520 от 2018-10-25 на 500.00 руб.",
                            need_payment=False,
                            uin="18810178181025002520",
                        ),
                        FinesItems(
                            id=3175473796,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2018, 9, 27, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811630020016000140",
                                bank=Bank(
                                    bik="044030001",
                                    name="в Северо-Западном главном управлении Центрального Банка Российской Федерации (Северо-Западное ГУ Банка России)",
                                    account=Number(number=40101810200000010001),
                                ),
                                user=User(
                                    kpp="781345001",
                                    tin="7830002600",
                                    name="УФК по г.Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО)",
                                ),
                                okato=40394000,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810178180927028948"
                                ),
                            ),
                            amount=Total(total=500),
                            photos=[],
                            vendor=Name(name="ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО"),
                            article=Article(
                                code="12.9Ч.2",
                                description="Превышение установленной скорости движения транспортного средства на величину более 20, но не более 40 километров в час",
                            ),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2018, 10, 17, 0, 0)), percent=50
                            ),
                            location=Location(raw=None),
                            description="УИН 18810178180927028948 от 2018-09-27 на 500.00 руб.",
                            need_payment=False,
                            uin="18810178180927028948",
                        ),
                        FinesItems(
                            id=53334515,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2018, 9, 24, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811630020016000140",
                                bank=Bank(
                                    bik="044030001",
                                    name="в Северо-Западном главном управлении Центрального Банка Российской Федерации (Северо-Западное ГУ Банка России)",
                                    account=Number(number=40101810200000010001),
                                ),
                                user=User(
                                    kpp="781345001",
                                    tin="7830002600",
                                    name="УФК по г.Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО)",
                                ),
                                okato=40394000,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810178180924146826"
                                ),
                            ),
                            amount=Total(total=1000),
                            photos=[],
                            vendor=Name(name="ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО"),
                            article=Article(
                                code="12.9Ч.3",
                                description="Превышение установленной скорости движения транспортного средства на величину более 40, но не более 60 километров в час",
                            ),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2018, 10, 14, 0, 0)), percent=50
                            ),
                            location=Location(raw=None),
                            description="УИН 18810178180924146826 от 2018-09-24 на 1,000.00 руб.",
                            need_payment=False,
                            uin="18810178180924146826",
                        ),
                        FinesItems(
                            id=3218931974,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2018, 8, 22, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811630020016000140",
                                bank=Bank(
                                    bik="044030001",
                                    name="в Северо-Западном главном управлении Центрального Банка Российской Федерации (Северо-Западное ГУ Банка России)",
                                    account=Number(number=40101810200000010001),
                                ),
                                user=User(
                                    kpp="781345001",
                                    tin="7830002600",
                                    name="УФК по г.Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО)",
                                ),
                                okato=40394000,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810178180822136570"
                                ),
                            ),
                            amount=Total(total=500),
                            photos=[],
                            vendor=Name(name="ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО"),
                            article=Article(
                                code="12.9Ч.2",
                                description="Превышение установленной скорости движения транспортного средства на величину более 20, но не более 40 километров в час",
                            ),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2018, 9, 11, 0, 0)), percent=50
                            ),
                            location=Location(raw=None),
                            description="УИН 18810178180822136570 от 2018-08-22 на 500.00 руб.",
                            need_payment=False,
                            uin="18810178180822136570",
                        ),
                        FinesItems(
                            id=3210430484,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2018, 8, 16, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811630020016000140",
                                bank=Bank(
                                    bik="044030001",
                                    name="в Северо-Западном главном управлении Центрального Банка Российской Федерации (Северо-Западное ГУ Банка России)",
                                    account=Number(number=40101810200000010001),
                                ),
                                user=User(
                                    kpp="781345001",
                                    tin="7830002600",
                                    name="УФК по г.Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО)",
                                ),
                                okato=40394000,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810178180816055343"
                                ),
                            ),
                            amount=Total(total=500),
                            photos=[],
                            vendor=Name(name="ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО"),
                            article=Article(
                                code="12.9Ч.2",
                                description="Превышение установленной скорости движения транспортного средства на величину более 20, но не более 40 километров в час",
                            ),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2018, 9, 5, 0, 0)), percent=50
                            ),
                            location=Location(raw=None),
                            description="УИН 18810178180816055343 от 2018-08-16 на 500.00 руб.",
                            need_payment=False,
                            uin="18810178180816055343",
                        ),
                        FinesItems(
                            id=78970801,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2018, 8, 15, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811630020016000140",
                                bank=Bank(
                                    bik="044030001",
                                    name="в Северо-Западном главном управлении Центрального Банка Российской Федерации (Северо-Западное ГУ Банка России)",
                                    account=Number(number=40101810200000010001),
                                ),
                                user=User(
                                    kpp="781345001",
                                    tin="7830002600",
                                    name="УФК по г.Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО)",
                                ),
                                okato=40394000,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810178180815195192"
                                ),
                            ),
                            amount=Total(total=500),
                            photos=[],
                            vendor=Name(name="ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО"),
                            article=Article(
                                code="12.9Ч.2",
                                description="Превышение установленной скорости движения транспортного средства на величину более 20, но не более 40 километров в час",
                            ),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2018, 9, 4, 0, 0)), percent=50
                            ),
                            location=Location(raw=None),
                            description="УИН 18810178180815195192 от 2018-08-15 на 500.00 руб.",
                            need_payment=False,
                            uin="18810178180815195192",
                        ),
                        FinesItems(
                            id=2175223234,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2018, 8, 13, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811630020016000140",
                                bank=Bank(
                                    bik="044106001",
                                    name="в Отделение по Ленинградской области Северо-Западного главного управления Центрального банка Российской Федерации (Отделение Ленинградское)",
                                    account=Number(number=40101810200000010022),
                                ),
                                user=User(
                                    kpp="781345001",
                                    tin="7830002600",
                                    name="УФК по Ленинградской области (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ЦАФАП в ОДД ГИБДД ГУ МВД России по Ленинградской области)",
                                ),
                                okato=41612101,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810147180813044026"
                                ),
                            ),
                            amount=Total(total=500),
                            photos=[],
                            vendor=Name(
                                name="ЦАФАП в ОДД ГИБДД ГУ МВД России по Ленинградской области"
                            ),
                            article=Article(
                                code="12.9Ч.2",
                                description="Превышение установленной скорости движения транспортного средства на величину более 20, но не более 40 километров в час",
                            ),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2018, 9, 2, 0, 0)), percent=50
                            ),
                            location=Location(raw=None),
                            description="УИН 18810147180813044026 от 2018-08-13 на 500.00 руб.",
                            need_payment=False,
                            uin="18810147180813044026",
                        ),
                        FinesItems(
                            id=1103367429,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2018, 5, 17, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811630020016000140",
                                bank=Bank(
                                    bik="044525000",
                                    name="ГУ Банка России по ЦФО",
                                    account=Number(number=40101810845250010102),
                                ),
                                user=User(
                                    kpp="770245001",
                                    tin="7703037039",
                                    name="УФК по МО (УГИБДД ГУ МВД России по Московской области)(Центр видеофиксации ГИБДД ГУ МВД России по Московской области)",
                                ),
                                okato=46641152,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810150180517187190"
                                ),
                            ),
                            amount=Total(total=500),
                            photos=[],
                            vendor=Name(
                                name="Центр видеофиксации ГИБДД ГУ МВД России по Московской области"
                            ),
                            article=Article(code=None, description=None),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2018, 6, 6, 0, 0)), percent=50
                            ),
                            location=Location(raw=None),
                            description="УИН 18810150180517187190 от 2018-05-17 на 500.00 руб.",
                            need_payment=False,
                            uin="18810150180517187190",
                        ),
                        FinesItems(
                            id=3881878817,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2018, 5, 10, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811630020016000140",
                                bank=Bank(
                                    bik="044030001",
                                    name="в Северо-Западном главном управлении Центрального Банка Российской Федерации (Северо-Западное ГУ Банка России)",
                                    account=Number(number=40101810200000010001),
                                ),
                                user=User(
                                    kpp="781345001",
                                    tin="7830002600",
                                    name="УФК по г.Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО)",
                                ),
                                okato=40394000,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810178180510023746"
                                ),
                            ),
                            amount=Total(total=1000),
                            photos=[],
                            vendor=Name(name="ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО"),
                            article=Article(code=None, description=None),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2018, 5, 30, 0, 0)), percent=50
                            ),
                            location=Location(raw=None),
                            description="УИН 18810178180510023746 от 2018-05-10 на 1,000.00 руб.",
                            need_payment=False,
                            uin="18810178180510023746",
                        ),
                        FinesItems(
                            id=3961867218,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2018, 4, 26, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811630020016000140",
                                bank=Bank(
                                    bik="044030001",
                                    name="в Северо-Западном главном управлении Центрального Банка Российской Федерации (Северо-Западное ГУ Банка России)",
                                    account=Number(number=40101810200000010001),
                                ),
                                user=User(
                                    kpp="781345001",
                                    tin="7830002600",
                                    name="УФК по г.Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО)",
                                ),
                                okato=40394000,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810178180426125991"
                                ),
                            ),
                            amount=Total(total=500),
                            photos=[],
                            vendor=Name(name="ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО"),
                            article=Article(code=None, description=None),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2018, 5, 16, 0, 0)), percent=50
                            ),
                            location=Location(raw=None),
                            description="УИН 18810178180426125991 от 2018-04-26 на 500.00 руб.",
                            need_payment=False,
                            uin="18810178180426125991",
                        ),
                        FinesItems(
                            id=519480539,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2018, 1, 25, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811630020016000140",
                                bank=Bank(
                                    bik="044030001",
                                    name="в Северо-Западном главном управлении Центрального Банка Российской Федерации (Северо-Западное ГУ Банка России)",
                                    account=Number(number=40101810200000010001),
                                ),
                                user=User(
                                    kpp="781345001",
                                    tin="7830002600",
                                    name="УФК по г.Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО)",
                                ),
                                okato=40394000,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810178180125011024"
                                ),
                            ),
                            amount=Total(total=2000),
                            photos=[],
                            vendor=Name(name="ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО"),
                            article=Article(code=None, description=None),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2018, 2, 14, 0, 0)), percent=50
                            ),
                            location=Location(raw=None),
                            description="УИН 18810178180125011024 от 2018-01-25 на 2,000.00 руб.",
                            need_payment=False,
                            uin="18810178180125011024",
                        ),
                        FinesItems(
                            id=1704194028,
                            uid=None,
                            date=DateEvent(event=datetime.datetime(2018, 1, 15, 0, 0)),
                            fssp=Fssp(is_proceed=False),
                            wire=Wire(
                                kbk="18811630020016000140",
                                bank=Bank(
                                    bik="044030001",
                                    name="в Северо-Западном главном управлении Центрального Банка Российской Федерации (Северо-Западное ГУ Банка России)",
                                    account=Number(number=40101810200000010001),
                                ),
                                user=User(
                                    kpp="781345001",
                                    tin="7830002600",
                                    name="УФК по г.Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)(ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО)",
                                ),
                                okato=40394000,
                                payment=Payment(
                                    purpose="ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810178180115088814"
                                ),
                            ),
                            amount=Total(total=500),
                            photos=[],
                            vendor=Name(name="ЦАФАП в ОДД ГИБДД ГУ МВД России по г.СПб и ЛО"),
                            article=Article(code=None, description=None),
                            is_paid=True,
                            discount=DateEndPercent(
                                date=DateEnd(end=datetime.datetime(2018, 2, 4, 0, 0)), percent=50
                            ),
                            location=Location(raw=None),
                            description="УИН 18810178180115088814 от 2018-01-15 на 500.00 руб.",
                            need_payment=False,
                            uin="18810178180115088814",
                        ),
                    ],
                    has_fines=True,
                    comment="Штрафы",
                ),
                commercial_use=CountItems(
                    count=0,
                    items=[],
                    comment="Коммерческое использование ТС",
                    date=DateUpdate(update=None),
                ),
                additional_info=AdditionalInfo(
                    vehicle=VehicleInfo(
                        notes=[
                            "29.07.2017 ИЗМ. ВЛАДЕЛЬЦА ПО ДКП № БЕЗ НОМЕРА ОТ 21.06.2017 .МРЭО ГИБДДЭК. КЛАСС ТРЕТИЙ",
                            "1632204986,93",
                        ],
                        owner=OwnerInfo(
                            geo=GeoOwner(city=None, region="Санкт-Петербург Г."),
                            type="PERSON",
                            enforcement_proceedings={"has_proceedings": True},
                        ),
                        segment=Segment(euro=[]),
                        category=Category(
                            code="B",
                            description="Легковые автомобили, небольшие грузовики (до 3,5 тонн)",
                        ),
                        exported=False,
                        passport=Passport(
                            org=Name(name="Мрэо Гибдд Омвд По Альметьевскому Р-Ну"),
                            date=DatePassport(receive="2015-05-29 00:00:00"),
                            number="16ОК330069",
                            has_dublicate=True,
                        ),
                        modifications=Modifications(was_modificated=False),
                        sts={"date": {"receive": "2017-07-29 00:00:00"}},
                    ),
                    identifiers=IdentifiersInfo(vin=[]),
                    comment="Дополнительная информация",
                    catalog={
                        "rsa": {"items": []},
                        "oats": {"items": []},
                        "tecdoc": {"items": []},
                        "transdekra": {"items": []},
                    },
                ),
                service_history=CountItems(
                    count=0,
                    items=[],
                    comment="История дилерского обслуживания",
                    date=DateUpdate(update=datetime.datetime(2021, 12, 23, 16, 56, 23)),
                ),
                diagnostic_cards=CountItems(
                    count=0,
                    items=[],
                    comment="Диагностические карты",
                    date=DateUpdate(update=datetime.datetime(2021, 12, 23, 16, 56, 23)),
                ),
                recall_campaigns=CountItems(
                    count=0,
                    items=[],
                    comment="Отзывные кампании",
                    date=DateUpdate(update=datetime.datetime(2021, 12, 23, 16, 56, 23)),
                ),
                identifiers_masked=Identifiers(
                    vehicle=Vehicle(
                        pts="16О*****69",
                        sts="785*****29",
                        vin="KNAF************0",
                        body=None,
                        chassis=None,
                        reg_num="Х8*****78",
                    ),
                    manufacture=[],
                    comment="Маскированные идентификаторы",
                ),
                images=Images(
                    photos=Photos(
                        date=DateUpdate(update=datetime.datetime(2021, 12, 23, 16, 30, 36)),
                        count=9,
                        items=[
                            PhotosItem(
                                id=3997940607,
                                uri="https://ng-images.avtocod.ru/images/2021/10/06/7bd71580f79043023dea5473cc0cc22e.jpg",
                                date=Issued(issued=datetime.datetime(2021, 6, 18, 0, 0)),
                                vehicle=PhotoItemVehicle(brand=[], model=[]),
                            ),
                            PhotosItem(
                                id=1185887527,
                                uri="https://ng-images.avtocod.ru/images/2021/10/06/98d6c36ed82f97380519b9b128bc2c52.jpg",
                                date=Issued(issued=datetime.datetime(2021, 6, 18, 0, 0)),
                                vehicle=PhotoItemVehicle(brand=[], model=[]),
                            ),
                            PhotosItem(
                                id=2831038496,
                                uri="https://ng-images.avtocod.ru/images/2021/10/06/798f2df61102f34af0223da914a4664f.jpg",
                                date=Issued(issued=datetime.datetime(2021, 6, 18, 0, 0)),
                                vehicle=PhotoItemVehicle(brand=[], model=[]),
                            ),
                            PhotosItem(
                                id=493853533,
                                uri="https://ng-images.avtocod.ru/images/2021/10/06/b8c6a00f7aa1c18a60f44aab36188c06.jpg",
                                date=Issued(issued=datetime.datetime(2021, 6, 18, 0, 0)),
                                vehicle=PhotoItemVehicle(brand=[], model=[]),
                            ),
                            PhotosItem(
                                id=783644967,
                                uri="https://ng-images.avtocod.ru/images/2021/06/09/5533f41b30327998c81da33b74fa1952.jpg",
                                date=Issued(issued=datetime.datetime(2019, 1, 24, 0, 0)),
                                vehicle=PhotoItemVehicle(brand=[], model=[]),
                            ),
                            PhotosItem(
                                id=2221481686,
                                uri="https://ng-images.avtocod.ru/images/2021/06/09/c5392fb2964b69285623cd5b3f0a5134.jpg",
                                date=Issued(issued=datetime.datetime(2018, 5, 19, 0, 0)),
                                vehicle=PhotoItemVehicle(brand=[], model=[]),
                            ),
                            PhotosItem(
                                id=3436757783,
                                uri="https://ng-images.avtocod.ru/images/2021/06/09/6376bfba480b147fa7b86b4180007c48.jpg",
                                date=Issued(issued=datetime.datetime(2017, 11, 5, 0, 0)),
                                vehicle=PhotoItemVehicle(brand=[], model=[]),
                            ),
                            PhotosItem(
                                id=1552672650,
                                uri="https://ng-images.avtocod.ru/images/2021/06/09/518c7298f9105280c313b2dd5bc3d6c9.jpg",
                                date=Issued(issued=datetime.datetime(2012, 5, 22, 0, 0)),
                                vehicle=PhotoItemVehicle(brand=[], model=[]),
                            ),
                            PhotosItem(
                                id=2933977984,
                                uri="https://ng-images.avtocod.ru/images/2021/06/09/aaa6f51515b328416b13f03a20de9ee3.jpg",
                                date=Issued(issued=datetime.datetime(2012, 5, 22, 0, 0)),
                                vehicle=PhotoItemVehicle(brand=[], model=[]),
                            ),
                        ],
                        comment="Фотографии ТС",
                    ),
                    comment="Изображения, связанные с ТС",
                ),
                market_prices=MarketPrices(
                    date=None,
                    items=None,
                    comment="Рыночная стоимость ТС",
                    ads=Ads(
                        date=DateUpdate(update=datetime.datetime(2021, 12, 23, 17, 31, 55)),
                        items=[
                            AdsItem(
                                id=480189671,
                                amount=MaxMin(max=748392, min=447277, optimal=597835),
                                mileage=166000,
                                currency=TypeA(type="RUB"),
                                metadata=Metadata(
                                    comment=None,
                                    application=None,
                                    functions=[
                                        {
                                            "name": "price_mileage",
                                            "parts": [
                                                {
                                                    "type": "STRAIGHT_LINE",
                                                    "bounds": {
                                                        "left": 0,
                                                        "right": 1181837.3811312753,
                                                    },
                                                    "description": "y = coefficients[0] + x * coefficients[1]",
                                                    "coefficients": [693078, -0.5737489868114782],
                                                },
                                                {
                                                    "type": "STRAIGHT_LINE",
                                                    "bounds": {"left": 1181837.3811312753},
                                                    "description": "y = coefficients[0] + x * coefficients[1]",
                                                    "coefficients": [15000, 0],
                                                },
                                            ],
                                            "description": "y = price, x = mileage",
                                        }
                                    ],
                                ),
                                related_ads=[
                                    RelatedAd(
                                        geo=GeoAd(
                                            city="Ростовская область, Каменоломни",
                                            street="Ростовская область, Октябрьский р-н, Каменоломненское городское поселение, рабочий пос. Каменоломни, ул. Энгельса",
                                            country="Россия",
                                        ),
                                        uri="https://www.avito.ru/kamenolomni/avtomobili/kia_cerato_2010_2300885498",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 12, 23, 8, 36, 47)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=665000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=3),
                                            condition="Не битый",
                                            transmission=TypeAndTypeId(
                                                type="AUTOMATIC",
                                                type_id="ID_TRANSMISSION_TYPE_AUTOMATIC",
                                            ),
                                            mileage=136243,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(
                                            city="Алтайский край, Лебяжье",
                                            street="Алтайский край, муниципальное образование Барнаул, пос. Центральный, ул. Мира, 24",
                                            country="Россия",
                                        ),
                                        uri="https://www.avito.ru/altayskiy_kray_lebyazhe/avtomobili/kia_cerato_2010_2286617065",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 12, 22, 13, 8, 13)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=620000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=3),
                                            condition="Не битый",
                                            transmission=TypeAndTypeId(
                                                type="AUTOMATIC",
                                                type_id="ID_TRANSMISSION_TYPE_AUTOMATIC",
                                            ),
                                            mileage=250000,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(
                                            city="Первоуральск, Свердловская область",
                                            street=None,
                                            country="Россия",
                                        ),
                                        uri="https://pervouralsk.drom.ru/kia/cerato/45340756.html",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 12, 22, 0, 0)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=720000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=[],
                                            condition=None,
                                            transmission=TypeAndTypeId(
                                                type="UNKNOWN",
                                                type_id="ID_TRANSMISSION_TYPE_OTHER",
                                            ),
                                            mileage=154000,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(
                                            city="Первоуральск", street=None, country="Россия"
                                        ),
                                        uri="https://auto.ru/cars/used/sale/kia/cerato/1106374665-dcdbb23d/",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 12, 21, 18, 39, 11)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=810000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=3),
                                            condition="Не требует ремонта",
                                            transmission=TypeAndTypeId(
                                                type="AUTOMATIC",
                                                type_id="ID_TRANSMISSION_TYPE_AUTOMATIC",
                                            ),
                                            mileage=173000,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(
                                            city="Московская область, Звенигород",
                                            street="Московская область, Одинцовский г.о., Звенигород, жилой комплекс Лермонтовский",
                                            country="Россия",
                                        ),
                                        uri="https://www.avito.ru/zvenigorod/avtomobili/kia_cerato_2010_2297549474",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 12, 21, 8, 31, 40)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=650000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=2),
                                            condition="Не битый",
                                            transmission=TypeAndTypeId(
                                                type="MANUAL",
                                                type_id="ID_TRANSMISSION_TYPE_MANUAL",
                                            ),
                                            mileage=158000,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(
                                            city="Симферополь", street=None, country="Россия"
                                        ),
                                        uri="https://simferopol.drom.ru/kia/cerato/45310047.html",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 12, 20, 0, 0)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=635000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=[],
                                            condition=None,
                                            transmission=TypeAndTypeId(
                                                type="MANUAL",
                                                type_id="ID_TRANSMISSION_TYPE_MANUAL",
                                            ),
                                            mileage=161892,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(
                                            city="Нижневартовск, Ханты-Мансийский автономный округ",
                                            street=None,
                                            country="Россия",
                                        ),
                                        uri="https://nizhnevartovsk.drom.ru/kia/cerato/45289229.html",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 12, 18, 0, 0)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=500000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=2),
                                            condition=None,
                                            transmission=TypeAndTypeId(
                                                type="MANUAL",
                                                type_id="ID_TRANSMISSION_TYPE_MANUAL",
                                            ),
                                            mileage=128514,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(
                                            city="Краснодарский край, Краснодар",
                                            street="Краснодарский край, Краснодар, ул. Стасова, 178",
                                            country="Россия",
                                        ),
                                        uri="https://www.avito.ru/krasnodar/avtomobili/kia_cerato_2010_2278101333",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 12, 15, 8, 52, 35)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=670000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=4),
                                            condition="Не битый",
                                            transmission=TypeAndTypeId(
                                                type="AUTOMATIC",
                                                type_id="ID_TRANSMISSION_TYPE_AUTOMATIC",
                                            ),
                                            mileage=185000,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(
                                            city="Самарская область, Тольятти",
                                            street="Самарская область, Тольятти, ул. Горького, 43",
                                            country="Россия",
                                        ),
                                        uri="https://www.avito.ru/tolyatti/avtomobili/kia_cerato_2010_2282975088",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 12, 14, 3, 47, 35)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=570000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=3),
                                            condition="Не битый",
                                            transmission=TypeAndTypeId(
                                                type="AUTOMATIC",
                                                type_id="ID_TRANSMISSION_TYPE_AUTOMATIC",
                                            ),
                                            mileage=300000,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(city="Москва", street=None, country="Россия"),
                                        uri="https://moscow.drom.ru/kia/cerato/45236216.html",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 12, 14, 0, 0)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=729000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=1),
                                            condition=None,
                                            transmission=TypeAndTypeId(
                                                type="UNKNOWN",
                                                type_id="ID_TRANSMISSION_TYPE_OTHER",
                                            ),
                                            mileage=105218,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(
                                            city="Омская область, Омск",
                                            street="Омская область, Омск, Волгоградская ул., 44",
                                            country="Россия",
                                        ),
                                        uri="https://www.avito.ru/omsk/avtomobili/kia_cerato_2010_2295875534",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 12, 9, 23, 54, 35)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=615000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=4),
                                            condition="Не битый",
                                            transmission=TypeAndTypeId(
                                                type="AUTOMATIC",
                                                type_id="ID_TRANSMISSION_TYPE_AUTOMATIC",
                                            ),
                                            mileage=178200,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(city="Краснодар", street=None, country="Россия"),
                                        uri="https://krasnodar.drom.ru/kia/cerato/45155085.html",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 12, 7, 0, 0)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=775000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=1),
                                            condition=None,
                                            transmission=TypeAndTypeId(
                                                type="MANUAL",
                                                type_id="ID_TRANSMISSION_TYPE_MANUAL",
                                            ),
                                            mileage=63000,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(city="Волгоград", street=None, country="Россия"),
                                        uri="https://volgograd.drom.ru/kia/cerato/45140346.html",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 12, 6, 0, 0)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=600000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=1),
                                            condition=None,
                                            transmission=TypeAndTypeId(
                                                type="MANUAL",
                                                type_id="ID_TRANSMISSION_TYPE_MANUAL",
                                            ),
                                            mileage=233000,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(
                                            city="Татарстан, Казань",
                                            street="Республика Татарстан, Пестречинский р-н, Богородское сельское поселение, д. Куюки, 3-й квартал, 5",
                                            country="Россия",
                                        ),
                                        uri="https://www.avito.ru/kazan/avtomobili/kia_cerato_2010_2296452555",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 12, 4, 19, 42, 6)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=520000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=2),
                                            condition="Не битый",
                                            transmission=TypeAndTypeId(
                                                type="MANUAL",
                                                type_id="ID_TRANSMISSION_TYPE_MANUAL",
                                            ),
                                            mileage=209000,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(
                                            city="Брянская область, Брянск",
                                            street="Брянская область, Брянск, ул. Чкалова, 3",
                                            country="Россия",
                                        ),
                                        uri="https://www.avito.ru/bryansk/avtomobili/kia_cerato_2010_2263051944",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 12, 3, 9, 36, 10)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=630000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=3),
                                            condition="Не битый",
                                            transmission=TypeAndTypeId(
                                                type="AUTOMATIC",
                                                type_id="ID_TRANSMISSION_TYPE_AUTOMATIC",
                                            ),
                                            mileage=140000,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(
                                            city="Башкортостан, Уфа",
                                            street="Республика Башкортостан, Уфа, Рубежная ул., 168",
                                            country="Россия",
                                        ),
                                        uri="https://www.avito.ru/ufa/avtomobili/kia_cerato_2010_2285107159",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 12, 1, 6, 42, 45)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=589000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=4),
                                            condition="Не битый",
                                            transmission=TypeAndTypeId(
                                                type="MANUAL",
                                                type_id="ID_TRANSMISSION_TYPE_MANUAL",
                                            ),
                                            mileage=144350,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(
                                            city="Энгельс, Саратовская область",
                                            street="Саратовская область, Энгельсский р-н, Энгельс, Кожевенная ул., 12",
                                            country="Россия",
                                        ),
                                        uri="https://www.avito.ru/engels/avtomobili/kia_cerato_2010_2299481127",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 11, 30, 9, 37, 51)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=680000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=3),
                                            condition="Не битый",
                                            transmission=TypeAndTypeId(
                                                type="AUTOMATIC",
                                                type_id="ID_TRANSMISSION_TYPE_AUTOMATIC",
                                            ),
                                            mileage=120000,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(
                                            city="Ханты-Мансийский АО, Сургут",
                                            street="Тюменская область, Ханты-Мансийский автономный округ, Сургут, ул. Профсоюзов, 53",
                                            country="Россия",
                                        ),
                                        uri="https://www.avito.ru/surgut/avtomobili/kia_cerato_2010_2269051408",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 11, 29, 19, 51, 32)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=639000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Купе", type_id="ID_BODY_TYPE_COUPE"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=4),
                                            condition="Не битый",
                                            transmission=TypeAndTypeId(
                                                type="AUTOMATIC",
                                                type_id="ID_TRANSMISSION_TYPE_AUTOMATIC",
                                            ),
                                            mileage=220000,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(
                                            city="Тульская область, Тула",
                                            street="Тульская область, Тула",
                                            country="Россия",
                                        ),
                                        uri="https://www.avito.ru/tula/avtomobili/kia_cerato_2010_1895214091",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 11, 27, 14, 59, 7)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=440000,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=2),
                                            condition="Не битый",
                                            transmission=TypeAndTypeId(
                                                type="MANUAL",
                                                type_id="ID_TRANSMISSION_TYPE_MANUAL",
                                            ),
                                            mileage=200000,
                                        ),
                                    ),
                                    RelatedAd(
                                        geo=GeoAd(
                                            city="Санкт-Петербург",
                                            street="Санкт-Петербург, Полюстровский пр-т, 68А",
                                            country="Россия",
                                        ),
                                        uri="https://www.avito.ru/sankt-peterburg/avtomobili/kia_cerato_2010_2288910805",
                                        date=DatePublish(
                                            publish=datetime.datetime(2021, 11, 26, 4, 33, 54)
                                        ),
                                        price=PriceWithRegion(
                                            moscow=None,
                                            current=None,
                                            moscow_region=None,
                                            amount=599759,
                                            currency="RUB",
                                        ),
                                        vehicle=VehicleAd(
                                            body=TypeAndTypeId(
                                                type="Седан", type_id="ID_BODY_TYPE_SEDAN"
                                            ),
                                            year=2010,
                                            brand=Name(name="Kia"),
                                            drive=TypeAndTypeId(
                                                type="Передний",
                                                type_id="ID_DRIVING_WHEELS_TYPE_FRONT",
                                            ),
                                            model=Name(name="Cerato"),
                                            wheel=PositionAndPositionId(
                                                position="LEFT",
                                                position_id="ID_STEERING_WHEEL_TYPE_LEFT",
                                            ),
                                            engine=Engine(
                                                fuel=Fuel(
                                                    type="Бензиновый",
                                                    type_id="ID_ENGINE_TYPE_PETROL",
                                                ),
                                                power=Power(hp=126, kw=None),
                                                number=None,
                                                volume=1600,
                                                model=None,
                                                standarts=None,
                                                comment=None,
                                            ),
                                            owners=Count(count=3),
                                            condition="Не битый",
                                            transmission=TypeAndTypeId(
                                                type="MANUAL",
                                                type_id="ID_TRANSMISSION_TYPE_MANUAL",
                                            ),
                                            mileage=191169,
                                        ),
                                    ),
                                ],
                            )
                        ],
                        comment=None,
                    ),
                ),
                carfax={
                    "check": {"_comment": "Данные быстрой проверки на наличие данных у CarFax"},
                    "_comment": "Данные от CarFax",
                },
                registration_actions={
                    "date": {"update": "2021-12-23 17:04:29"},
                    "count": 8,
                    "items": [
                        {
                            "_id": 1566430438,
                            "geo": {
                                "city": "г Санкт-Петербург",
                                "house": "85",
                                "region": "г Санкт-Петербург",
                                "street": "ш Революции",
                            },
                            "code": "93",
                            "date": {"start": "2017-07-29 00:00:00"},
                            "type": "Изменение собственника по сделкам, произведенным в любой форме (купля-продажа, дарение, др.) с заменой государственных регистрационных знаков",
                            "owner": {"org": [], "type": "PERSON"},
                            "reg_num": "Х893ЕК178",
                            "actuality": [],
                            "attributes": [],
                            "identifiers": {"pts": "16ОК330069", "sts": "7852934229"},
                            "usage_allowed": True,
                        },
                        {
                            "_id": 1914428459,
                            "geo": {
                                "city": "г Альметьевск",
                                "house": "224",
                                "region": "Республика Татарстан",
                                "street": "ул Советская",
                            },
                            "code": "94",
                            "date": {"end": "2017-07-29 00:00:00", "start": "2015-05-29 00:00:00"},
                            "type": "Изменение собственника по сделкам, произведенным в любой форме с сохранением государственных регистрационных знаков",
                            "owner": {"org": [], "type": "PERSON"},
                            "reg_num": "К330НН777",
                            "actuality": [],
                            "attributes": [],
                            "identifiers": {"pts": "16ОК330069", "sts": "1632204986"},
                            "usage_allowed": True,
                        },
                        {
                            "_id": 2150761242,
                            "geo": {
                                "city": "г Москва",
                                "house": "21",
                                "region": "г Москва",
                                "street": "ул Перерва",
                            },
                            "code": "41",
                            "date": {"end": "2015-05-29 00:00:00", "start": "2015-05-12 00:00:00"},
                            "type": "Замена государственного регистрационного знака",
                            "owner": {"org": [], "type": "PERSON"},
                            "reg_num": "К330НН777",
                            "actuality": [],
                            "attributes": [],
                            "identifiers": {"pts": "78УН177933", "sts": "7733401111"},
                            "usage_allowed": True,
                        },
                        {
                            "_id": 3050492909,
                            "geo": {
                                "city": "г Москва",
                                "house": "3",
                                "region": "г Москва",
                                "street": "ул Юности",
                            },
                            "code": "93",
                            "date": {"end": "2015-05-12 00:00:00", "start": "2014-03-14 00:00:00"},
                            "type": "Изменение собственника по сделкам, произведенным в любой форме (купля-продажа, дарение, др.) с заменой государственных регистрационных знаков",
                            "owner": {"org": [], "type": "PERSON", "phone_number": "89688357870"},
                            "reg_num": "М011ОО197",
                            "actuality": [],
                            "attributes": [],
                            "identifiers": {"pts": "78УН177933", "sts": "7717580979"},
                            "usage_allowed": True,
                        },
                        {
                            "_id": 1078910090,
                            "geo": {
                                "city": "г Сергиев Посад",
                                "house": "4а",
                                "region": "Московская область",
                                "street": "ул Фабричная",
                            },
                            "code": "41",
                            "date": {"end": "2014-03-14 00:00:00", "start": "2014-02-06 00:00:00"},
                            "type": "Замена государственного регистрационного знака",
                            "owner": {"org": [], "type": "PERSON", "phone_number": "89268876606"},
                            "reg_num": "Е732АК750",
                            "actuality": [],
                            "attributes": [],
                            "identifiers": {"pts": "78УН177933", "sts": "5016775036"},
                            "usage_allowed": True,
                        },
                        {
                            "_id": 712556405,
                            "geo": {
                                "city": "г Сергиев Посад",
                                "house": "4а",
                                "region": "Московская область",
                                "street": "ул Фабричная",
                            },
                            "code": "16",
                            "date": {"end": "2014-02-06 00:00:00", "start": "2012-05-03 00:00:00"},
                            "type": "Регистрация ТС, прибывших из других регионов РФ",
                            "owner": {"org": [], "type": "PERSON", "phone_number": "89268876606"},
                            "reg_num": "Р300ЕЕ190",
                            "actuality": [],
                            "attributes": [],
                            "identifiers": {"pts": "78УН177933", "sts": "50ХС717705"},
                            "usage_allowed": True,
                        },
                        {
                            "_id": 2700057716,
                            "geo": {
                                "city": "г Москва",
                                "house": "6 1",
                                "region": "г Москва",
                                "street": "ул 50 лет Октября",
                            },
                            "code": "62",
                            "date": {"end": "2012-05-03 00:00:00", "start": "2012-04-06 00:00:00"},
                            "type": "В связи с прекращением права собственности (отчуждение, конфискация ТС)",
                            "owner": {"org": [], "type": "PERSON"},
                            "reg_num": "КН543О77",
                            "actuality": [],
                            "attributes": [],
                            "identifiers": {"pts": "78УН177933"},
                            "usage_allowed": False,
                        },
                        {
                            "_id": 1870131322,
                            "geo": [],
                            "code": "11",
                            "date": {"end": "2012-04-06 00:00:00", "start": "2010-09-30 00:00:00"},
                            "type": "Первичная регистрация",
                            "owner": {"org": [], "type": "PERSON"},
                            "reg_num": "У917ВО197",
                            "actuality": [],
                            "attributes": [],
                            "identifiers": {"pts": "78УН177933", "sts": "77УЕ102109"},
                            "usage_allowed": True,
                        },
                    ],
                    "_comment": "Регистрационные действия",
                    "has_annulment": False,
                },
                restrictions={
                    "registration_actions": {
                        "date": {"update": "2021-12-23 16:56:23"},
                        "count": 0,
                        "items": [],
                        "_comment": "Ограничения на рег. действия",
                        "has_restrictions": False,
                    },
                    "registration_actions_archive": {
                        "date": {"update": "2018-07-14 15:20:24"},
                        "count": 1,
                        "items": [
                            {
                                "_id": 1268212080,
                                "date": {
                                    "added": "2017-08-05 00:00:00",
                                    "start": "2017-07-29 00:00:00",
                                },
                                "vehicle": {"year": 2010, "model": {"name": "Киа Серато Киа"}},
                                "restrict": {
                                    "type": "Запрет на регистрационные действия",
                                    "number": "278970919/1616",
                                    "reason": "Документ: 278970919/1616 от 29.07.2017, отставнова яна игоревна, спи: 92161015482461, ип: 58103/17/16016-ип от 28.07.2017",
                                },
                                "actuality": {"date": "2018-07-14 15:20:24"},
                                "initiator": {
                                    "name": "Судебный Пристав",
                                    "region": {"name": "Республика Татарстан"},
                                },
                            }
                        ],
                        "_comment": "Архив ограничений на рег. действия",
                        "has_restrictions": True,
                    },
                },
                ads={
                    "history": {
                        "date": {"update": "2021-12-23 17:31:55"},
                        "count": 1,
                        "items": [
                            {
                                "_id": 385011704,
                                "geo": {"city": "Санкт-Петербург", "region": "Санкт-Петербург"},
                                "uri": "https://www.avito.ru/sankt-peterburg/avtomobili/kia_cerato_2010_979813753",
                                "date": {"publish": "2019-01-24 00:00:00"},
                                "text": "Продается отличный аппарат. Полностью обслужен пройдет любые проверки. Автомат не пинается , дорогу держит хорошо. Масло менялось 17 января (есть наряд). Салон чистый. Эксклюзивный внешний вид. В подарок летний комплект резины на литье BBS 17 радиус. Причина продажи новое авто. Звоните смотрите в любое удобное время. Перекупы и салоны мимо езжу на машине каждый день.",
                                "price": {"value": 545000},
                                "photos": {
                                    "grz": {
                                        "X893EK178": [
                                            "https://ng-images.avtocod.ru/images/2021/06/09/5533f41b30327998c81da33b74fa1952.jpg"
                                        ]
                                    },
                                    "board": [
                                        "https://s.nomerogram.ru/photo/c3GE3WT284ox0UJNF0gau4w9xaOvAAeyM7KbGOdmOkr1AxaxQTFVyTnvUM8p4_8iMvUcGYayHnMAsbIaV4UGrMon.jpg",
                                        "https://s.nomerogram.ru/photo/V1WAMywuyU_8QhP39XTQiPYjk1mWy_NIbYLuWN-m9EaVNmP2-8bNjQ_wFgPNZ-KdA1bIt97dE33gOzrj-F5S5d_F.jpg",
                                        "https://s.nomerogram.ru/photo/jnnUwAxWsC24J0vUdar6DAXJ3BdFobRe0GW7Harh8U1_imZnATaH-4ClWPNPK3uIaujrNjhF2KCMZuWrdVhZ7-al.jpg",
                                        "https://s.nomerogram.ru/photo/qiiBhoC-lWJMN639_mONugrXGP3a-6BVYU-lF2fvXbWmIwIwJjJfjYGAmcHOruvZFLsOSrAmHrwxegmY-4theDO2.jpg",
                                        "https://s.nomerogram.ru/photo/YuNiJLqN5cVzDC8qHiuReLj7H6CUOMlsTrs_zpOnJjOzzc1V6pmd5nXvPBsa82X9Qg1zXGzQVPAbZ5mJOlvUWSl8.jpg",
                                        "https://s.nomerogram.ru/photo/YaTiAaCmTnA22catyM0nJD-GcBSvTtCavD5LdQ9uk8OmHBwTMUzhsjjdrV7fr5TBksejq3yNeM1Nv6muJHBLUSCO.jpg",
                                        "https://s.nomerogram.ru/photo/2uHv6CzTCYEXWewbpaKbCZtCWK8gwAiDJozi8fC3btKV61RJM7g3aYAza8jiHzx93s3LOxNNOCCyoCU-bgmRyY4z.jpg",
                                        "https://s.nomerogram.ru/photo/jOMhsdNILq_Tn7HFBWnqfpsdUWyCSWt_a2gsuVKW7l3vAjTJHYjryE6At1vcFVh9H2bTLbneYUMQDJonK7AF7LEB.jpg",
                                        "https://s.nomerogram.ru/photo/aX7SJtTvzgbZbnpvru1qLDIRyc9rZDIWaIPh3lAO-NAQwgBv25T_qFlRzFGMdoy2gJ16V_8FU7lAMkYy3tLK7uqT.jpg",
                                    ],
                                    "local": [
                                        "https://ng-images.avtocod.ru/images/2021/06/09/84df0ebcddf49d3c4b0b01ad07536399.jpg",
                                        "https://ng-images.avtocod.ru/images/2021/06/09/5533f41b30327998c81da33b74fa1952.jpg",
                                        "https://ng-images.avtocod.ru/images/2021/06/09/89eea0fed318ad1899f2fc1225a893bb.jpg",
                                        "https://ng-images.avtocod.ru/images/2021/06/09/cdb648af401fe94d5126f65a60bffc95.jpg",
                                        "https://ng-images.avtocod.ru/images/2021/06/09/43df468db4dbe7ed3307a664c6db5a62.jpg",
                                        "https://ng-images.avtocod.ru/images/2021/06/09/f9c451ee114a0cf33520371e814572c6.jpg",
                                        "https://ng-images.avtocod.ru/images/2021/06/09/764bc352b11ddb476f3041f31e680e98.jpg",
                                        "https://ng-images.avtocod.ru/images/2021/06/09/583773698a7c0e337bb83165aef80ad6.jpg",
                                        "https://ng-images.avtocod.ru/images/2021/06/09/ef6c1bf723ed059e7c588e2343173375.jpg",
                                    ],
                                },
                                "seller": [],
                                "vehicle": {
                                    "body": {"color": []},
                                    "year": 2010,
                                    "brand": {"name": "Kia"},
                                    "doors": [],
                                    "drive": [],
                                    "model": {"name": "Cerato"},
                                    "wheel": [],
                                    "engine": {"fuel": [], "power": []},
                                    "owners": [],
                                    "mileage": 165000,
                                    "passport": [],
                                    "identifiers": [],
                                    "transmission": [],
                                },
                            }
                        ],
                        "_comment": "История объявлений",
                    }
                },
                customs={
                    "history": {
                        "date": {"update": "2021-12-22 15:27:25"},
                        "count": 1,
                        "items": [
                            {
                                "_id": 2328079636,
                                "org": {
                                    "name": "Ото И Тк №1 Северо-Западного Акцизного Таможенного Поста (Специализированного)"
                                },
                                "tax": [],
                                "date": {"event": "2010-09-16 00:00:00"},
                                "color": {"name": "Серебристый"},
                                "owner": [],
                                "price": {"amount": 302672},
                                "country": {"to": [], "from": {"name": "Финляндская Республика"}},
                                "ecology": [],
                                "document": {"number": "10009191/160910/0012341"},
                                "specification": {
                                    "raw": 'НОВЫЙ ЛЕГКОВОЙ А/М "KIA CERATO" 2010 Г.В, VIN KNAFU611BA5295980, С БЕНЗИНОВЫМ ДВИГАТЕЛЕМ ОБЪЕМОМ 1591 СМ3, МОЩНОСТЬ 126 ЛС/92,7 КВТ, МОДЕЛЬ ДВИГАТЕЛЯ G4FC, № AH242135, ПОЛНАЯ МАССА 1720 КГ, КУПЕ, ЦВЕТ СЕРЕБРИСТЫЙ,КОД ОКП 451431 КЛИМАТ КОНТРОЛЬ, ЗАПРА'
                                },
                            }
                        ],
                        "_comment": "История по таможне",
                    }
                },
                repairs={
                    "history": {
                        "date": [],
                        "count": 0,
                        "items": [],
                        "_comment": "История ремонтных работ по страховке",
                    },
                    "_comment": "Ремонтные работы",
                },
                leasing=None,
                taxi={
                    "history": {"count": 0, "items": [], "_comment": "Такси"},
                    "used_in_taxi": False,
                },
                insurance={
                    "osago": {
                        "date": {"update": "2021-12-23 17:04:29"},
                        "count": 1,
                        "items": [
                            {
                                "_id": 1025907982,
                                "geo": {"region": "г Москва"},
                                "date": {
                                    "end": "2022-06-24 00:00:00",
                                    "start": "2021-06-25 00:00:00",
                                    "created": "2021-06-25 00:00:00",
                                    "periods": [{"end": "2022-06-24", "start": "2021-06-25"}],
                                },
                                "owner": {
                                    "dob": "1986-03-01",
                                    "name": "Б***** Елена Юрьевна",
                                    "type": "PERSON",
                                },
                                "policy": {
                                    "number": "0180362030",
                                    "series": "ХХХ",
                                    "expired": False,
                                    "is_active": False,
                                },
                                "insurer": {"name": 'ООО "СК "Согласие"'},
                                "vehicle": {
                                    "model": {"name": "Kia Cerato (категория «B»)"},
                                    "seats": [],
                                    "engine": {"power": {"hp": 126}},
                                    "weight": [],
                                    "identifiers": {"vin": "KNAFU611BA5295980"},
                                },
                                "contract": {
                                    "kbm": 1,
                                    "amount": {"currency": "RUB"},
                                    "is_active": False,
                                    "using_type": {"status": "PERSONAL", "description": "Личная"},
                                    "has_trailer": False,
                                    "is_follow_to_registration": False,
                                },
                                "insurant": {
                                    "dob": "1986-03-01",
                                    "name": "Б***** Елена Юрьевна",
                                    "type": "PERSON",
                                },
                                "restrictions": {"type": "WITH RESTRICTIONS", "drivers": 1},
                            }
                        ],
                        "_comment": "ОСАГО",
                    }
                },
                leasings={
                    "date": {"update": "2021-12-23 17:04:29"},
                    "count": 0,
                    "items": [],
                    "_comment": "Лизинг",
                    "used_in_leasing": False,
                },
            ),
            active_to=datetime.datetime(3000, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
            created_at=datetime.datetime(
                2021, 10, 6, 14, 43, 47, 908000, tzinfo=datetime.timezone.utc
            ),
            created_by="system",
            domain_uid="avtocod",
            updated_at=datetime.datetime(
                2021, 12, 23, 17, 31, 57, 416000, tzinfo=datetime.timezone.utc
            ),
            updated_by="system",
            vehicle_id="KNAFU611BA5295980",
            active_from="1900-01-01T00:00:00.000Z",
            progress_ok=28,
            requested_at="2021-12-23T17:31:54.432Z",
            progress_wait=0,
            progress_error=0,
            report_type_uid="avtocod_profi_full_report@avtocod",
            last_generation_stat=LastGenerationStat(
                duration=1958,
                start_time=datetime.datetime(
                    2021, 12, 23, 17, 31, 54, 432000, tzinfo=datetime.timezone.utc
                ),
                complete_time=datetime.datetime(
                    2021, 12, 23, 17, 31, 56, 390000, tzinfo=datetime.timezone.utc
                ),
            ),
        ),
        is_ready=True,
        is_completed=True,
        tags_ids=[],
        stage="",
        auto_index=27,
        analytical_mileage=233197,
        max_wait_to_ready_time=None,
        wait_to_ready_time=None,
        guarantee_status="approved",
        generation_start_time=datetime.datetime(
            2021, 12, 23, 17, 31, 54, tzinfo=datetime.timezone.utc
        ),
        additional_blocks=[],
        created_at=datetime.datetime(2021, 12, 23, 17, 31, 43, tzinfo=datetime.timezone.utc),
        updated_at=datetime.datetime(2021, 12, 23, 17, 32, 54, tzinfo=datetime.timezone.utc),
    )
