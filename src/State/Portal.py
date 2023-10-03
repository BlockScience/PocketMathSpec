from ..Types import StakeStatusType, ApplicationEntityType
from typing import List

portal_state = {"name": "Portal State",
              "notes": "",
              "variables": [{"type": StakeStatusType,
                             "name": "Stake Status",
                             "description": "The status of staking for the actor",
                             "symbol": None,
                             "domain": None},
                             {"type": List[ApplicationEntityType],
                             "name": "Delegators",
                             "description": "The applications which have delegated to this portal",
                             "symbol": None,
                             "domain": None}]}