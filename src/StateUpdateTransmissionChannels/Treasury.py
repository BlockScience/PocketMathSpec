treasury_transmission_channels = []

treasury_transmission_channels.append({"origin": "Mint POKT Mechanism",
                                     "entity": "Treasury",
                                     "variable": "Floating Supply",
                                     "optional": False})

treasury_transmission_channels.append({"origin": "Burn POKT Mechanism",
                                     "entity": "Treasury",
                                     "variable": "Floating Supply",
                                     "optional": False})

treasury_transmission_channels.append({"origin": "Increase Relay Fees",
                                     "entity": "Treasury",
                                     "variable": "Relay Fees",
                                     "optional": False})