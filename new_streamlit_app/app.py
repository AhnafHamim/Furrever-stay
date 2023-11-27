#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import numpy as np

from gradient_boosting_algorithm_11_18 import best_model


def main():
    st.title("Cat Attribute Prediction App")

    # Dropdown menus for cat attributes
    sex = st.selectbox("Sex", ["Male", "Female"])
    size = st.selectbox("Size", ["Kitten", "Adult"])
    # Add more attributes as needed
    # e.g., color = st.selectbox('Color', ['Black', 'White', 'Brown', etc.])

    # Button to make prediction
    if st.button("Predict"):
        # Prepare the data for the model
        data = {"Sex": [sex], "Size": [size]}
        # Add other attributes to the dictionary as well
        # e.g., data['Color'] = [color]

        df = pd.DataFrame(data)

        # Make sure to preprocess the DataFrame 'df' as required by your model
        # For example, you might need to encode categorical variables

        # Make predictions
        prediction = best_model.predict(df)

        # Display the prediction
        st.write(f"Prediction: {prediction}")


if __name__ == "__main__":
    main()
