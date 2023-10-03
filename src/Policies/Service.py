from ..Spaces import (service_join_space)

service_join_policy = {"name": "Service Join Policy",
                        "description": "The policy which decides whether a service can be added to the system.",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [service_join_space],
                        "codomain": [service_join_space],
                        "parameters_used": ["supported_services"]}