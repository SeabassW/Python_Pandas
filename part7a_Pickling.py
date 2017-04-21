import quandl
import pandas as pd
import pickle

api_key = 'cyJUASK__T4JA9s4T1JG'
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

#Needs an empty df to be able to fill it later
main_df = pd.DataFrame()

for abbv in fiddy_states[0][0][1:]:
    query = ("FMAC/HPI_"+str(abbv))
    df = quandl.get(query, authtoken=api_key)
    df.columns = [str(abbv)]

    if main_df.empty:
    	main_df = df
    else:
    	main_df = main_df.join(df)

print(main_df.head())

#pickles serializes and saves the bytestream and load it back in
#still has all the attributes. Gets around saving to e.g. .csv to save data

