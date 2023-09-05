from ..Spaces import servicer_stake_space, modify_servicer_pokt_space, servicer_param_update_space, servicer_unpause_space, servicer_unpause_space2

servicer_stake_policy = {"name": "Servicer Stake Policy",
                        "description": "",
                        "constraints": ["DOMAIN[0].public_key must not be null",
                                        "DOMAIN[0].amount > 0",
                                        "LEN(DOMAIN[0].relay_chains) > 0",
                                        "All chains in DOMAIN[0].relay_chains must be valid"],
                        "policy_options": [],
                        "domain": [servicer_stake_space],
                        "codomain": [servicer_stake_space, modify_servicer_pokt_space, modify_servicer_pokt_space],
                        "parameters_used": ["minimum_stake_servicer"]}

set_servicer_parameters_policy = {"name": "Set Servicer Parameters Policy",
                        "description": "",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [servicer_stake_space],
                        "codomain": [servicer_param_update_space, servicer_param_update_space],
                        "parameters_used": []}

servicer_unpause_policy = {"name": "Servicer Unpause Policy",
                        "description": "The policy which determines if an unpause can take place",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [servicer_unpause_space],
                        "codomain": [servicer_unpause_space2],
                        "parameters_used": ["minimum_pause_time"]}