import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['day'] = employees['event_day']
    employees['total_time'] = (employees['out_time'] - employees['in_time'])
    time=employees.groupby([employees['day'],employees['emp_id']])['total_time'].sum().reset_index()
    return time
