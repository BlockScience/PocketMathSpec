from ..Spaces import (
    gateway_relay_request_space,
    gateway_registration_space,
    modify_gateway_pokt_space,
    gateway_unregistration_space,
    application_undelegation_space,
    gateway_stake_status_space,
    return_gateway_stake_space,
    submit_relay_request_space,
)

gateway_transmission_channels = []

gateway_transmission_channels.append(
    {
        "origin": "Submit Relay Request (Gateway)",
        "target": "Submit Relay Request (Gateway) Policy",
        "space": gateway_relay_request_space,
        "optional": False,
    }
)


gateway_transmission_channels.append(
    {
        "origin": "Gateway Registration",
        "target": "Gateway Registration Policy",
        "space": gateway_registration_space,
        "optional": False,
    }
)

gateway_transmission_channels.append(
    {
        "origin": "Gateway Registration Policy",
        "target": "Modify Gateway POKT Holdings",
        "space": modify_gateway_pokt_space,
        "optional": True,
    }
)

gateway_transmission_channels.append(
    {
        "origin": "Gateway Registration Policy",
        "target": "Modify Gateway Stake",
        "space": modify_gateway_pokt_space,
        "optional": True,
    }
)

gateway_transmission_channels.append(
    {
        "origin": "Gateway Registration Policy",
        "target": "Add New Gateway",
        "space": gateway_registration_space,
        "optional": True,
    }
)

gateway_transmission_channels.append(
    {
        "origin": "Gateway Unregistration",
        "target": "Gateway Unregistration Policy",
        "space": gateway_unregistration_space,
        "optional": False,
    }
)

gateway_transmission_channels.append(
    {
        "origin": "Gateway Unregistration Policy",
        "target": "Update Gateway Stake Status",
        "space": gateway_stake_status_space,
        "optional": True,
    }
)

gateway_transmission_channels.append(
    {
        "origin": "Gateway Unregistration Policy",
        "target": "Remove Gateway Delegator",
        "space": application_undelegation_space,
        "optional": True,
    }
)

gateway_transmission_channels.append(
    {
        "origin": "Return Gateway Stake",
        "target": "Return Gateway Stake Policy",
        "space": return_gateway_stake_space,
        "optional": False,
    }
)

gateway_transmission_channels.append(
    {
        "origin": "Return Gateway Stake Policy",
        "target": "Update Gateway Stake Status",
        "space": gateway_stake_status_space,
        "optional": True,
    }
)

gateway_transmission_channels.append(
    {
        "origin": "Return Gateway Stake Policy",
        "target": "Modify Gateway POKT Holdings",
        "space": modify_gateway_pokt_space,
        "optional": True,
    }
)

gateway_transmission_channels.append(
    {
        "origin": "Return Gateway Stake Policy",
        "target": "Modify Gateway Stake",
        "space": modify_gateway_pokt_space,
        "optional": True,
    }
)

gateway_transmission_channels.append(
    {
        "origin": "Submit Relay Request (Gateway) Policy",
        "target": "Create New Session",
        "space": submit_relay_request_space,
        "optional": True,
    }
)

gateway_transmission_channels.append(
    {
        "origin": "Submit Relay Request (Gateway) Policy",
        "target": "Burn Per Session Policy",
        "space": submit_relay_request_space,
        "optional": False,
    }
)
