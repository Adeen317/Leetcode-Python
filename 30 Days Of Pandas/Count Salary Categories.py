import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
        def categorize_salary(salary):
            if salary < 20000:
                return 'Low Salary'
            elif 20000 <= salary <= 50000:
                return 'Average Salary'
            else:
                return 'High Salary'

        # Apply the categorize_salary function to create a new column 'salary_category'
        accounts['category'] = accounts['income'].apply(categorize_salary)

        # Group by 'category' and count the number of occurrences
        result = accounts.groupby('category').size().reset_index(name='accounts_count')

        # If there are no accounts in a category, fill it with 0
        result = result.set_index('category').reindex(['Low Salary', 'Average Salary', 'High Salary'], fill_value=0).reset_index()

        result.sort_values(by='accounts_count',ascending=False)
        return result
            
