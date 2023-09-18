from ..Spaces import (burn_pokt_space)

burn_pokt = {
    "name": "Burn POKT",
    "description": "Treasury burning supply of POKT",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Treasury"],
    "codomain": [burn_pokt_space],
    "parameters_used": [],
}