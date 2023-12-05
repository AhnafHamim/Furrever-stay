
import streamlit as st
from joblib import load
import pandas as pd

# Load both trained models (replace these lines with actual model loading)
model1 = load("use_model.joblib")  # Model for >30 days or not
model2 = load("gb_model.joblib")   # Model for quantitative prediction

def main():
    st.title("Cat Shelter Staying Prediction - Dual Models")

    # Create tabs for each model
    tab1, tab2 = st.tabs(["Model 1: >30 Days Prediction", "Model 2: Quantitative Prediction"])

    with tab1:
        st.header("Model 1: Predicting Greater or Less than 30 Days")
        # Inputs and prediction for model 1
        color_mapping1 = {"BLACK": 0, "GRAY": 1, "TABBY": 3, "WHITE": 4, "OTHER": 2}
        condition_mapping1 = {
        "ILL MILD": 0,
        "ILL SEVERE": 1,
        "INJURED": 2,
        "NORMAL": 3,
        "UNDER WEIGHT": 5,
        "OTHER": 4,
        }

        color1 = st.selectbox("Color", options=list(color_mapping1.keys()))
        condition1 = st.selectbox("Condition", options=list(condition_mapping1.keys()))

        # Use a slider for intake_age
        intake_age1 = st.slider("Intake Age", min_value=0, max_value=20, value=1, key="slider1")

        if st.button("Predict", key="button1"):
            # Prepare the input for the model
            input_data = pd.DataFrame(
                {
                    "simplified_color_encoded": [color_mapping1[color1]],
                    "simplified_condition_encoded": [condition_mapping1[condition1]],
                    "intake_age": [intake_age1],
                }
            )

            # Make the prediction
            prediction = model1.predict(input_data)

            # Map predictions to human-readable labels
            prediction_labels = {
                0: "staying less than a month",
                1: "staying more than a month",
            }
            human_readable_prediction = prediction_labels.get(prediction[0], "Unknown")

            # Determine the color based on the prediction
            text_color = "red" if prediction[0] == 1 else "green"

            # Display the prediction with colored text using Markdown syntax
            colored_text = (
                f'<span style="color:{text_color};font-size:35px">The model predicts: {human_readable_prediction}</span>'
            )
            st.markdown(f"{colored_text}", unsafe_allow_html=True)

    with tab2:
        st.header("Model 2: Quantitative Stay Duration Prediction")
        # Inputs and prediction for model 2
        color_mapping2 = {'BLACK': 0, 'BLACK_N_WHITE': 1, 'BRN_TABBY': 2, 'GRAY': 3, 'GRAY_N_WHITE': 4, 'GRAY_TABBY': 5, 'MIX': 6, 'ORG_TABBY': 7, 'OTHER': 8, 'OTHER_TABBY': 9, 'TORTIE': 10}
        condition_mapping2 = {'HEALTHY': 0, 'ILL': 1, 'OTHER': 2}    
        type_mapping2 = {'OTHER': 0, 'OWNER SURRENDER': 1, 'STRAY': 2}

        color2 = st.selectbox("Color", options=list(color_mapping2.keys()))
        type2 = st.selectbox("Type", options=list(type_mapping2.keys()))
        condition2 = st.selectbox("Condition", options=list(condition_mapping2.keys()))

        # Use a slider for intake_age
        intake_age2 = st.slider("Intake Age", min_value=0, max_value=20, value=1, key="slider2")
        
        if st.button("Predict",key="button2"):
                # Prepare the input for the model
            input_data = pd.DataFrame(
                {
                    "intake_age": [intake_age2],
                    "simplified_condition_encoded": [condition_mapping2[condition2]],
                    "simplified_type_encoded":[type_mapping2[type2]],
                    "simplified_color_encoded": [color_mapping2[color2]]
                }
            )

                # Make the prediction
            prediction = model2.predict(input_data)
            predicted_days=round(prediction[0])

            # Determine the color based on the prediction
            text_color = "red" if prediction[0] >=30 else "green"

            # Display the prediction with colored text using Markdown syntax
            colored_text = (
                f'<span style="color:{text_color};font-size:35px">The model predicts: {predicted_days} days</span>'
            )
            st.markdown(f"{colored_text}", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
