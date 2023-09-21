from ..Spaces import mint_pokt_mechanism_space


mint_pokt_mechanism = {"name": "Mint POKT Mechanism",
                           "description": "The mechanism which has the treasury minting POKT",
                           "constraints": [],
                           "logic": "The floating supply increases by the POKT amount",
                           "domain": [mint_pokt_mechanism_space],
                           "parameters_used": []}