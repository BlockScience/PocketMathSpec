from ..Spaces import modify_servicer_pokt_space


modify_servicer_pokt_holdings = {"name": "Modify Servicer POKT Holdings",
                           "description": "The mechanism to update the personal holdings of a servicer",
                           "constraints": [],
                           "logic": "The servicer at DOMAIN[0].servicer_address has its POKT Holdings modified by DOMAIN[0].value",
                           "domain": [modify_servicer_pokt_space],
                           "parameters_used": None}

modify_servicer_stake = {"name": "Modify Servicer Stake",
                           "description": "The mechanism to update the stake of a servicer",
                           "constraints": [],
                           "logic": "The servicer at DOMAIN[0].servicer_address has its stake modified by DOMAIN[0].value",
                           "domain": [modify_servicer_pokt_space],
                           "parameters_used": None}

