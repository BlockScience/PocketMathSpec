from ..Spaces import (mint_block_rewards_space, mint_pokt_mechanism_space, assign_servicer_salary_space,
                      validator_block_reward_space)

block_reward_policy_aggregate = {"name": "Block Reward Policy Aggregate",
                        "description": "The aggregate policy for creating the total amount of block reward and also splitting it between different groups.",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [mint_block_rewards_space],
                        "codomain": [mint_pokt_mechanism_space, assign_servicer_salary_space, validator_block_reward_space],
                        "parameters_used": ["validator_fee_percentage", "dao_fee_percentage", "relays_to_tokens_multiplier",
                                            "portal_fee_per_relay", "application_fee_per_relay", "block_proposer_allocation",
                                            "maturity_relay_cost", "maturity_relay_charge", "min_bootstrap_gateway_fee_per_relay",
                                            "max_bootstrap_servicer_cost_per_relay", "servicer_bootstrap_unwind_start",
                                            "servicer_bootstrap_end", "gateway_bootstrap_unwind_start", "gateway_bootstrap_unwind_end"]}

