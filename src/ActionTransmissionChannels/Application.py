from ..Spaces import (
    application_stake_space,
    modify_application_pokt_space,
    application_param_update_space,
    application_delegate_to_gateway_space,
    application_unstake_space,
    application_stake_status_space,
    submit_relay_request_space,
    application_undelegation_space,
    return_application_stake_space,
    burn_pokt_mechanism_space,
)

application_transmission_channels = []

application_transmission_channels.append(
    {
        "origin": "Application Stake",
        "target": "Application Stake Policy",
        "space": application_stake_space,
        "optional": False,
    }
)

application_transmission_channels.append(
    {
        "origin": "Application Stake Policy",
        "target": "Set Application Parameters Policy",
        "space": application_stake_space,
        "optional": False,
    }
)


application_transmission_channels.append(
    {
        "origin": "Application Stake Policy",
        "target": "Modify Application POKT Holdings",
        "space": modify_application_pokt_space,
        "optional": True,
    }
)
application_transmission_channels.append(
    {
        "origin": "Application Stake Policy",
        "target": "Modify Application Stake",
        "space": modify_application_pokt_space,
        "optional": True,
    }
)

application_transmission_channels.append(
    {
        "origin": "Set Application Parameters Policy",
        "target": "Update Application Params",
        "space": application_param_update_space,
        "optional": True,
    }
)


application_transmission_channels.append(
    {
        "origin": "Application Delegate to Gateway",
        "target": "Application Delegate to Gateway Policy",
        "space": application_delegate_to_gateway_space,
        "optional": False,
    }
)

application_transmission_channels.append(
    {
        "origin": "Application Delegate to Gateway Policy",
        "target": "Update Application Delegate",
        "space": application_delegate_to_gateway_space,
        "optional": True,
    }
)

application_transmission_channels.append(
    {
        "origin": "Application Delegate to Gateway Policy",
        "target": "Add Gateway Delegator",
        "space": application_delegate_to_gateway_space,
        "optional": True,
    }
)

application_transmission_channels.append(
    {
        "origin": "Application Unstake",
        "target": "Application Unstake Policy",
        "space": application_unstake_space,
        "optional": False,
    }
)

application_transmission_channels.append(
    {
        "origin": "Application Unstake Policy",
        "target": "Update Application Stake Status",
        "space": application_stake_status_space,
        "optional": False,
    }
)

application_transmission_channels.append(
    {
        "origin": "Submit Relay Request",
        "target": "Submit Relay Request Policy",
        "space": submit_relay_request_space,
        "optional": False,
    }
)

application_transmission_channels.append(
    {
        "origin": "Application Undelegation",
        "target": "Application Undelegate to Gateway Policy",
        "space": application_undelegation_space,
        "optional": False,
    }
)


application_transmission_channels.append(
    {
        "origin": "Application Undelegate to Gateway Policy",
        "target": "Update Application Delegate",
        "space": application_undelegation_space,
        "optional": False,
    }
)

application_transmission_channels.append(
    {
        "origin": "Application Undelegate to Gateway Policy",
        "target": "Remove Gateway Delegator",
        "space": application_undelegation_space,
        "optional": True,
    }
)


application_transmission_channels.append(
    {
        "origin": "Return Application Stake",
        "target": "Return Application Stake Policy",
        "space": return_application_stake_space,
        "optional": False,
    }
)


application_transmission_channels.append(
    {
        "origin": "Return Application Stake Policy",
        "target": "Update Application Stake Status",
        "space": application_stake_space,
        "optional": True,
    }
)

application_transmission_channels.append(
    {
        "origin": "Return Application Stake Policy",
        "target": "Modify Application POKT Holdings",
        "space": modify_application_pokt_space,
        "optional": True,
    }
)

application_transmission_channels.append(
    {
        "origin": "Return Application Stake Policy",
        "target": "Modify Application Stake",
        "space": modify_application_pokt_space,
        "optional": True,
    }
)

application_transmission_channels.append(
    {
        "origin": "Submit Relay Request Policy",
        "target": "Create New Session",
        "space": submit_relay_request_space,
        "optional": True,
    }
)

application_transmission_channels.append(
    {
        "origin": "Submit Relay Request Policy",
        "target": "Burn Per Session Policy",
        "space": submit_relay_request_space,
        "optional": False,
    }
)

application_transmission_channels.append(
    {
        "origin": "Burn Per Session Policy",
        "target": "Burn POKT Mechanism",
        "space": burn_pokt_mechanism_space,
        "optional": False,
    }
)

application_transmission_channels.append(
    {
        "origin": "Burn Per Session Policy",
        "target": "Modify Application Stake",
        "space": modify_application_pokt_space,
        "optional": False,
    }
)
