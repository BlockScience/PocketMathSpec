from typing import NewType, List

ServiceEntityType = NewType("Service Entity", object)

ApplicationEntityType = NewType("Application Entity", object)
ServicerEntityType = NewType("Servicer Entity", object)
ServicerGroupType = NewType("Servicer Group", List[ServicerEntityType])
WatcherEntityType = NewType("Watcher Entity", object)
GatewayEntityType = NewType("Gateway Entity", object)
ValidatorEntityType = NewType("Validator Entity", object)
DAOEntityType = NewType("DAO Entity", object)
