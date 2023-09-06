from ..Types import uPOKTType, PublicKeyType, GeoZoneType, RelayChainType
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
                             {"type": List[RelayChainType],
                             "name": "Relay Chains",
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
                             "description": "The number of servicers per request to be using",
                             "symbol": None,
                             "domain": None},]}






