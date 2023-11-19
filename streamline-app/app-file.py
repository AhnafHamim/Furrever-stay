#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st
import pandas as pd
import numpy as np
from gradient_boosting_algorithm_11_18 import best_model
    
# Function to load and preprocess the dataset
def load_and_preprocess_data(file):
    try:
        # Attempt to read the CSV file
        df = pd.read_csv(file)

        # You need to adjust the following line based on your actual column names
        X = df[independent_variables]
        return X

    except pd.errors.EmptyDataError:
        # Handle the case where the file is empty
        st.error("The uploaded file is empty. Please upload a valid CSV file.")
        return None

# Function to make predictions using the trained model
def make_predictions(model, data):
    return np.round(model.predict(data))  # Adjust as needed

# Streamlit app
def main():
    st.title("Model Prediction App")

    # File upload
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        st.write("### Uploaded CSV file:")
        st.write(pd.read_csv(uploaded_file))
        
        # Print the content of the file
        st.write("### File Content:")
        st.write(uploaded_file.getvalue())
        
        # Load and preprocess data
        data = load_and_preprocess_data(uploaded_file)

        # Load the trained model
        st.write("### Using trained model for predictions")
        predictions = make_predictions(best_model, data)

        # Display predictions
        st.write("### Model Predictions:")
        st.write(predictions)

        # Save predictions to CSV file
        predictions_df = pd.DataFrame({'Predicted': predictions})
        st.write("### Saving predictions to CSV file:")
        st.write(predictions_df)

        # Save the predictions to a CSV file
        predictions_df.to_csv('predictions_output.csv', index=False)

if __name__ == "__main__":
    main()


# In[ ]:




