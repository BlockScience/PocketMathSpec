from ..Spaces import (relay_chain_join_space, relay_chain_leave_space)

relay_chain_join = {
    "name": "Relay Chain Join",
    "description": "Action for relay chain moving to be added to the system.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Relay Chain"],
    "codomain": [relay_chain_join_space],
    "parameters_used": [],
}

relay_chain_leave = {
    "name": "Relay Chain Leave",
    "description": "Action for relay chain moving to leave the system.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Relay Chain"],
    "codomain": [relay_chain_leave_space],
    "parameters_used": [],
}