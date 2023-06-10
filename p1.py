import pandas as pd
import numpy as np

id=int(input('enter the id :'))
d = {"emid": pd.Series([id])}
df = pd.DataFrame(d)
print(df)
print(df.describe())
