portal_transmission_channels = []

portal_transmission_channels.append({"origin": "Add Portal Delegator",
                                     "entity": "Portal",
                                     "variable": "Delegators",
                                     "optional": False})

portal_transmission_channels.append({"origin": "Remove Portal Delegator",
                                     "entity": "Portal",
                                     "variable": "Delegators",
                                     "optional": False})

portal_transmission_channels.append({"origin": "Modify Portal POKT Holdings",
                                     "entity": "Portal",
                                     "variable": "POKT Holdings",
                                     "optional": False})

portal_transmission_channels.append({"origin": "Modify Portal Stake",
                                     "entity": "Portal",
                                     "variable": "Staked POKT",
                                     "optional": False})

portal_transmission_channels.append({"origin": "Add New Portal",
                                     "entity": "Global",
                                     "variable": "Portals",
                                     "optional": False})

portal_transmission_channels.append({"origin": "Update Portal Stake Status",
                                     "entity": "Portal",
                                     "variable": "Stake Status",
                                     "optional": False})