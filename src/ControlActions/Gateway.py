from ..Spaces import return_gateway_stake_space

return_gateway_stake = {
    "name": "Return Gateway Stake",
    "description": """After unstaking, the original stake (i.e. deposit) is returned to the Gateway's custodial account after an unbounding period has elapsed.""",
    "constraints": [],
    "control_action_options": [],
    "codomain": [return_gateway_stake_space],
    "parameters_used": ["gateway_unstaking_time"],
}
