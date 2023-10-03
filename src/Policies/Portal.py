from ..Spaces import (portal_relay_request_space, portal_registration_space, modify_portal_pokt_space)

submit_relay_request_portal_policy = {"name": "Submit Relay Request (Portal) Policy",
                        "description": "Policy which handles the logic of portal relay requests and fees",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [portal_relay_request_space],
                        "codomain": [],
                        "parameters_used": ["gateway_bootstrap_unwind_start", "gateway_bootstrap_unwind_end",
                                            "min_bootstrap_gateway_fee_per_relay", "maturity_relay_charge", 
                                            "maturity_relay_cost"]}



portal_registration_policy = {"name": "Portal Registration Policy",
                        "description": "Policy which handles the logic of portal registration and if enough stake is present. The portal is also added to the global state if it is approved.",
                        "constraints": [],
                        "policy_options": [],
                        "domain": [portal_registration_space],
                        "codomain": [modify_portal_pokt_space, modify_portal_pokt_space, portal_registration_space],
                        "parameters_used": ["portal_minimum_stake"]}