from ..Spaces import (service_join_space, service_leave_space)

service_join = {
    "name": "Service Join",
    "description": "Action for Service moving to be added to the system.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Service"],
    "codomain": [service_join_space],
    "parameters_used": [],
}

service_leave = {
    "name": "Service Leave",
    "description": "Action for Service moving to leave the system.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Service"],
    "codomain": [service_leave_space],
    "parameters_used": [],
}