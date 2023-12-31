from ..Spaces import (
    servicer_stake_space,
    modify_servicer_pokt_space,
    servicer_param_update_space,
    servicer_unpause_space,
    servicer_unpause_space2,
    servicer_pause_space,
    servicer_pause_space2,
    servicer_relay_space,
    servicer_stake_burn_space,
    servicer_unstake_space,
    servicer_stake_status_space,
    return_servicer_stake_space,
    modify_gateway_pokt_space,
    modify_application_pokt_space,
    increase_relay_fees_space,
    burn_pokt_mechanism_space,
    jail_node_space,
    unjail_node_space,
    servicer_forced_unstake_space,
    remove_servicer_space,
)

servicer_transmission_channels = []

servicer_transmission_channels.append(
    {
        "origin": "Servicer Stake",
        "target": "Servicer Stake Policy",
        "space": servicer_stake_space,
        "optional": False,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Stake Policy",
        "target": "Set Servicer Parameters Policy",
        "space": servicer_stake_space,
        "optional": True,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Stake Policy",
        "target": "Modify Servicer POKT Holdings",
        "space": modify_servicer_pokt_space,
        "optional": True,
    }
)
servicer_transmission_channels.append(
    {
        "origin": "Servicer Stake Policy",
        "target": "Modify Servicer Stake",
        "space": modify_servicer_pokt_space,
        "optional": True,
    }
)
servicer_transmission_channels.append(
    {
        "origin": "Set Servicer Parameters Policy",
        "target": "Prune Servicer QoS",
        "space": servicer_param_update_space,
        "optional": True,
    }
)
servicer_transmission_channels.append(
    {
        "origin": "Set Servicer Parameters Policy",
        "target": "Update Servicer Params",
        "space": servicer_param_update_space,
        "optional": True,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Unpause",
        "target": "Servicer Unpause Policy",
        "space": servicer_unpause_space,
        "optional": False,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Unpause Policy",
        "target": "Servicer Unpause Mechanism",
        "space": servicer_unpause_space2,
        "optional": True,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Pause",
        "target": "Servicer Pause Policy",
        "space": servicer_pause_space,
        "optional": False,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Pause Policy",
        "target": "Servicer Update Pause Height",
        "space": servicer_pause_space2,
        "optional": True,
    }
)


servicer_transmission_channels.append(
    {
        "origin": "Servicer Relay",
        "target": "Servicer Relay Policy",
        "space": servicer_relay_space,
        "optional": True,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Stake Burn",
        "target": "Servicer Stake Burn Policy",
        "space": servicer_stake_burn_space,
        "optional": False,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Unstake",
        "target": "Servicer Unstake Policy",
        "space": servicer_unstake_space,
        "optional": False,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Unstake Policy",
        "target": "Update Servicer Stake Status",
        "space": servicer_stake_status_space,
        "optional": False,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Return Servicer Stake",
        "target": "Return Servicer Stake Policy",
        "space": return_servicer_stake_space,
        "optional": False,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Return Servicer Stake Policy",
        "target": "Update Servicer Stake Status",
        "space": servicer_stake_status_space,
        "optional": True,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Return Servicer Stake Policy",
        "target": "Modify Servicer POKT Holdings",
        "space": modify_servicer_pokt_space,
        "optional": True,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Return Servicer Stake Policy",
        "target": "Modify Servicer Stake",
        "space": modify_servicer_pokt_space,
        "optional": True,
    }
)


servicer_transmission_channels.append(
    {
        "origin": "Servicer Relay Policy",
        "target": "Modify Gateway Stake",
        "space": modify_gateway_pokt_space,
        "optional": True,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Relay Policy",
        "target": "Modify Application Stake",
        "space": modify_application_pokt_space,
        "optional": True,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Relay Policy",
        "target": "Increase Relay Fees",
        "space": increase_relay_fees_space,
        "optional": False,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Relay Policy",
        "target": "Remove Session",
        "space": servicer_relay_space,
        "optional": True,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Relay Policy",
        "target": "Burn Per Relay Policy",
        "space": servicer_relay_space,
        "optional": False,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Burn Per Relay Policy",
        "target": "Burn POKT Mechanism",
        "space": burn_pokt_mechanism_space,
        "optional": False,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Burn Per Relay Policy",
        "target": "Modify Application Stake",
        "space": modify_application_pokt_space,
        "optional": False,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Jail Node",
        "target": "Jail Node Policy",
        "space": jail_node_space,
        "optional": False,
    }
)


servicer_transmission_channels.append(
    {
        "origin": "Jail Node Policy",
        "target": "Servicer Update Pause Height",
        "space": servicer_pause_space2,
        "optional": True,
    }
)
servicer_transmission_channels.append(
    {
        "origin": "Jail Node Policy",
        "target": "Modify Servicer Stake",
        "space": modify_servicer_pokt_space,
        "optional": True,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Jail Node Policy",
        "target": "Burn POKT Mechanism",
        "space": burn_pokt_mechanism_space,
        "optional": True,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Unjail Node",
        "target": "Unjail Node Policy",
        "space": unjail_node_space,
        "optional": False,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Unjail Node Policy",
        "target": "Servicer Update Pause Height",
        "space": servicer_pause_space2,
        "optional": True,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Forced Unstake",
        "target": "Servicer Forced Unstake Policy",
        "space": servicer_forced_unstake_space,
        "optional": False,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Forced Unstake Policy",
        "target": "Modify Servicer Stake",
        "space": modify_servicer_pokt_space,
        "optional": False,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Forced Unstake Policy",
        "target": "Burn POKT Mechanism",
        "space": burn_pokt_mechanism_space,
        "optional": False,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Forced Unstake Policy",
        "target": "Remove Servicer",
        "space": remove_servicer_space,
        "optional": False,
    }
)

servicer_transmission_channels.append(
    {
        "origin": "Servicer Forced Unstake Policy",
        "target": "Modify Servicer POKT Holdings",
        "space": modify_servicer_pokt_space,
        "optional": True,
    }
)
