from ..Spaces import (service_join_space)

service_join_policy_option_v1 = {"name": "Service Join Policy V1",
                                 "description": "Basic policy option.",
                                 "logic": "If the servicer id is in the supported_services parameter and it is not already present in the system, continue the action chain. Otherwise terminate."
                                 }

service_join_policy = {"name": "Service Join Policy",
                        "description": "The policy which decides whether a service can be added to the system.",
                        "constraints": [],
                        "policy_options": [service_join_policy_option_v1],
                        "domain": [service_join_space],
                        "codomain": [service_join_space],
                        "parameters_used": ["supported_services"]}