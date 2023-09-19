from ..Spaces import return_application_stake_space

return_application_stake = {
    "name": "Return Application Stake",
    "description": """After unstaking, the original stake (i.e. deposit) is returned to the Application's custodial account after application_unstaking_time has elapsed.""",
    "constraints": [],
    "control_action_options": [],
    "codomain": [return_application_stake_space],
    "parameters_used": ["application_unstaking_time"],
}