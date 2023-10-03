from ..Spaces import application_delegate_to_portal_space


add_portal_delegator = {"name": "Add Portal Delegator",
                           "description": "The mechanism which adds an application that the portal is a delegator for.",
                           "constraints": [],
                           "logic": "Append the application at DOMAIN[0].application_public_key to the delegators attribute for the portal at DOMAIN[0].portal_public_key",
                           "domain": [application_delegate_to_portal_space],
                           "parameters_used": []}