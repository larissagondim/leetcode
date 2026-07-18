import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    condition = (~employees['name'].str.startswith('M')) & (employees['employee_id'] % 2 != 0)
    employees['bonus'] = 0
    employees.loc[condition, 'bonus'] = employees.loc[condition, 'salary']
    return employees[['employee_id', 'bonus']].sort_values('employee_id')
    