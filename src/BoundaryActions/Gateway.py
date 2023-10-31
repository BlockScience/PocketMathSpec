from ..Spaces import (
    gateway_registration_space,
    gateway_unregistration_space,
    gateway_relay_request_space,
)

gateway_registration = {
    "name": "Gateway Registration",
    "description": "Registration differs from staking in the sense that the pubKey is known but there are no economic benefits/penalties in this stage of the protocol's progression. The Gateway must register on-chain in order for the Servicer to accept its signature as part of the ring. Future versions of the protocol may include on-chain rewards or penalties for the Gateway, but the current iteration will incentivize Gateways to provide a high quality, highly trusted service through free market economics.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Gateway"],
    "codomain": [gateway_registration_space],
    "parameters_used": [],
}

gateway_unregistration = {
    "name": "Gateway Unregistration",
    "description": "A Gateway is able to submit an UnstakeMsg to exit and remove itself from the network. After a successful UnstakeMsg, the Gateway is no eligible sign relays on behalf of an Application. On-chain delegation from existing Applications will be removed from the world state. After the GatewayUnstakingTime unbonding time elapses, the remaining stake is returned to the Gateway's address.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Gateway"],
    "codomain": [gateway_unregistration_space],
    "parameters_used": [],
}

submit_relay_request_gateway = {
    "name": "Submit Relay Request (Gateway)",
    "description": "Gateway submitting a relay request on behalf of an application.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Gateway"],
    "codomain": [gateway_relay_request_space],
    "parameters_used": [],
}
