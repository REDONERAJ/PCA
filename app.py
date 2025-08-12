from flask import Flask, render_template, request
import numpy as np
from model import load_pca_model

app = Flask(__name__)

# Load the PCA model when the app starts
pca_model = load_pca_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transform', methods=['POST'])
def transform_data():
    try:
        data_str = request.form['data_input']
        # Convert comma-separated string to a list of floats
        input_data = [float(x.strip()) for x in data_str.split(',')]
        
        # Ensure input data has the correct number of features for transformation
        # (This example assumes 3 features as per model.py's training data)
        if len(input_data) != 3:
            return render_template('index.html', error="Input data must have 3 comma-separated numbers.")

        # Reshape for PCA transformation (single sample)
        input_array = np.array(input_data).reshape(1, -1)
        
        transformed_data = pca_model.transform(input_array)
        
        return render_template('index.html', 
                               original_data=data_str, 
                               transformed_data=transformed_data[0])
    except ValueError:
        return render_template('index.html', error="Invalid input. Please enter comma-separated numbers.")
    except Exception as e:
        return render_template('index.html', error=f"An error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True)