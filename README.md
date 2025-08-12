# PCA Data Transformation Web App

This project is a **Flask-based web application** that demonstrates **Principal Component Analysis (PCA)** on numeric data.  
It allows the user to input comma-separated numeric values, and outputs their transformation into principal components using a pre-trained PCA model.

---

##  Features
- Trains a simple **PCA** model (default: 3D data reduced to 2 components).
- Web interface for entering numeric vectors.
- Displays transformed PCA components instantly.
- Modern, responsive UI for better usability.
- Fully offline — no external dataset needed.

---

##  Project Structure.
```
├── model.py # Trains the PCA model and saves it as pca_model.pkl
├── app.py # Flask app for web-based PCA transformation
├── templates/
│ └── index.html # User interface (form + results)
├── pca_model.pkl # Saved trained PCA model
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```
---

##  Installation & Setup

1. **Clone the repository**
git clone <your_repo_url>
cd <project_folder>

2. **Install dependencies**
pip install -r requirements.txt



3. **Train the PCA model**
python model.py


This will generate `pca_model.pkl` for use by the web app.

4. **Run the Flask app**
python app.py



5. **Open in your browser**
http://127.0.0.1:5000/



---

## Example Input
For the default PCA model (trained on 3 features), enter:
1, 2, 3


Expected output:
Transformed Data (Principal Components): [ ... two numerical values ... ]



---

## Requirements
Flask
numpy
scikit-learn
joblib



---

## How It Works
1. **model.py**:
   - Creates a sample 3D dataset.
   - Trains a PCA model to reduce from 3 → 2 dimensions.
   - Saves the trained model as `pca_model.pkl`.
   
2. **app.py**:
   - Loads the saved PCA model.
   - Accepts comma-separated numbers through the web form.
   - Transforms the input vector using PCA.
   - Displays the transformed components.

3. **templates/index.html**:
   - Provides a clean, modern, and responsive user interface.
   - Displays results or error messages.

---

## Notes
- Input must match the feature size used to train the PCA model (default: 3 numbers).
- The UI automatically displays results for valid inputs and shows errors for invalid entries.


---

## Screenshot
<img width="1366" height="629" alt="Screenshot 2025-08-12 080809" src="https://github.com/user-attachments/assets/7595e637-efd3-4cad-918f-d03c61a58c9b" />
<img width="1366" height="633" alt="Screenshot 2025-08-12 080824" src="https://github.com/user-attachments/assets/7debd1eb-0c21-4313-86eb-1c213cc4f4a5" />
<img width="1366" height="640" alt="Screenshot 2025-08-12 080835" src="https://github.com/user-attachments/assets/8c3197b0-1493-4de4-b147-8f84c7b62602" />
