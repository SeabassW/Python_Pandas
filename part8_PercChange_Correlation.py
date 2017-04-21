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


# fig = plt.figure()
# ax1 = plt.subplot2grid((1,1),(0,0))

#Generate Data
HPI_data = pd.read_pickle('fiddy_states_pctchange2.pickle')
# benchmark = HPI_Benchmark()

# #Plot Data
# HPI_data.plot(ax = ax1)
# benchmark.plot(ax = ax1, color='k', linewidth=10)

# #Visual Elements
# plt.legend().remove()
# plt.show()

HPI_State_Correlation = HPI_data.corr()
#print(HPI_State_Correlation)

print(HPI_State_Correlation.describe())