from ..Spaces import modify_servicer_pokt_space, servicer_param_update_space, servicer_unpause_space2, servicer_pause_space2


modify_servicer_pokt_holdings = {"name": "Modify Servicer POKT Holdings",
                           "description": "The mechanism to update the personal holdings of a servicer",
                           "constraints": [],
                           "logic": "The servicer at DOMAIN[0].servicer_address has its POKT Holdings modified by DOMAIN[0].value",
                           "domain": [modify_servicer_pokt_space],
                           "parameters_used": []}

modify_servicer_stake = {"name": "Modify Servicer Stake",
                           "description": "The mechanism to update the stake of a servicer",
                           "constraints": [],
                           "logic": "The servicer at DOMAIN[0].servicer_address has its stake modified by DOMAIN[0].value",
                           "domain": [modify_servicer_pokt_space],
                           "parameters_used": []}

prune_servicer_qos = {"name": "Prune Servicer QoS",
                           "description": "The mechanism which prunes historical QoS (TestScores, ReportCard, etc…)",
                           "constraints": [],
                           "logic": "The servicer at DOMAIN[0].public_key has its QoS metrics pruned",
                           "domain": [servicer_param_update_space],
                           "parameters_used": []}

update_servicer_params = {"name": "Update Servicer Params",
                           "description": "The mechanism which updates servicer params",
                           "constraints": [],
                           "logic": "The servicer at DOMAIN[0].public_key has its params updated with the latest stake, assuming the stake was greater than the prior stake",
                           "domain": [servicer_param_update_space],
                           "parameters_used": []}

servicer_unpause_mechanism = {"name": "Servicer Unpause Mechanism",
                           "description": "The mechanism which unpauses a servicer",
                           "constraints": [],
                           "logic": "The servicer at DOMAIN[0].address has its pause_height variable updated to None",
                           "domain": [servicer_unpause_space2],
                           "parameters_used": []}

servicer_update_pause_height = {"name": "Servicer Update Pause Height",
                           "description": "The mechanism which updates the pause height ",
                           "constraints": [],
                           "logic": "The servicer at DOMAIN[0].address has its pause_height variable updated to DOMAIN[0].height",
                           "domain": [servicer_pause_space2],
                           "parameters_used": []}