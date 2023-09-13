from ..Spaces import portal_registration_space, portal_unregistration_space

portal_registration = {
    "name": "Portal Registration",
    "description": "Registration differs from staking in the sense that the pubKey is known but there are no economic benefits/penalties in this stage of the protocol's progression. The Portal must register on-chain in order for the Servicer to accept its signature as part of the ring. Future versions of the protocol may include on-chain rewards or penalties for the Portal, but the current iteration will incentivize Portals to provide a high quality, highly trusted service through free market economics.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Portal"],
    "codomain": [portal_registration_space],
    "parameters_used": [],
}

portal_unregistration = {
    "name": "Portal Unregistration",
    "description": "A Portal is able to submit an UnstakeMsg to exit and remove itself from the network. After a successful UnstakeMsg, the Portal is no eligible sign relays on behalf of an Application. On-chain delegation from existing Applications will be removed from the world state. After the PortalUnstakingTime unbonding time elapses, the remaining stake is returned to the Portal's address.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Portal"],
    "codomain": [portal_unregistration_space],
    "parameters_used": [],
}


