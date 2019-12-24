import numpy as np
import pandas as pd

import pandas as pd
import numpy as np

df = pd.DataFrame({'Type': list('ABBC'), 'Set': list('ZZXY')})
df['Type2'] = df['Type']
B = ['B', 'BB']
D = ['D', 'DD']
df2 = df.replace({'Type': {}})
# df.replace({'a' : { 'Medium' : 2, 'Small' : 1, 'High' : 3 }})

# cols = df.columns.tolist()
# cols = cols[-1:] + cols[:-1]
# df = df[cols]
# print(df)
print(df2)
# print(cols)
