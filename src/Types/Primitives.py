from typing import NewType


# A public key for cryptography
PublicKeyType = NewType('Public Key', str)

# 1*10^6 uPOKT = 1 POKT
uPOKTType = NewType('uPOKT', int)
POKTType = NewType('POKT', int)

# A URL for an api end point
ServiceURLType = NewType('Service URL', str)

RelayChainType = NewType('Relay Chain', str)

# The physical geo-location identifier this Servicer registered in
GeoZoneType = NewType('GeoZone', str)

Days = NewType('GeoZone', int)

AddressType = NewType("Address", int)

#TODO
ServicerReportCardType = NewType('Service Report Card', dict)
ServicerTestScoresType = NewType('Service Test Scores', dict)