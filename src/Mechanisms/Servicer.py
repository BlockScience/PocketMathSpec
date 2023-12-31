from ..Spaces import (modify_servicer_pokt_space, servicer_param_update_space, servicer_unpause_space2,
                      servicer_pause_space2, servicer_stake_status_space, servicer_relay_space,
                      remove_servicer_space)


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

update_servicer_stake_status = {"name": "Update Servicer Stake Status",
                           "description": "The mechanism which updates the staking status and as well the unstaking height.",
                           "constraints": [],
                           "logic": "The servicer at DOMAIN[0].address has its unstaking_height variable updated to DOMAIN[0].height which will be none if it is staking. It will also have its stake status set to DOMAIN[0].status.",
                           "domain": [servicer_stake_status_space],
                           "parameters_used": []}

remove_session = {"name": "Remove Session",
                           "description": "The mechanism which removes a session from the global state.",
                           "constraints": [],
                           "logic": "The session from DOMAIN[0] is removed from the global session state.",
                           "domain": [servicer_relay_space],
                           "parameters_used": []}

remove_servicer = {"name": "Remove Servicer",
                           "description": "The mechanism which removes a servicer from the global state.",
                           "constraints": [],
                           "logic": "The servicer from DOMAIN[0] is removed from the global session state.",
                           "domain": [remove_servicer_space],
                           "parameters_used": []}
