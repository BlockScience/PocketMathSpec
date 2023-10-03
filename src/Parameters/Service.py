from ..Types import ServiceIDType
from typing import List

service_parameter_set = {"name": "Service Parameter Set",
                       "notes": "",
                       "parameters": [{"variable_type": List[ServiceIDType],
                                       "name": "supported_services",
                                       "description": "The services that governance has voted to allow.",
                                       "symbol": None,
                                       "domain": None
                                       },]}





