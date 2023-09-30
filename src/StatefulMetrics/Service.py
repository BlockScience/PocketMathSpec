from ..Types import ServicerGroupType

service_stateful_metric = {"name": "Service Stateful Metrics",
                           "notes": "",
                           "metrics": [{"type": ServicerGroupType,
                                        "name": "servicers",
                                        "description": "Servicers which are members on this service. It can be found by iterating over the servicers and seeing which ones have a given service in their services array.",
                                        "variables_used": [],
                                        "parameters_used": [],
                                        "symbol": None,
                                        "domain": None}]}