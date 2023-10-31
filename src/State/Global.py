from typing import List
from ..Types import (
    ServiceEntityType,
    SessionType,
    GatewayEntityType,
    ServicerEntityType,
    ApplicationEntityType,
    DAOEntityType,
    ValidatorEntityType,
    GeoZoneType,
    uPOKTType,
)

global_state = {
    "name": "Global State",
    "notes": "",
    "variables": [
        {
            "type": List[ServiceEntityType],
            "name": "Services",
            "description": "The services active in the system",
            "symbol": None,
            "domain": None,
        },
        {
            "type": List[SessionType],
            "name": "Sessions",
            "description": "A Session is a time-based mechanism used to regulate the various interactions (Web3 access, monitoring, etc) between protocol actors to enable the Utilitarian economy in a fair and secure manner. A single session may extend multiple Blocks as determined by SessionBlockFrequency.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": List[GatewayEntityType],
            "name": "Gateways",
            "description": "Gateways held within the system.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": List[ServicerEntityType],
            "name": "Servicers",
            "description": "Servicers held within the system.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": List[GeoZoneType],
            "name": "Geozones",
            "description": "Geozones used within the system.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": List[ApplicationEntityType],
            "name": "Applications",
            "description": "The applications present in the current state.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": List[ValidatorEntityType],
            "name": "Validators",
            "description": "The validators present in the current state.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": DAOEntityType,
            "name": "DAO",
            "description": "The DAO which helps with governance of the system.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": uPOKTType,
            "name": "Floating Supply",
            "description": "The amount of floating supply in the ecosystem",
            "symbol": None,
            "domain": None,
        },
        {
            "type": uPOKTType,
            "name": "Relay Fees",
            "description": "The amount of fees custodied but not yet disbursed.",
            "symbol": None,
            "domain": None,
        },
    ],
}
