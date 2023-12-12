
import streamlit as st
from joblib import load
import pandas as pd

# Load both trained models (replace these lines with actual model loading)
model1 = load("texas_strealit_app/use_model.joblib")  # Model for >30 days or not
model2 = load("texas_strealit_app/gb_model.joblib")   # Model for quantitative prediction

def main():
    st.title("Cat Shelter Staying Prediction - Dual Models")

    # Create tabs for each model
    tab1, tab2 = st.tabs(["Model 1: >30 Days Prediction", "Model 2: Quantitative Prediction"])

    intake_type_mapping = {
        'Other': 0,
        'Surrendered by Owner': 1,
        'Stray': 2
    }

    intake_condition_mapping = {
        'Aged': 0,
        'Injured': 1,
        'Neonatal': 2,
        'Normal': 3,
        'Nursing': 4,
        'Other': 5,
        'Pregnant': 6,
        'Sick': 7
    }

    sex_intake_mapping = {
        'Female': 0,
        'Male': 1
    }

    breed_mapping = {
        'Domestic Shorthair': 0,
        'Domestic Shorthair Mix': 1,
        'Other': 2
    }

    CoatColor_mapping = {
        'Black': 0,
        'Black and White': 1,
        'Blue': 2,
        'Brown': 3,
        'Calico or Calico_mix': 4,
        'Orange': 5,
        'Other': 6,
        'Torbie/Torbie mix': 7,
        'Tortie/Tortie mix': 8,
        'White/Mix': 9
    }

    CoatPattern_mapping = {
        'Other': 0,
        'Solid': 1,
        'Tabby': 2
    }

    with tab1:
        st.header("Model 1: Predicting Greater or Less than 30 Days")
        # Inputs and prediction for model 1

        intake_type1 = st.selectbox("Intake Type", options=list(intake_type_mapping.keys()),key="type1")
        intake_condition1 = st.selectbox("Intake Condition", options=list(intake_condition_mapping.keys()),key="cond1")
        sex_intake1 = st.selectbox("Sex at Intake", options=list(sex_intake_mapping.keys()),key="sex1")
        breed1 = st.selectbox("Breed", options=list(breed_mapping.keys()),key="breed1")
        coat_color1 = st.selectbox("Coat Color", options=list(CoatColor_mapping.keys()),key="color1")
        coat_pattern1 = st.selectbox("Coat Pattern", options=list(CoatPattern_mapping.keys()),key="pattern1")
        # Use a slider for intake_age
        intake_age1 = st.slider("Intake Age", min_value=0, max_value=20, value=1, key="slider1")

        if st.button("Predict", key="button1"):
            # Prepare the input for the model
            input_data = pd.DataFrame(
                {
                    'age_intake_months':[intake_age1],
                    "intake_type_encoded": [intake_type_mapping[intake_type1]],
                    "intake_condition_encoded": [intake_condition_mapping[intake_condition1]],
                    "CoatColor_encoded": [CoatColor_mapping[coat_color1]],
                    "sex_intake_encoded": [sex_intake_mapping[sex_intake1]],
                    'CoatPattern_encoded': [CoatPattern_mapping[coat_pattern1]],
                    "breed_encoded": [breed_mapping[breed1]]
                })

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

        intake_type2 = st.selectbox("Intake Type", options=list(intake_type_mapping.keys()))
        intake_condition2 = st.selectbox("Intake Condition", options=list(intake_condition_mapping.keys()))
        breed2 = st.selectbox("Breed", options=list(breed_mapping.keys()))
        coat_color2 = st.selectbox("Coat Color", options=list(CoatColor_mapping.keys()))

        # Use a slider for intake_age
        intake_age2 = st.slider("Intake Age", min_value=0, max_value=20, value=1, key="slider2")
        
        if st.button("Predict",key="button2"):
                # Prepare the input for the model
            input_data = pd.DataFrame(
                {
                    'age_intake_months':[intake_age2],
                    "intake_type_encoded": [intake_type_mapping[intake_type2]],
                    "intake_condition_encoded": [intake_condition_mapping[intake_condition2]],
                    "CoatColor_encoded": [CoatColor_mapping[coat_color2]],
                    "breed_encoded": [breed_mapping[breed2]]
                })

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
