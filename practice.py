import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': ['kwon', 'park', 'kim', 'choi'],
    'age' : [24, np.nan, 17, 34],
    'class' : [np.nan, np.nan, 1, np.nan]
})

x = df.isnull().sum()
print(x)