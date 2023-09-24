from ..Spaces import return_servicer_stake_space, servicer_block_reward_space

return_servicer_stake = {
    "name": "Return Servicer Stake",
    "description": """After unstaking, the original stake (i.e. deposit) is returned to the Servicer's custodial account after ServicerUnbondingPeriod has elapsed.""",
    "constraints": [],
    "control_action_options": [],
    "codomain": [return_servicer_stake_space],
    "parameters_used": ["servicer_unbounding_period"],
}

servicer_block_reward = {"name": "Servicer Block Reward",
    "description": "Rewards allocated on a block basis",
    "constraints": [],
    "control_action_options": [],
    "codomain": [servicer_block_reward_space],
    "parameters_used": ["servicer_stake_floor_multiplier", "servicer_stake_weight_ceiling",
                        "servicer_stake_floor_multiplier_exponent", "servicer_stake_weight_multiplier"],}
