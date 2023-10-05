from ..Spaces import (mint_block_rewards_space, mint_pokt_mechanism_space, assign_servicer_salary_space,
                      validator_block_reward_space, burn_pokt_space, burn_pokt_mechanism_space)

block_reward_policy_aggregate = {"name": "Block Reward Policy Aggregate",
                        "description": """The aggregate policy for creating the total amount of block reward and also splitting it between different groups.

Based upon the numerous parameters, the total reward for each group is determined. For a more detailed version of the policy, one can look here: https://docs.google.com/spreadsheets/d/1QYe6NzuiyimsXs5cT1BSM-UT1DtX_K38cOZsEFJOtdA/edit#gid=242780369""",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [mint_block_rewards_space],
                        "codomain": [mint_pokt_mechanism_space, assign_servicer_salary_space, validator_block_reward_space],
                        "parameters_used": ["validator_fee_percentage", "dao_fee_percentage", "relays_to_tokens_multiplier",
                                            "portal_fee_per_relay", "application_fee_per_relay", "block_proposer_allocation",
                                            "transaction_fee", "maturity_relay_cost", "maturity_relay_charge", "min_bootstrap_gateway_fee_per_relay",
                                            "max_bootstrap_servicer_cost_per_relay", "servicer_bootstrap_unwind_start",
                                            "servicer_bootstrap_end", "gateway_bootstrap_unwind_start", "gateway_bootstrap_unwind_end"]}


burn_pokt_policy = {
    "name": "Burn POKT Policy",
    "description": "Policy which takes care of treasury POKT being burnt.",
    "constraints": [],
    "policy_options": [],
    "domain": [burn_pokt_space],
    "codomain": [burn_pokt_mechanism_space],
    "parameters_used": [],
}