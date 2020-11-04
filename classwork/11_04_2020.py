import pandas as pd

df = pd.read_csv(r"election_candidate.csv", skiprows=1)  # use leading r to declare string as literal (to parse slashes literally)

pd.set_option("display.max_rows", 10)
pd.set_option("display.max_columns", 10)

df = df.rename(columns={"Election: (United States)": "Election"})  # override with mapping

print(df.iloc[0])  # print row 0
print(df.iloc[-1])  # print row from end

print(df.iloc[0:5, 1:2])  # indexes 0-5, columns 1 and 2

df.fillna(value = 0)  # fill N/A values with provided

left = pd.DataFrame({"col": ["value", "value"], "col2": [1, 2]})  # create columns with values
right = pd.DataFrame({"col": ["value", "value"], "col3": ["another", "value"]})
merge = pd.merge(left, right)  # merge on matching cols
print(merge)

import numpy as np

print(
    pd.DataFrame({"col": [1, 2, 3, 4, 5], "value": np.random.randint(5)})
)

