from ..Spaces import (service_join_space)

service_transmission_channels = []

service_transmission_channels.append({"origin": "Service Join",
                                        "target": "Service Join Policy",
                                        "space": service_join_space,
                                        "optional": False})