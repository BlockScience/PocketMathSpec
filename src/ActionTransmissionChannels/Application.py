from ..Spaces import application_stake_space

application_transmission_channels = []

application_transmission_channels.append({"origin": "Application Stake",
                                        "target": "Application Stake Policy",
                                        "space": application_stake_space,
                                        "optional": False})

application_transmission_channels.append({"origin": "Application Stake Policy",
                                        "target": "Set Application Parameters Policy",
                                        "space": application_stake_space,
                                        "optional": False})