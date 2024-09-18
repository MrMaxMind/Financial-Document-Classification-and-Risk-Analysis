from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset
import torch

# Check if CUDA (GPU) is available
device = torch.device('cuda:2' if torch.cuda.is_available() else 'cpu')

# Load the Financial PhraseBank dataset with a specific configuration ('sentences_allagree')
dataset = load_dataset('financial_phrasebank', 'sentences_allagree', split='train', trust_remote_code=True)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Tokenize the dataset
def preprocess_function(examples):
    return tokenizer(examples['sentence'], padding='max_length', truncation=True)

encoded_dataset = dataset.map(preprocess_function, batched=True)

# Load pre-trained BERT model for sequence classification with 3 labels (positive, negative, neutral)
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)

# Move the model to the GPU (if available)
model.to(device)

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=2,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
)

# Trainer class for managing the training loop
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=encoded_dataset,
)

# Train the model
trainer.train()

# Save the fine-tuned model
model.save_pretrained('models')
