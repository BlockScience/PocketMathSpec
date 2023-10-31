from ..Types import POKTType, NumberOfBlocksType

gateway_parameter_set = {
    "name": "Gateway Parameter Set",
    "notes": "",
    "parameters": [
        {
            "variable_type": POKTType,
            "name": "stake_per_app_delegation",
            "description": "The amount of stake needed per application that is delegating to the gateway.",
            "symbol": None,
            "domain": None,
        },
        {
            "variable_type": POKTType,
            "name": "gateway_fee_per_relay",
            "description": "The fee per relay to gateways.",
            "symbol": None,
            "domain": None,
        },
        {
            "variable_type": POKTType,
            "name": "gateway_minimum_stake",
            "description": "The minimum stake for the gateway, starting at 150,000 POKT.",
            "symbol": None,
            "domain": None,
        },
        {
            "variable_type": NumberOfBlocksType,
            "name": "gateway_unstaking_time",
            "description": "The time before a gateway has their stake returned.",
            "symbol": None,
            "domain": None,
        },
    ],
}
