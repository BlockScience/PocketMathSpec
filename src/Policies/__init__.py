from .Dummy import dummy_policy
from .Servicer import servicer_stake_policy, set_servicer_parameters_policy, servicer_unpause_policy
policies = {
    "Dummy Policy": dummy_policy,
    "Servicer Stake Policy": servicer_stake_policy,
    "Set Servicer Parameters Policy": set_servicer_parameters_policy,
    "Servicer Unpause Policy": servicer_unpause_policy
}
