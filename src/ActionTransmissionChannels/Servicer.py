from ..Spaces import servicer_stake_space, modify_servicer_pokt_space

servicer_transmission_channels = []

servicer_transmission_channels.append({"origin": "Servicer Stake",
                                        "target": "Servicer Stake Policy",
                                        "space": servicer_stake_space,
                                        "optional": False})

servicer_transmission_channels.append({"origin": "Servicer Stake Policy",
                                        "target": "Set Servicer Parameters Policy",
                                        "space": servicer_stake_space,
                                        "optional": True})

servicer_transmission_channels.append({"origin": "Servicer Stake Policy",
                                        "target": "Modify Servicer POKT Holdings",
                                        "space": modify_servicer_pokt_space,
                                        "optional": True})
servicer_transmission_channels.append({"origin": "Servicer Stake Policy",
                                        "target": "Modify Servicer Stake",
                                        "space": modify_servicer_pokt_space,
                                        "optional": True})


 

