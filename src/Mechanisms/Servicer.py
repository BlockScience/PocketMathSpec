from ..Spaces import modify_servicer_pokt_space, servicer_param_update_space


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

prune_servicer_qos = {"name": "Prune Servicer QoS",
                           "description": "The mechanism which prunes historical QoS (TestScores, ReportCard, etc…)",
                           "constraints": [],
                           "logic": "The servicer at DOMAIN[0].public_key has its QoS metrics pruned",
                           "domain": [servicer_param_update_space],
                           "parameters_used": None}

update_servicer_params = {"name": "Update Servicer Params",
                           "description": "The mechanism which updates servicer params",
                           "constraints": [],
                           "logic": "The servicer at DOMAIN[0].public_key has its params updated with the latest stake, assuming the stake was greater than the prior stake",
                           "domain": [servicer_param_update_space],
                           "parameters_used": None}



