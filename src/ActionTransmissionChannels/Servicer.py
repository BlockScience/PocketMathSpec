from ..Spaces import servicer_stake_space

servicer_transmission_channels = []

servicer_transmission_channels.append({"origin": "Servicer Stake",
                                        "target": "Servicer Stake Policy",
                                        "space": servicer_stake_space,
                                        "optional": False})