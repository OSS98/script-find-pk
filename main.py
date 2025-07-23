import pandas as pd


def main():
    print("Hello World!")
    df_budget = pd.read_excel('source/Onward2.xlsx', sheet_name='ONWVTN01')
    potential_primary_keys = []

    df_deduplicated = df_budget.drop_duplicates()
    print(df_deduplicated)
    export_file = 'source/Onward2_deduplicated.xlsx'
    df_deduplicated.to_excel(export_file, index=False)
    print(f"Exported to {export_file}")



if __name__ == "__main__":
    main()