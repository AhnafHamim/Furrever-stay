import streamlit as st
from joblib import load
import pandas as pd

# Load your trained model
model = load("use_model.joblib")

def main():
    st.title("Cat Shelter staying Prediction")

    # User inputs through dropdown menus
    color_mapping = {"BLACK": 0, "GRAY": 1, "TABBY": 3, "WHITE": 4, "OTHER": 2}
    condition_mapping = {
        "ILL MILD": 0,
        "ILL SEVERE": 1,
        "INJURED": 2,
        "NORMAL": 3,
        "UNDER WEIGHT": 5,
        "OTHER": 4,
    }

    color = st.selectbox("Color", options=list(color_mapping.keys()))
    condition = st.selectbox("Condition", options=list(condition_mapping.keys()))

    # Use a slider for intake_age
    intake_age = st.slider("Intake Age", min_value=0, max_value=20, value=1)

    if st.button("Predict"):
        # Prepare the input for the model
        input_data = pd.DataFrame(
            {
                "simplified_color_encoded": [color_mapping[color]],
                "simplified_condition_encoded": [condition_mapping[condition]],
                "intake_age": [intake_age],
            }
        )

        # Make the prediction
        prediction = model.predict(input_data)

        # Map predictions to human-readable labels
        prediction_labels = {0: 'staying less than a month', 1: 'staying more than a month'}
        human_readable_prediction = prediction_labels.get(prediction[0], 'Unknown')

        # Determine the color based on the prediction
        text_color = 'red' if prediction[0] == 1 else 'green'
    
        # Display the prediction with colored text using Markdown syntax
        colored_text = f'<span style="color:{text_color}">{human_readable_prediction}</span>'
        st.markdown(f'The model predicts: {colored_text}', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
