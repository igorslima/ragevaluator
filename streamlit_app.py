import streamlit as st
from rag_evaluator import RAGEvaluator
from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient('mongodb+srv://igorslima:xWo6JnXYi2WnG7af@msc-ai-bath.rrx20ab.mongodb.net/?retryWrites=true&w=majority&appName=MSc-AI-Bath')
db = client['user_db']
interactions_collection = db['interactions']

# Initialize the evaluator
evaluator = RAGEvaluator()

# Create a text input for the username
username = st.text_input("Enter the username for validation")

# Validate if the username is provided
if username:
    # Fetch interactions for the specified username
    interactions = interactions_collection.find({"username": username})

    if interactions.count() > 0:
        # Iterate through each interaction and evaluate it
        for interaction in interactions:
            # Extract fields from each document
            question = interaction.get('question', '')
            answer = interaction.get('answer', '')
            
            # Concatenate response1, response2, and response3 to create the reference
            response1 = interaction.get('response1', '')
            response2 = interaction.get('response2', '')
            response3 = interaction.get('response3', '')
            
            reference = f"{response1} {response2} {response3}".strip()

            # Evaluate the response if all necessary data is present
            if question and answer and reference:
                metrics = evaluator.evaluate_all(question, answer, reference)
                
                # Display the metrics for each interaction
                st.write(f"Metrics for question: {question}")
                st.write(f"Answer from chatbot: {answer}")
                st.write(metrics)
            else:
                st.write(f"Missing data for interaction: {interaction['_id']}")
    else:
        st.write("No interactions found for this username.")
else:
    st.write("Please enter a username to start the evaluation.")

# Close the MongoDB connection
client.close()
