import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    lowdf = accounts[accounts['income'] < 20000]
    middf = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)]
    higdf = accounts[accounts['income'] > 50000]

    return pd.DataFrame([['Low Salary', len(lowdf)], ['Average Salary', len(middf)], ['High Salary', len(higdf)]],
                        columns=['category', 'accounts_count'])
-----

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    def categorize_income(income: int) -> str:
        if income < 20000:
            return 'Low Salary'
        elif income <= 50000:
            return 'Average Salary'
        else:
            return 'High Salary'

    accounts['category'] = accounts['income'].apply(categorize_income)
    counts = accounts['category'].value_counts().to_dict()
    all_categories = ['Low Salary', 'Average Salary', 'High Salary']
    result = pd.DataFrame({
        'category': all_categories,
        'accounts_count': [counts.get(cat, 0) for cat in all_categories]
    })

    return result
