from ..Spaces import return_portal_stake_space

return_portal_stake = {
    "name": "Return Portal Stake",
    "description": """After unstaking, the original stake (i.e. deposit) is returned to the Portal's custodial account after an unbounding period has elapsed.""",
    "constraints": [],
    "control_action_options": [],
    "codomain": [return_portal_stake_space],
    "parameters_used": ["portal_unstaking_time"],
}