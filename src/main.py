from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

if __name__ == '__main__':
    cancer = load_breast_cancer()
    X, y = cancer.data, cancer.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=55)

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    joblib.dump(model, 'cancer_knn_model.pkl')
    
    print(f"KNN model training successful! Accuracy: {accuracy:.2%}")