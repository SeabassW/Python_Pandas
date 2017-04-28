import numpy as np
import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean
from sklearn import svm, preprocessing, cross_validation
style.use('fivethirtyeight') 

api_key = 'cyJUASK__T4JA9s4T1JG'

def create_labels(cur_hpi, fut_hpi):
	if fut_hpi > cur_hpi:
		return 1
	else:
		return 0

def moving_average(values):
	return mean(values)


housing_data = pd.read_pickle('HPI.pickle')
housing_data = housing_data.pct_change()


housing_data.replace([np.inf, -np.inf], np.nan, inplace=True)
housing_data.dropna(inplace=True)

housing_data['US_HPI_future'] = housing_data['United States'].shift(-1)
#print(housing_data[['US_HPI_future', 'United States']].head())

# Apply function to DataFrame
housing_data['label'] = list(map(create_labels, housing_data['United States'], housing_data['US_HPI_future']))
#print(housing_data.head())

# X = features
# y = labels

X = np.array(housing_data.drop(['US_HPI_future', 'label'], 1))
# Wrap preprocessing around it
X = preprocessing.scale(X)
y = np.array(housing_data['label'])

# Train and test
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))
#print(housing_data.drop(['US_HPI_future', 'label'], 1))