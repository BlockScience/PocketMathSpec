from .Dummy import dummy_boundary_action
from .Servicer import servicer_stake, servicer_pause, servicer_unpause, servicer_unstake
from .Application import application_stake

boundary_actions = {
    "Dummy Boundary Action": dummy_boundary_action,
    "Servicer Stake": servicer_stake,
    "Servicer Pause": servicer_pause,
    "Servicer Unpause": servicer_unpause,
    "Servicer Unstake": servicer_unstake,
    "Application Stake": application_stake
}
