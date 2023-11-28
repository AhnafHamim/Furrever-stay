import streamlit as st
from joblib import load
import pandas as pd

# Load your trained model
model = load("use_model.joblib")


def main():
    st.title("Cat Attributes Prediction")

    # User inputs through dropdown menus
    color_mapping = {"BLACK": 0, "GRAY": 1, "OTHER": 2, "TABBY": 3, "WHITE": 4}
    condition_mapping = {
        "ILL MILD": 0,
        "ILL SEVERE": 1,
        "INJURED": 2,
        "NORMAL": 3,
        "OTHER": 4,
        "UNDER WEIGHT": 5,
    }
    sex_mapping = {0: "FEMALE", 1: "MALE"}
    type_mapping = {0: "OTHER", 1: "OWNER SURRENDER", 2: "STRAY"}

    color = st.selectbox("Color", options=list(color_mapping.keys()))
    condition = st.selectbox("Condition", options=list(condition_mapping.keys()))
    sex = st.selectbox("Sex", options=list(sex_mapping.values()))
    type_ = st.selectbox("Type", options=list(type_mapping.values()))

    if st.button("Predict"):
        # Prepare the input for the model
        input_data = pd.DataFrame(
            {
                "simplified_color_encoded": [color_mapping[color]],
                "simplified_sex_encoded": [0 if sex == "FEMALE" else 1],
                "simplified_condition_encoded": [condition_mapping[condition]],
                "simplified_type_encoded": [
                    key for key, value in type_mapping.items() if value == type_
                ][0],
            }
        )

        # Make the prediction
        prediction = model.predict(input_data)

        # Display the prediction
        st.success(f"The model predicts: {prediction[0]}")


if __name__ == "__main__":
    main()
