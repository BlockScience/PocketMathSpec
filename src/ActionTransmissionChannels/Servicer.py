from ..Spaces import servicer_stake_space, modify_servicer_pokt_space, servicer_param_update_space, servicer_unpause_space, servicer_unpause_space2, servicer_pause_space, servicer_pause_space2

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
servicer_transmission_channels.append({"origin": "Set Servicer Parameters Policy",
                                        "target": "Prune Servicer QoS",
                                        "space": servicer_param_update_space,
                                        "optional": True})
servicer_transmission_channels.append({"origin": "Set Servicer Parameters Policy",
                                        "target": "Update Servicer Params",
                                        "space": servicer_param_update_space,
                                        "optional": True})

servicer_transmission_channels.append({"origin": "Servicer Unpause",
                                        "target": "Servicer Unpause Policy",
                                        "space": servicer_unpause_space,
                                        "optional": False})

servicer_transmission_channels.append({"origin": "Servicer Unpause Policy",
                                        "target": "Servicer Unpause Mechanism",
                                        "space": servicer_unpause_space2,
                                        "optional": True})

servicer_transmission_channels.append({"origin": "Servicer Pause",
                                        "target": "Servicer Pause Policy",
                                        "space": servicer_pause_space,
                                        "optional": False})

servicer_transmission_channels.append({"origin": "Servicer Pause Policy",
                                        "target": "Servicer Update Pause Height",
                                        "space": servicer_pause_space2,
                                        "optional": True})
