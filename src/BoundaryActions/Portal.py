from ..Spaces import portal_registration_space

portal_registration = {
    "name": "Portal Registration",
    "description": "Action for portals to register themselves.",
    "constraints": [],
    "boundary_action_options": [],
    "called_by": ["Portal"],
    "codomain": [portal_registration_space],
    "parameters_used": [],
}