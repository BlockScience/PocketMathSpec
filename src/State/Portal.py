from ..Types import StakeStatusType, ApplicationEntityType, uPOKTType
from typing import List

gateway_state = {
    "name": "Gateway State",
    "notes": "",
    "variables": [
        {
            "type": StakeStatusType,
            "name": "Stake Status",
            "description": "The status of staking for the actor",
            "symbol": None,
            "domain": None,
        },
        {
            "type": List[ApplicationEntityType],
            "name": "Delegators",
            "description": "The applications which have delegated to this gateway",
            "symbol": None,
            "domain": None,
        },
        {
            "type": uPOKTType,
            "name": "POKT Holdings",
            "description": "The personal holdings of the application in uPOKT",
            "symbol": None,
            "domain": None,
        },
        {
            "type": uPOKTType,
            "name": "Staked POKT",
            "description": "The amount that is staked by the application currently in uPOKT",
            "symbol": None,
            "domain": None,
        },
    ],
}
