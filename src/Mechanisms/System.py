from ..Spaces import (
    mint_pokt_mechanism_space,
    burn_pokt_mechanism_space,
    increase_relay_fees_space,
    decrease_relay_fees_space,
)


mint_pokt_mechanism = {
    "name": "Mint POKT Mechanism",
    "description": "The mechanism which has the protocol minting POKT",
    "constraints": [],
    "logic": "The floating supply increases by the POKT amount",
    "domain": [mint_pokt_mechanism_space],
    "parameters_used": [],
}

burn_pokt_mechanism = {
    "name": "Burn POKT Mechanism",
    "description": "The mechanism which has the protocl burning POKT",
    "constraints": [],
    "logic": "The floating supply decreases by the POKT amount",
    "domain": [burn_pokt_mechanism_space],
    "parameters_used": [],
}

increase_relay_fees = {
    "name": "Increase Relay Fees",
    "description": "The mechanism which tracks the relay fees",
    "constraints": [],
    "logic": "The relay fees increase by the POKT amount",
    "domain": [increase_relay_fees_space],
    "parameters_used": [],
}

decrease_relay_fees = {
    "name": "Decrease Relay Fees",
    "description": "The mechanism which disburses the relay fees collected",
    "constraints": [],
    "logic": "The relay fees decrease by the POKT amount",
    "domain": [decrease_relay_fees_space],
    "parameters_used": [],
}
