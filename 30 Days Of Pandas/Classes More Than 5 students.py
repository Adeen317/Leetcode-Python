import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    course=courses.groupby('class').filter(lambda x: len(x['student']) >= 5)
    course=course.drop_duplicates(subset='class',keep='first')

    return course[['class']]
