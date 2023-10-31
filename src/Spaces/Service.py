from typing import TypedDict

service_join_space = TypedDict(
    "Service Join Space", {"name": str, "gateway_api_prefix": str, "service_id": str}
)
service_leave_space = TypedDict("Service Leave Space", {"service_id": str})
