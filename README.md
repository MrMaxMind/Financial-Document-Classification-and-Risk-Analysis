# **Financial Document Classification & Risk Analysis**

Welcome to the Financial Document Classification & Risk Analysis repository. This project is designed to classify financial documents or stock symbol-based data into different risk categories using a fine-tuned BERT model. Below are instructions for setting up the project, its features, and deployment on Render using Docker.

---

<div align="center">
  <img src="./financial_risk.jpg" alt="Financial Risk Analysis Image" style="border:none;">
</div>

---

## 🚀 **Overview**

This project leverages a pre-trained BERT model fine-tuned for document classification. The model is capable of classifying financial documents or stock symbol-related data into risk categories, providing key insights into the classification. The web app includes a Flask backend, an interactive frontend, and can be deployed using Docker on Render.

---

## ✨ **Features**

- **Text Extraction**: Extracts financial data from stock symbols or uploaded PDF/TXT files.
- **Risk Classification**: Classifies financial documents or data into predefined risk categories using a fine-tuned BERT model.
- **Financial Data Fetching**: Automatically fetches data related to the stock symbol from a free API.
- **User Interface**: Interactive web interface to input stock symbols, text, or upload financial documents.
- **Render Deployment**: Easily deployable on Render using Docker.
- **Key Insights**: Displays key statistics and features that influence the risk classification.

---

## 📂 **Contents**

- `app.py`: Flask backend to handle user inputs, API requests, and return classification results.
- `models/`: Contains `config.json` and `model.safetensors` for the BERT model.
- `templates/index.html`: Frontend HTML for the user interface.
- `static/style.css`: Custom CSS for styling the web interface.
- `static/script.js`: JavaScript for dynamic frontend behavior.
- `financial_model_training.py` : Python Script to train **BERT Model** and save it.
- `requirements.txt`: Python dependencies required to run the project.
- `Dockerfile`: Configuration for containerizing the project.

---

## 🛠️  **Getting Started**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your_username/Financial-Document-Classification.git
   cd Financial-Document-Classification
2. **Install the required packages**:
   Ensure you have Python 3.x installed. Install dependencies by running:
   ```bash
   pip install -r requirements.txt
   
4. **Run the Model Training Script**:
   Train the BERT model and generate `config.json` and `model.safetensors` using the provided Python script:
   ```bash
   python3 financial_model_training.py

5. **Run the Flask App**:
   To start the web app locally:
   ```bash
   python3 app.py
   Open your web browser and go to `http://127.0.0.1:5000/`

---

## 🚢 **Deployment Instructions**

### 1. Model Training: 

Train the **BERT Model** using the provided Python Script `financial_model_training.py` and save the trained model into `models` directory.

### 2. Deploy the App on Render:

- Push your project to GitHub.
- Create a new web service on Render, connecting it to your GitHub repository.
- Ensure app.py is set as the entry point and requirements.txt includes all dependencies.

### 3. Configure the Environment:

- Add the necessary environment variables if required.
- Deploy the app, and Render will automatically start your service.

---

## 🔍 **Key Insights**

- Successfully fine-tuned a BERT model for financial document classification.
- Supports both file uploads and stock symbol input to classify risk.
- Shows key statistics and reasoning behind the risk classification for transparency.
- Deployed on Render using Docker for cloud scalability.

---

## 🛠️ **Tools and Libraries**

- `Flask`: For the web backend.
- `PyTorch`: For loading and running the BERT model.
- `Transformers`: Hugging Face library for fine-tuning and inference.
- `PyPDF2 & pdfminer.six`: For extracting text from PDFs.
- `Alpha Vantage API`: For fetching financial data using stock symbols.
- `HTML, CSS, JavaScript`: For creating the frontend interface.

---

## 🤝 **Contributing**
If you have suggestions or improvements, feel free to open an issue or create a pull request.

---

## ⭐ **Thank You!**

Thank you for visiting! If you find this project useful, please consider starring the repository. Happy coding!

