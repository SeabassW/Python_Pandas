import quandl
import pandas as pd
import pickle 			#default Python pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight') 

# Remove bad datapoints
bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}
df = pd.DataFrame(bridge_height)

# Use the STD
df['STD'] = df['meters'].rolling(window=2, center=False).std()
#print(df['STD'])

df_std = df.describe()['meters']['std']
#print(df_std)

# Remove bad datapoint with comparison operator
df = df[ (df['STD'] < df_std) ]
print(df)

# df.plot()
# plt.show()
