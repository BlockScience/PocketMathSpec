from ..Types import uPOKTType, ServicerReportCardType, ServicerTestScoresType, PublicKeyType, GeoZoneType, ServiceType, ServiceURLType, BlockHeightType
from typing import List

treasury_state = {"name": "Treasury State",
              "notes": "",
              "variables": [{"type": uPOKTType,
                             "name": "Floating Supply",
                             "description": "The amount of floating supply in the ecosystem",
                             "symbol": None,
                             "domain": None}]}