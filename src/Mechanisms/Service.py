from ..Spaces import (service_join_space)


add_new_service = {"name": "Add New Service",
                           "description": "Create a new service entity from the message and add it to the global state",
                           "constraints": [],
                           "logic": "DOMAIN[0] is used to create the new service and then it is appended to the global state's services.",
                           "domain": [service_join_space],
                           "parameters_used": []}