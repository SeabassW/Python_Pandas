import quandl
import pandas as pd
import pickle 			#default Python pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight') 

api_key = 'cyJUASK__T4JA9s4T1JG'

def state_list():
	fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
	return fiddy_states[0][0][1:]

def grab_initial_state_data():
	states = state_list()
	main_df = pd.DataFrame()

	for abbv in states:
	    query = ("FMAC/HPI_"+str(abbv))
	    df = quandl.get(query, authtoken=api_key)
	    df.columns = [str(abbv)]
	    df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] *100.0

	    if main_df.empty:
	    	main_df = df
	    else:
	    	main_df = main_df.join(df)

	print(main_df.head())

	pickle_out = open('fiddy_states_pctchange2.pickle', 'wb')
	pickle.dump(main_df, pickle_out)
	pickle_out.close()

#grab_initial_state_data()

def HPI_Benchmark():
	df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
	df.rename(columns={'Value': 'United States'}, inplace=True)
	df["United States"] = (df["United States"] - df["United States"][0]) / df["United States"][0] *100.0
	return df


fig = plt.figure()
ax1 = plt.subplot2grid((2,1),(0,0))
ax2 = plt.subplot2grid((2,1),(1,0), sharex=ax1)

#Generate Data
HPI_data = pd.read_pickle('fiddy_states.pickle')


#Rolling averages / Moving average
HPI_data['TX12MA'] = pd.rolling_mean(HPI_data['TX'], 12)
#print(HPI_data[['TX', 'TX12MA']].tail())

#Rolling STD
HPI_data['TX12STD'] = pd.rolling_std(HPI_data['TX'], 12)
print(HPI_data[['TX', 'TX12MA']].head(24))

#Plot Data
HPI_data[['TX', 'TX12MA']].plot(ax = ax1)
HPI_data['TX12STD'].plot(ax = ax2)

#Rolling Correlation
TX_AK_12corr = HPI_data['TX'].rolling(window=12).corr(HPI_data['AK'])

HPI_data['TX'].plot(ax = ax1, label='TX HPI')
HPI_data['AK'].plot(ax = ax1, label='AK HPI')
ax1.legend(loc=4)

TX_AK_12corr.plot(ax = ax2, label = 'TX_AK_12corr')

#Visual Elements
plt.legend(loc=4)
plt.show()
