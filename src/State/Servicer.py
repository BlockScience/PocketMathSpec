from ..Types import uPOKTType, ServicerReportCardType, ServicerTestScoresType, PublicKeyType, GeoZoneType, RelayChainType, ServiceURLType, BlockHeightType
from typing import List

servicer_state = {"name": "Servicer State",
              "notes": "",
              "variables": [{"type": PublicKeyType,
                             "name": "Public key",
                             "description": "The identifier of the node",
                             "symbol": None,
                             "domain": None},
                             {"type": uPOKTType,
                             "name": "Servicer Salary",
                             "description": "A ServicerSalary is assigned to each individual Servicer based on their specific ReportCard, and is distributed every SalaryBlockFrequency",
                             "symbol": None,
                             "domain": None},
                             {"type": ServicerReportCardType,
                             "name": "Report Card",
                             "description": "The report card used when determing salary for a servicer",
                             "symbol": None,
                             "domain": None},
                             {"type": ServicerTestScoresType,
                             "name": "Test Scores",
                             "description": "The QoS test scores",
                             "symbol": None,
                             "domain": None},
                             {"type": uPOKTType,
                             "name": "POKT Holdings",
                             "description": "The personal holdings of the servicer in uPOKT",
                             "symbol": None,
                             "domain": None},
                             {"type": uPOKTType,
                             "name": "Staked POKT",
                             "description": "The personal holdings of the servicer in uPOKT",
                             "symbol": None,
                             "domain": None},
                             {"type": ServiceURLType,
                             "name": "Service URL",
                             "description": "The API endpoint where the Web3 service is provided",
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
                             {"type": PublicKeyType,
                             "name": "Operator Public Key",
                             "description": "OPTIONAL; The non-custodial pubKey operating this node",
                             "symbol": None,
                             "domain": None},
                             {"type": BlockHeightType,
                             "name": "Pause Height",
                             "description": "The height for which a servicer has been paused at",
                             "symbol": None,
                             "domain": None}
                             ]}
