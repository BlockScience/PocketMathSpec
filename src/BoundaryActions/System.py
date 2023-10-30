from ..Spaces import burn_pokt_space

burn_pokt = {
    "name": "Burn POKT",
    "description": "Protocol burning supply of POKT for a discretionary purpose. I.e. one that is decided upon by the DAO.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["DAO"],
    "codomain": [burn_pokt_space],
    "parameters_used": [],
}
