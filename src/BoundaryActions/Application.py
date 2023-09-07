from ..Spaces import application_stake_space, application_unstake_space

application_stake = {
    "name": "Application Stake",
    "description": "In order to participate as a Application in Pocket Network, each actor is required to bond a certain amount of tokens in escrow while they are consuming the Web3 access. Upon registration, the Application is required to provide information necessary to create applicable Sessions (GeoZone(s), RelayChain(s), etc...).",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Application"],
    "codomain": [application_stake_space],
    "parameters_used": [],
}

application_unstake = {
    "name": "Application Unstake",
    "description": "The action of unstaking from the network for an application",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Application"],
    "codomain": [application_unstake_space],
    "parameters_used": [],
}