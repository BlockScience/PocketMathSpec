from typing import List
from ..Types import ServiceEntityType, SessionType, PortalEntityType

global_state = {"name": "Global State",
              "notes": "",
              "variables": [{"type": List[ServiceEntityType],
                             "name": "Services",
                             "description": "The services active in the system",
                             "symbol": None,
                             "domain": None},
                             {"type": List[SessionType],
                             "name": "Sessions",
                             "description": "A Session is a time-based mechanism used to regulate the various interactions (Web3 access, monitoring, etc) between protocol actors to enable the Utilitarian economy in a fair and secure manner. A single session may extend multiple Blocks as determined by SessionBlockFrequency.",
                             "symbol": None,
                             "domain": None},
                             {"type": List[PortalEntityType],
                             "name": "Portals",
                             "description": "Portals held within the system.",
                             "symbol": None,
                             "domain": None},]}



