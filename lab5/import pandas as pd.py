import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load dataset
df = pd.read_csv(r"C:\Users\PC\Downloads\talabat_enhanced_orders.csv")
# Preview dataset
print(df.head())
print(df.info())

# Basic statistics
print(df.describe())

# Order status distribution
df['Order_Status'].value_counts().plot(kind='bar')
plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Count")
plt.show()

# Feature Engineering
df['Order_Time'] = pd.to_datetime(df['Order_Time'], errors='coerce')
df['Hour'] = df['Order_Time'].dt.hour

# Select features
features = [
    'Quantity',
    'Total_Price',
    'Delivery_Distance_km',
    'Hour'
]

X = df[features]
y = df['Order_Status']

# Handle missing values
X = X.fillna(X.mean())

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Results
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))