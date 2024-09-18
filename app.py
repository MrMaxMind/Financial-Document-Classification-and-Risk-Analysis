import os
import torch
from transformers import BertTokenizer, BertForSequenceClassification, BertConfig
from safetensors.torch import load_file
from flask import Flask, request, jsonify, render_template
import requests
import PyPDF2

app = Flask(__name__)

# Load the tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Load model configuration and weights separately
config = BertConfig.from_json_file('./models/config.json')
model = BertForSequenceClassification(config)

# Load the safetensors model weights
model_weights = load_file('./models/model.safetensors')
model.load_state_dict(model_weights)

# Mapping of predicted labels to meaningful risk types
risk_labels = {
    0: "Low Risk",
    1: "Moderate Risk",
    2: "High Risk"
}

# Function to fetch financial data from a free API using a stock symbol
def get_financial_data_from_symbol(stock_symbol):
    api_key = '73JKP2DKX79NKYO8'
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={stock_symbol}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        key_stats = {
            'P/E Ratio': data.get('PERatio', 'N/A'),
            'Market Cap': data.get('MarketCapitalization', 'N/A'),
            'Debt/Equity': data.get('DebtEquityRatio', 'N/A'),
            'EPS': data.get('EPS', 'N/A'),
        }
        return data.get('Description', ''), key_stats  # Return description and key stats
    else:
        return 'Error fetching financial data.', {}

# Function to process financial data through the model
def process_financial_data(financial_text):
    inputs = tokenizer(financial_text, padding=True, truncation=True, return_tensors='pt')
    model_output = model(**inputs)
    predicted_label = torch.argmax(model_output.logits, dim=1).item()
    return risk_labels[predicted_label]  # Return meaningful risk label

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    stock_symbol = request.form.get('stock_symbol')  # Get stock symbol input

    if stock_symbol:
        # Fetch financial data using a stock symbol and free API
        financial_data, key_stats = get_financial_data_from_symbol(stock_symbol)
        if 'Error' in financial_data:
            return jsonify({"error": "Unable to fetch financial data for the provided stock symbol."}), 400
        # Process the fetched data with the model
        result = process_financial_data(financial_data)
        return jsonify({
            "classification_label": result,
            "key_stats": key_stats
        })

    # If a file is uploaded instead
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file or stock symbol provided."}), 400

    # Save the uploaded file
    file_path = os.path.join('uploads', file.filename)
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    file.save(file_path)

    # Read file content (for txt and pdf handling)
    if file.filename.endswith('.txt'):
        with open(file_path, 'r') as f:
            financial_text = f.read()
    elif file.filename.endswith('.pdf'):
        financial_text = extract_text_from_pdf(file_path)
    else:
        return jsonify({"error": "Unsupported file format."}), 400

    # Process the financial text data through the model
    result = process_financial_data(financial_text)
    return jsonify({"classification_label": result})

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""
    except Exception as e:
        text = f"Error extracting text from PDF: {str(e)}"
    return text

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
