import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher['cnt']=teacher.drop_duplicates(subset=['teacher_id','subject_id'],keep='first',inplace=True)
    teacher=teacher.groupby(teacher['teacher_id'])['cnt'].size().reset_index()
    return teacher
    
