from ..Spaces import (
    application_stake_space,
    application_unstake_space,
    application_delegate_to_gateway_space,
    application_undelegation_space,
    submit_relay_request_space,
)

application_stake = {
    "name": "Application Stake",
    "description": "In order to participate as a Application in Pocket Network, each actor is required to bond a certain amount of tokens in escrow while they are consuming the Web3 access. Upon registration, the Application is required to provide information necessary to create applicable Sessions (GeoZone(s), Service(s), etc...).",
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

application_delegate_to_gateway = {
    "name": "Application Delegate to Gateway",
    "description": "An action where the application delegates to a gateway to control their on-chain actions",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Application"],
    "codomain": [application_delegate_to_gateway_space],
    "parameters_used": [],
}

application_undelegation = {
    "name": "Application Undelegation",
    "description": "If a staked Application wants to stop using a Gateway, and prevent the Gateway from further signing relays on its behalf, it would simply submit an on-chain UndelegateMsg. Further relays signed by the Gateway on behalf of the Application would be rejected by the Servicers.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Application"],
    "codomain": [application_undelegation_space],
    "parameters_used": [],
}

submit_relay_request = {
    "name": "Submit Relay Request",
    "description": "An application submits a Relay Request, or an API requests to be routed to any Service",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Application"],
    "codomain": [submit_relay_request_space],
    "parameters_used": [],
}
