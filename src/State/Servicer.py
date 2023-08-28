from ..Types import uPOKTType, ServicerReportCardType

servicer_state = {"name": "Servicer State",
              "notes": "",
              "variables": [{"type": uPOKTType,
                             "name": "Servicer Salary",
                             "description": "A ServicerSalary is assigned to each individual Servicer based on their specific ReportCard, and is distributed every SalaryBlockFrequency",
                             "symbol": None,
                             "domain": None},
                             {"type": ServicerReportCardType,
                             "name": "Servicer Report Card",
                             "description": "The report card used when determing salary for a servicer",
                             "symbol": None,
                             "domain": None}]}
