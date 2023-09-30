from typing import NewType, TypedDict, List
from datetime import datetime

PercentType = NewType('Percent', float)
MillisecondsType = NewType('Percent', int)

# A public key for cryptography
PublicKeyType = NewType('Public Key', str)

# 1*10^6 uPOKT = 1 POKT
uPOKTType = NewType('uPOKT', int)
POKTType = NewType('POKT', int)

USDType = NewType('USD', float)
NumberRelaysPerDayType = NewType('Number of Relays per Day', int)

# A URL for an api end point
ServiceURLType = NewType('Service URL', str)

ServiceType = NewType('Service', str)

# The physical geo-location identifier this Servicer registered in
GeoZoneType = NewType('GeoZone', str)

Days = NewType('GeoZone', int)

AddressType = NewType("Address", int)

BlockHeightType = NewType("Block Height", int)

NanoSecondsType = NewType("Nanoseconds", int)

# Number of blocks
NumberOfBlocksType = NewType("Number of Blocks", int)

ServicerTestScoresType = NewType('Service Test Scores', TypedDict('Service Test Scores', {"sampling_start": datetime,
                                                                                          "total_samples": int,
                                                                                          "null_indices": List[int],
                                                                                          "data_accuracy": PercentType,
                                                                                          "average_latency": MillisecondsType,
                                                                                          "volume": int
                                                                                          }))

# Simple representation of a floating point number between 0-1
# In actual implementation it is going to be a rolling average of test scores
ServicerReportCardType = NewType('Service Report Card', float)

