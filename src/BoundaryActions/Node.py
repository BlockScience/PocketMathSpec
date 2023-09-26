from ..Spaces import unjail_node_space

unjail_node = {
    "name": "Unjail Node",
    "description": "Process of a node submitting to be unjailed.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Servicer", "Validator"],
    "codomain": [unjail_node_space],
    "parameters_used": ["downtime_jail_duration"],
}