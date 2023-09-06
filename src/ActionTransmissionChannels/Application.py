from ..Spaces import application_stake_space, modify_application_pokt_space, application_param_update_space

application_transmission_channels = []

application_transmission_channels.append({"origin": "Application Stake",
                                        "target": "Application Stake Policy",
                                        "space": application_stake_space,
                                        "optional": False})

application_transmission_channels.append({"origin": "Application Stake Policy",
                                        "target": "Set Application Parameters Policy",
                                        "space": application_stake_space,
                                        "optional": False})



application_transmission_channels.append({"origin": "Application Stake Policy",
                                        "target": "Modify Application POKT Holdings",
                                        "space": modify_application_pokt_space,
                                        "optional": True})
application_transmission_channels.append({"origin": "Application Stake Policy",
                                        "target": "Modify Application Stake",
                                        "space": modify_application_pokt_space,
                                        "optional": True})

application_transmission_channels.append({"origin": "Set Application Parameters Policy",
                                        "target": "Update Application Params",
                                        "space": application_param_update_space,
                                        "optional": True})


