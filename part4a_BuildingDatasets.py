import quandl
import pandas as pd

#Use HPI from Freddie Mac on Quandl
api_key = 'cyJUASK__T4JA9s4T1JG'

#read Quandl API to get HPI from Alaska
df = quandl.get('FMAC/HPI_AK', authtoken=api_key)
#print(df.head())

#get 50 states from Wikipedia
#fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

#this is a list:
#print(fiddy_states)

#this is a dataframe:
#print(fiddy_states[0])

#this is a column:
#print(fiddy_states[0][0])

#for abbv in fiddy_states[0][0][1:]:
	#print("FMAC/HPI_"+str(abbv))

#get 50 states list from webpage other than Wikipedia
#http://www.50states.com/abbreviations.htm

fifty_states = pd.read_html('http://www.50states.com/abbreviations.htm')
#print(fifty_states[0][1][1:51])

for abbv in fifty_states[0][1][1:51]:
	print("FMAC/HPI_+" + str(abbv))