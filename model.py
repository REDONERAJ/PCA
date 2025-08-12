import numpy as np
from sklearn.decomposition import PCA
import joblib

def train_pca_model():
    """Trains a simple PCA model and saves it."""
    # Sample data for demonstration
    X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

    # Initialize and fit PCA
    pca = PCA(n_components=2) # Reduce to 2 principal components
    pca.fit(X)

    # Save the trained PCA model
    joblib.dump(pca, 'pca_model.pkl')
    print("PCA model trained and saved as 'pca_model.pkl'")

def load_pca_model():
    """Loads the pre-trained PCA model."""
    return joblib.load('pca_model.pkl')

if __name__ == '__main__':
    train_pca_model()