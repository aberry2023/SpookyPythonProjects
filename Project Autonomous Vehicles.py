import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import wget

# Download the dataset from the Kaggle URL
url = "https://www.kaggle.com/datasets/art12400/2019-autonomous-vehicle-disengagement-reports?select=2019AutonomousVe" \
      "hicleDisengagementReports.csv"
filename = "2019AutonomousVehicleDisengagementReports.csv"
wget.download(url, filename)

# Load the dataset
data = pd.read_csv(filename)

# Split the data into features (X) and target variable (y)
X = data.drop('Manufacturer', axis=1)
y = data['Manufacturer']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest classifier with appropriate parameters
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

