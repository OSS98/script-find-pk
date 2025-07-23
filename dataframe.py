import pandas as pd 

print('Budget file')
df_budget = pd.read_xml('response5/Budget account entries.xml')
print(df_budget)

print('General file')
df_general = pd.read_xml('response5/General journal.xml')
print(df_general)