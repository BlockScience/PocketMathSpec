from typing import NewType, List
ServiceEntityType = NewType('Service Entity', object)

ApplicationEntityType = NewType('Application Entity', object)
ServicerEntityType = NewType('Servicer Entity', object)
ServicerGroupType = NewType("Servicer Group",List[ServicerEntityType])
FishermanEntityType = NewType('Fisherman Entity', object)