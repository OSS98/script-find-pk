from itertools import combinations


def find_unique_combinations(df, cols):
    for r in range(1, len(cols) + 1):
        for combo in combinations(cols, r):
            # print(f"Checking combination: {combo}")

            # Create a combined key based on selected columns
            combined_key = df[list(combo)].apply(tuple, axis=1)
            print(combined_key)
            print(combined_key.nunique())

            # Check if the combination of columns is unique
            if combined_key.nunique() == len(df):
                print(f"Unique combination: {combo}")
                
    print("End of search")