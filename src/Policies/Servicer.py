from ..Spaces import servicer_stake_space

servicer_stake_policy = {"name": "Servicer Stake Policy",
                        "description": "",
                        "constraints": ["DOMAIN[0].public_key must not be null",
                                        "DOMAIN[0].amount > 0",
                                        "LEN(DOMAIN[0].relay_chains) > 0",
                                        "All chains in DOMAIN[0].relay_chains must be valid"],
                        "policy_options": [],
                        "domain": [servicer_stake_space],
                        "codomain": [servicer_stake_space],
                        "parameters_used": []}

set_servicer_parameters_policy = {"name": "Set Servicer Parameters Policy",
                        "description": "",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [servicer_stake_space],
                        "codomain": [],
                        "parameters_used": []}