from ..Types import uPOKTType, PublicKeyType, GeoZoneType, ServiceType, StakeStatusType, BlockHeightType, PortalEntityType
from typing import List


application_state = {"name": "Application State",
              "notes": "",
              "variables": [{"type": PublicKeyType,
                             "name": "Public key",
                             "description": "The identifier of the application",
                             "symbol": None,
                             "domain": None},
                             {"type": uPOKTType,
                             "name": "POKT Holdings",
                             "description": "The personal holdings of the application in uPOKT",
                             "symbol": None,
                             "domain": None},
                             {"type": uPOKTType,
                             "name": "Staked POKT",
                             "description": "The staked amount of the application in uPOKT",
                             "symbol": None,
                             "domain": None},
                             {"type": List[ServiceType],
                             "name": "Services",
                             "description": "The flavor(s) of Web3 hosted by this Servicer",
                             "symbol": None,
                             "domain": None},
                             {"type": GeoZoneType,
                             "name": "GeoZone",
                             "description": "The physical geo-location identifier this Servicer registered in",
                             "symbol": None,
                             "domain": None},
                             {"type": int,
                             "name": "Number of Servicers",
                             "description": "The number of servicers an application would prefer, if available, for a session.",
                             "symbol": None,
                             "domain": None},
                             {"type": StakeStatusType,
                             "name": "Stake Status",
                             "description": "The status of staking for the actor",
                             "symbol": None,
                             "domain": None},
                             {"type": BlockHeightType,
                             "name": "Unstaking Height",
                             "description": "The height for which a servicer has begun unstaking at or none to represent no unstaking",
                             "symbol": None,
                             "domain": None},
                             {"type": PortalEntityType,
                             "name": "Delegate",
                             "description": "The portal which has been delegated to or None if there is no delegate",
                             "symbol": None,
                             "domain": None}
                             ]}






