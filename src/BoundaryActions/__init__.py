from .Dummy import dummy_boundary_action
from .Servicer import servicer_stake, servicer_pause, servicer_unpause
boundary_actions = {
    "Dummy Boundary Action": dummy_boundary_action,
    "Servicer Stake": servicer_stake,
    "Servicer Pause": servicer_pause,
    "Servicer Unpause": servicer_unpause
}
