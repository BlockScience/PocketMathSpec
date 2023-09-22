from ..Spaces import (mint_block_rewards_space, mint_pokt_mechanism_space, assign_servicer_salary_space,
                      validator_block_reward_space)

block_reward_policy_aggregate = {"name": "Block Reward Policy Aggregate",
                        "description": "The aggregate policy for creating the total amount of block reward and also splitting it between different groups.",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [mint_block_rewards_space],
                        "codomain": [mint_pokt_mechanism_space, assign_servicer_salary_space, validator_block_reward_space],
                        "parameters_used": ["validator_fee_percentage", "dao_fee_percentage", "relays_to_tokens_multiplier",
                                            "portal_fee_per_relay", "application_fee_per_relay"]}

