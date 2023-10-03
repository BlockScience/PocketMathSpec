from ..Spaces import (service_join_space, service_leave_space)

service_transmission_channels = []

service_transmission_channels.append({"origin": "Service Join",
                                        "target": "Service Join Policy",
                                        "space": service_join_space,
                                        "optional": False})

service_transmission_channels.append({"origin": "Service Join Policy",
                                        "target": "Add New Service",
                                        "space": service_join_space,
                                        "optional": True})

service_transmission_channels.append({"origin": "Service Leave",
                                        "target": "Service Leave Policy",
                                        "space": service_leave_space,
                                        "optional": False})