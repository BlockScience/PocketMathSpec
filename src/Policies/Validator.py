from ..Spaces import (validator_stake_space, modify_validator_pokt_space)

validator_stake_policy = {"name": "Validator Stake Policy",
                        "description": "Policy for determining actions to take from a validator moving to stake.",
                        "constraints": ["DOMAIN[0].public_key must not be null",
                                        "DOMAIN[0].amount > 0",],
                        "policy_options": [],
                        "domain": [validator_stake_space],
                        "codomain": [validator_stake_space, modify_validator_pokt_space, modify_validator_pokt_space],
                        "parameters_used": []}
