import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load the sample file
df = pd.read_csv("C:\\Users\\13139\\PycharmProjects\\pythonProject\\pythonProject\\PastTraffic.csv")

# Display the head of the DataFrame
print(df.head())

# Convert categorical values to numeric
d = {'Y':1, 'N':0}
df['Normal?'] = df['Normal?'].map(d)

# Display the modified DataFrame
print(df.head())

# Selected and target columns, respectively
selected_columns = ['TTL', 'Hops']
X = df[selected_columns]
y = df['Normal?']

# Construct the decision tree
clf = DecisionTreeClassifier()
clf.fit(X, y)