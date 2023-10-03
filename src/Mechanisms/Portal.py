from ..Spaces import application_delegate_to_portal_space, application_undelegation_space, modify_portal_pokt_space


add_portal_delegator = {"name": "Add Portal Delegator",
                           "description": "The mechanism which adds an application that the portal is a delegator for.",
                           "constraints": [],
                           "logic": "Append the application at DOMAIN[0].application_public_key to the delegators attribute for the portal at DOMAIN[0].portal_public_key",
                           "domain": [application_delegate_to_portal_space],
                           "parameters_used": []}

remove_portal_delegator = {"name": "Remove Portal Delegator",
                           "description": "The mechanism which removes an application that the portal is a delegator for.",
                           "constraints": [],
                           "logic": "Remove the application at DOMAIN[0].application_public_key from the delegators attribute for the portal at DOMAIN[0].portal_public_key",
                           "domain": [application_undelegation_space],
                           "parameters_used": []}

modify_portal_pokt_holdings = {"name": "Modify Portal POKT Holdings",
                           "description": "The mechanism to update the personal holdings of a portal",
                           "constraints": [],
                           "logic": "The portal at DOMAIN[0].portal_address has its POKT Holdings modified by DOMAIN[0].value",
                           "domain": [modify_portal_pokt_space],
                           "parameters_used": []}

modify_portal_stake = {"name": "Modify Portal Stake",
                           "description": "The mechanism to update the stake of a portal",
                           "constraints": [],
                           "logic": "The portal at DOMAIN[0].portal_address has its stake modified by DOMAIN[0].value",
                           "domain": [modify_portal_pokt_space],
                           "parameters_used": []}