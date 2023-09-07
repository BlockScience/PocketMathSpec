from .Dummy import dummy_space1, dummy_space2
from .Servicer import (servicer_stake_space, servicer_pause_space, servicer_unpause_space,
                       assign_servicer_salary_space, modify_servicer_pokt_space, servicer_param_update_space, servicer_unstake_space,
                       servicer_unpause_space2)
from .Application import (application_stake_space, modify_application_pokt_space, application_param_update_space,
                          application_unstake_space, application_delegate_to_portal_space)
spaces = {"Dummy Space 1": dummy_space1,
          "Dummy Space 2": dummy_space2,
          "Servicer Stake Space": servicer_stake_space,
          "Servicer Pause Space": servicer_pause_space,
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
          "Application Delegate to Portal Space": application_delegate_to_portal_space}



