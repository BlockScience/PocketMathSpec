from ..Spaces import mint_pokt_mechanism_space, burn_pokt_mechanism_space


mint_pokt_mechanism = {"name": "Mint POKT Mechanism",
                           "description": "The mechanism which has the treasury minting POKT",
                           "constraints": [],
                           "logic": "The floating supply increases by the POKT amount",
                           "domain": [mint_pokt_mechanism_space],
                           "parameters_used": []}

burn_pokt_mechanism = {"name": "Burn POKT Mechanism",
                           "description": "The mechanism which has the treasury burning POKT",
                           "constraints": [],
                           "logic": "The floating supply decreases by the POKT amount",
                           "domain": [burn_pokt_mechanism_space],
                           "parameters_used": []}