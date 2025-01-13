from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model(data):
    """
    Trains a Random Forest model using the cleaned data.
    """
    X, y = data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize the Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the model
    model.fit(X_train, y_train)
    
    return model, X_test, y_test

def predict(model, X_test):
    """
    Predicts weather conditions using the trained model.
    """
    return model.predict(X_test)
