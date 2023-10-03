from ..Spaces import portal_relay_request_space, portal_registration_space
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
                                        "space": portal_registration_space,
                                        "optional": True})

portal_transmission_channels.append({"origin": "Portal Registration Policy",
                                        "target": "Modify Portal Stake",
                                        "space": portal_registration_space,
                                        "optional": True})