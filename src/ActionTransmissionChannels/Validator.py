from ..Spaces import validator_stake_space, modify_validator_pokt_space, validator_param_update_space, validator_unpause_space

validator_transmission_channels = []

validator_transmission_channels.append({"origin": "Validator Stake",
                                        "target": "Validator Stake Policy",
                                        "space": validator_stake_space,
                                        "optional": False})

validator_transmission_channels.append({"origin": "Validator Stake Policy",
                                        "target": "Set Validator Parameters Policy",
                                        "space": validator_stake_space,
                                        "optional": True})

validator_transmission_channels.append({"origin": "Validator Stake Policy",
                                        "target": "Modify Validator Stake",
                                        "space": modify_validator_pokt_space,
                                        "optional": True})

validator_transmission_channels.append({"origin": "Validator Stake Policy",
                                        "target": "Modify Validator POKT Holdings",
                                        "space": modify_validator_pokt_space,
                                        "optional": True})

validator_transmission_channels.append({"origin": "Set Validator Parameters Policy",
                                        "target": "Update Validator Params",
                                        "space": validator_param_update_space,
                                        "optional": True})

validator_transmission_channels.append({"origin": "Validator Unpause",
                                        "target": "Validator Unpause Policy",
                                        "space": validator_unpause_space,
                                        "optional": False})