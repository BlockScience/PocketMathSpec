from ..Spaces import (portal_relay_request_space, portal_registration_space, modify_portal_pokt_space,
                      portal_unregistration_space, application_undelegation_space, portal_stake_status_space,
                      return_portal_stake_space)
portal_transmission_channels = []

portal_transmission_channels.append({"origin": "Submit Relay Request (Portal)",
                                        "target": "Submit Relay Request (Portal) Policy",
                                        "space": portal_relay_request_space,
                                        "optional": False})


portal_transmission_channels.append({"origin": "Portal Registration",
                                        "target": "Portal Registration Policy",
                                        "space": portal_registration_space,
                                        "optional": False})

portal_transmission_channels.append({"origin": "Portal Registration Policy",
                                        "target": "Modify Portal POKT Holdings",
                                        "space": modify_portal_pokt_space,
                                        "optional": True})

portal_transmission_channels.append({"origin": "Portal Registration Policy",
                                        "target": "Modify Portal Stake",
                                        "space": modify_portal_pokt_space,
                                        "optional": True})

portal_transmission_channels.append({"origin": "Portal Registration Policy",
                                        "target": "Add New Portal",
                                        "space": portal_registration_space,
                                        "optional": True})

portal_transmission_channels.append({"origin": "Portal Unregistration",
                                        "target": "Portal Unregistration Policy",
                                        "space": portal_unregistration_space,
                                        "optional": False})

portal_transmission_channels.append({"origin": "Portal Unregistration Policy",
                                        "target": "Update Portal Stake Status",
                                        "space": portal_stake_status_space,
                                        "optional": True})

portal_transmission_channels.append({"origin":  "Portal Unregistration Policy",
                                        "target": "Remove Portal Delegator",
                                        "space": application_undelegation_space,
                                        "optional": True})

portal_transmission_channels.append({"origin":  "Return Portal Stake",
                                        "target": "Return Portal Stake Policy",
                                        "space": return_portal_stake_space,
                                        "optional": False})

