from .Dummy import dummy_control_action
from .Servicer import assign_servicer_salary
from .Validator import validator_stake_burning

control_actions = {
    "Dummy Control Action": dummy_control_action,
    "Assign Servicer Salary": assign_servicer_salary,
    "Validator Stake Burning": validator_stake_burning
}
