from ..Spaces import (
    return_servicer_stake_space,
    servicer_block_reward_space,
    servicer_stake_burn_space,
    servicer_forced_unstake_space,
)

return_servicer_stake = {
    "name": "Return Servicer Stake",
    "description": """After unstaking, the original stake (i.e. deposit) is returned to the Servicer's custodial account after ServicerUnbondingPeriod has elapsed.""",
    "constraints": [],
    "control_action_options": [],
    "codomain": [return_servicer_stake_space],
    "parameters_used": ["servicer_unbounding_period"],
}

servicer_stake_burn = {
    "name": "Servicer Stake Burn",
    "description": """The control action for a servicer having their stake burned due to bad behavior.

A Servicer's stake can be burnt in two situations:

1. A Servicer receives a TestScore below the TestScoreBurnThreshold
2. A Watcher initiates a PauseMsg with the required evidence

If a Service Node stake falls below the minimum amount through serving incorrect data or incorrect block validation, 20% of the minimum stake for that Service Node will be slashed and jailed. If a Service Node submits a fraudulent Relay batch, 100% of their stake will be slashed.""",
    "constraints": [],
    "control_action_options": [],
    "codomain": [servicer_stake_burn_space],
    "parameters_used": [],
}

servicer_forced_unstake = {
    "name": "Servicer Forced Unstake",
    "description": """After reaching MaxJailedBlocks, a servicer will be force unstaked which will result in a node’s entire stake being slashed.""",
    "constraints": [],
    "control_action_options": [],
    "codomain": [servicer_forced_unstake_space],
    "parameters_used": ["max_jailed_blocks"],
}
