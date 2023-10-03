from ..Spaces import (service_join_space, service_leave_space)


add_new_service = {"name": "Add New Service",
                           "description": "Create a new service entity from the message and add it to the global state",
                           "constraints": [],
                           "logic": "DOMAIN[0] is used to create the new service and then it is appended to the global state's services.",
                           "domain": [service_join_space],
                           "parameters_used": []}

remove_service = {"name": "Remove Service",
                           "description": "Mechanism which removes services",
                           "constraints": [],
                           "logic": "The service in DOMAIN[0] is removed.",
                           "domain": [service_leave_space],
                           "parameters_used": []}