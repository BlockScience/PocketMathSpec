from ..Spaces import (validator_stake_space, modify_validator_pokt_space, validator_param_update_space,
                      validator_unpause_space, validator_block_reward_space)

validator_stake_policy = {"name": "Validator Stake Policy",
                        "description": "Policy for determining actions to take from a validator moving to stake.",
                        "constraints": ["DOMAIN[0].public_key must not be null",
                                        "DOMAIN[0].amount > 0",],
                        "policy_options": [],
                        "domain": [validator_stake_space],
                        "codomain": [validator_stake_space, modify_validator_pokt_space, modify_validator_pokt_space],
                        "parameters_used": []}

set_validator_parameters_policy = {"name": "Set Validator Parameters Policy",
                        "description": "Policy for determining the impact of validator parameter changes",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [validator_stake_space],
                        "codomain": [validator_param_update_space],
                        "parameters_used": []}

validator_unpause_policy =  {"name": "Validator Unpause Policy",
                        "description": "Policy for determining whether a validator can be unpaused",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [validator_unpause_space],
                        "codomain": [validator_unpause_space],
                        "parameters_used": ["minimum_validator_pause_time"]}


validator_block_reward_policy = {"name": "Validator Block Reward Policy",
                        "description": "Policy for allocation of block rewards to validator",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [validator_block_reward_space],
                        "codomain": [],
                        "parameters_used": []}


