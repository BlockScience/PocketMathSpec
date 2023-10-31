from ..Spaces import (
    application_delegate_to_gateway_space,
    application_undelegation_space,
    modify_gateway_pokt_space,
    gateway_registration_space,
    gateway_stake_status_space,
)


add_gateway_delegator = {
    "name": "Add Gateway Delegator",
    "description": "The mechanism which adds an application that the gateway is a delegator for.",
    "constraints": [],
    "logic": "Append the application at DOMAIN[0].application_public_key to the delegators attribute for the gateway at DOMAIN[0].gateway_public_key",
    "domain": [application_delegate_to_gateway_space],
    "parameters_used": [],
}

remove_gateway_delegator = {
    "name": "Remove Gateway Delegator",
    "description": "The mechanism which removes an application that the gateway is a delegator for.",
    "constraints": [],
    "logic": "Remove the application at DOMAIN[0].application_public_key from the delegators attribute for the gateway at DOMAIN[0].gateway_public_key",
    "domain": [application_undelegation_space],
    "parameters_used": [],
}

modify_gateway_pokt_holdings = {
    "name": "Modify Gateway POKT Holdings",
    "description": "The mechanism to update the personal holdings of a gateway",
    "constraints": [],
    "logic": "The gateway at DOMAIN[0].gateway_address has its POKT Holdings modified by DOMAIN[0].value",
    "domain": [modify_gateway_pokt_space],
    "parameters_used": [],
}

modify_gateway_stake = {
    "name": "Modify Gateway Stake",
    "description": "The mechanism to update the stake of a gateway",
    "constraints": [],
    "logic": "The gateway at DOMAIN[0].gateway_address has its stake modified by DOMAIN[0].value",
    "domain": [modify_gateway_pokt_space],
    "parameters_used": [],
}

add_new_gateway = {
    "name": "Add New Gateway",
    "description": "The mechanism for adding a new gateway to the global state",
    "constraints": [],
    "logic": "The gateway at DOMAIN[0].gateway_address is added to the global state",
    "domain": [gateway_registration_space],
    "parameters_used": [],
}

update_gateway_stake_status = {
    "name": "Update Gateway Stake Status",
    "description": "The mechanism for updating gateway stake status",
    "constraints": [],
    "logic": "The gateway at DOMAIN[0].gateway_address has its stake status updated to DOMAIN[0].status",
    "domain": [gateway_stake_status_space],
    "parameters_used": [],
}
