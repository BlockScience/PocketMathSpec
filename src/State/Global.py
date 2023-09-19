from typing import List
from ..Types import RelayChainEntityType

global_state = {"name": "Global State",
              "notes": "",
              "variables": [{"type": List[RelayChainEntityType],
                             "name": "Relay Chains",
                             "description": "The relay chains active in the system",
                             "symbol": None,
                             "domain": None}]}



