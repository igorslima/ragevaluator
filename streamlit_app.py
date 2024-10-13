
import streamlit as st

from rag_evaluator import RAGEvaluator

from pymongo import MongoClient


# MongoDB connection setup
client = MongoClient('mongodb+srv://igorslima:xWo6JnXYi2WnG7af@msc-ai-bath.rrx20ab.mongodb.net/?retryWrites=true&w=majority&appName=MSc-AI-Bath')
db = client['user_db']
interactions_collection = db['interactions']

# Initialize the evaluator
evaluator = RAGEvaluator()

# Input data
question = "What are the causes of climate change?"
response = "Climate change is caused by human activities."
reference = "Human activities such as burning fossil fuels cause climate change."

# Evaluate the response
metrics = evaluator.evaluate_all(question, response, reference)

# Print the results
st.write(metrics)
