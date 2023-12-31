from ..Spaces import (
    mint_block_rewards_space,
    mint_pokt_mechanism_space,
    assign_servicer_salary_space,
    validator_block_reward_space,
    burn_pokt_space,
    burn_pokt_mechanism_space,
    distribute_fees_space,
    decrease_relay_fees_space,
    modify_validator_pokt_space,
    modify_dao_pokt_space,
)

block_reward_policy_aggregate = {
    "name": "Block Reward Policy Aggregate",
    "description": """The aggregate policy for creating the total amount of block reward and also splitting it between different groups.

Based upon the numerous parameters, the total reward for each group is determined. For a more detailed version of the policy, one can look here: https://docs.google.com/spreadsheets/d/1QYe6NzuiyimsXs5cT1BSM-UT1DtX_K38cOZsEFJOtdA/edit#gid=242780369.

The burn on the demand-side to pay for access and the distribution of rewards to servicers are kept separate, even if they relate to one another in the aggregate sense when it comes to modelling the supply over time.

Relay Mining will determine probabalistically how much relays each servicer did, and, therefore, who much of the servicer rewards they are entitled to.

The pool of rewards should accumulate over time until drawn down by the servicers submittting a "claim" for their work using the appropriate "proof".
""",
    "constraints": [],
    "policy_options": [],
    "domain": [mint_block_rewards_space],
    "codomain": [
        mint_pokt_mechanism_space,
        assign_servicer_salary_space,
        validator_block_reward_space,
    ],
    "parameters_used": [
        "relays_to_tokens_multiplier",
        "block_proposer_allocation",
        "transaction_fee",
        "maturity_relay_cost",
        "maturity_relay_charge",
        "min_bootstrap_gateway_fee_per_relay",
        "max_bootstrap_servicer_cost_per_relay",
        "servicer_bootstrap_unwind_start",
        "servicer_bootstrap_end",
        "gateway_bootstrap_unwind_start",
        "gateway_bootstrap_unwind_end",
    ],
}


distribute_fees_policy = {
    "name": "Distribute Fees Policy",
    "description": """The aggregate policy for determining what fees are allocated where.
                        
For a more detailed version of the policy, one can look here: https://docs.google.com/spreadsheets/d/1QYe6NzuiyimsXs5cT1BSM-UT1DtX_K38cOZsEFJOtdA/edit#gid=242780369""",
    "constraints": [],
    "policy_options": [],
    "domain": [distribute_fees_space],
    "codomain": [
        decrease_relay_fees_space,
        modify_validator_pokt_space,
        modify_dao_pokt_space,
    ],
    "parameters_used": ["validator_fee_percentage", "dao_fee_percentage"],
}


burn_pokt_policy = {
    "name": "Burn POKT Policy",
    "description": "Policy which takes care of POKT being burnt.",
    "constraints": [],
    "policy_options": [],
    "domain": [burn_pokt_space],
    "codomain": [burn_pokt_mechanism_space],
    "parameters_used": [],
}
