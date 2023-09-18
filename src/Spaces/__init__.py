from .Dummy import dummy_space1, dummy_space2
from .Servicer import (servicer_stake_space, servicer_pause_space, servicer_unpause_space,
                       assign_servicer_salary_space, modify_servicer_pokt_space, servicer_param_update_space, servicer_unstake_space,
                       servicer_unpause_space2, servicer_pause_space2)
from .Application import (application_stake_space, modify_application_pokt_space, application_param_update_space,
                          application_unstake_space, application_delegate_to_portal_space,
                          application_undelegation_space, submit_relay_request_space)
from .Validator import (validator_stake_space, modify_validator_pokt_space, validator_param_update_space,
                        validator_pause_space, validator_stake_burning_space, validator_unstake_space,
                        validator_unpause_space, validator_jail_space, become_validator_space,
                        validator_block_reward_space)
from .Portal import (portal_registration_space, portal_unregistration_space)

spaces = {"Dummy Space 1": dummy_space1,
          "Dummy Space 2": dummy_space2,
          "Servicer Stake Space": servicer_stake_space,
          "Servicer Pause Space": servicer_pause_space,
          "Servicer Pause Space 2": servicer_pause_space2,
          "Servicer Unpause Space": servicer_unpause_space,
          "Assign Servicer Salary Space": assign_servicer_salary_space,
          "Modify Servicer POKT Space": modify_servicer_pokt_space,
          "Servicer Param Update Space": servicer_param_update_space,
          "Servicer Unstake Space": servicer_unstake_space,
          "Application Stake Space": application_stake_space,
          "Servicer Unpause Space 2": servicer_unpause_space2,
          "Modify Application POKT Space": modify_application_pokt_space,
          "Application Param Update Space": application_param_update_space,
          "Application Unstake Space": application_unstake_space,
          "Application Delegate to Portal Space": application_delegate_to_portal_space,
          "Validator Stake Space": validator_stake_space,
          "Modify Validator POKT Space": modify_validator_pokt_space,
          "Validator Param Update Space": validator_param_update_space,
          "Portal Registration Space": portal_registration_space,
          "Portal Unregistration Space": portal_unregistration_space,
          "Application Undelegation Space": application_undelegation_space,
          "Validator Pause Space": validator_pause_space,
          "Validator Stake Burning Space": validator_stake_burning_space,
          "Validator Unstake Space": validator_unstake_space,
          "Validator Unpause Space": validator_unpause_space,
          "Validator Jail Space": validator_jail_space,
          "Become Validator Space": become_validator_space,
          "Validator Block Reward Space": validator_block_reward_space,
          "Submit Relay Request": submit_relay_request_space}



