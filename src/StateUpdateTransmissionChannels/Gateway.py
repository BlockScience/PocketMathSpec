gateway_transmission_channels = []

gateway_transmission_channels.append(
    {
        "origin": "Add Gateway Delegator",
        "entity": "Gateway",
        "variable": "Delegators",
        "optional": False,
    }
)

gateway_transmission_channels.append(
    {
        "origin": "Remove Gateway Delegator",
        "entity": "Gateway",
        "variable": "Delegators",
        "optional": False,
    }
)

gateway_transmission_channels.append(
    {
        "origin": "Modify Gateway POKT Holdings",
        "entity": "Gateway",
        "variable": "POKT Holdings",
        "optional": False,
    }
)

gateway_transmission_channels.append(
    {
        "origin": "Modify Gateway Stake",
        "entity": "Gateway",
        "variable": "Staked POKT",
        "optional": False,
    }
)

gateway_transmission_channels.append(
    {
        "origin": "Add New Gateway",
        "entity": "Global",
        "variable": "Gateways",
        "optional": False,
    }
)

gateway_transmission_channels.append(
    {
        "origin": "Update Gateway Stake Status",
        "entity": "Gateway",
        "variable": "Stake Status",
        "optional": False,
    }
)
