import streamlit as st
from joblib import load
import pandas as pd

# Load your trained model
model = load("gb_model.joblib")


def main():
    st.title("Cat Shelter Staying Quantitative Prediction")

    # User inputs through dropdown menus
    color_mapping = {'BLACK': 0, 'BLACK_N_WHITE': 1, 'BRN_TABBY': 2, 'GRAY': 3, 'GRAY_N_WHITE': 4, 'GRAY_TABBY': 5, 'MIX': 6, 'ORG_TABBY': 7, 'OTHER': 8, 'OTHER_TABBY': 9, 'TORTIE': 10}
    condition_mapping = {'HEALTHY': 0, 'ILL': 1, 'OTHER': 2}    
    type_mapping = {'OTHER': 0, 'OWNER SURRENDER': 1, 'STRAY': 2}

    color = st.selectbox("Color", options=list(color_mapping.keys()))
    type = st.selectbox("Type", options=list(type_mapping.keys()))
    condition = st.selectbox("Condition", options=list(condition_mapping.keys()))

    # Use a slider for intake_age
    intake_age = st.slider("Intake Age", min_value=0, max_value=20, value=1)
    
    if st.button("Predict"):
            # Prepare the input for the model
        input_data = pd.DataFrame(
            {
                "intake_age": [intake_age],
                "simplified_condition_encoded": [condition_mapping[condition]],
                "simplified_type_encoded":[type_mapping[type]],
                "simplified_color_encoded": [color_mapping[color]]
            }
        )

            # Make the prediction
        prediction = model.predict(input_data)
        predicted_days=round(prediction[0])

        # Determine the color based on the prediction
        text_color = "red" if prediction[0] >=30 else "green"

        # Display the prediction with colored text using Markdown syntax
        colored_text = (
            f'<span style="color:{text_color}">{predicted_days} days</span>'
        )
        st.markdown(f"The model predicts: {colored_text}", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
