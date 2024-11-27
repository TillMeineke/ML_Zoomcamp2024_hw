import os
import pandas as pd
import requests
import streamlit as st
from PIL import Image
from src.data_cat import (
    cap_shape_categories_dict,
    color_categories_dict,
    habitat_categories_dict,
    season_categories_dict,
)


def get_options_for_feature(feature):
    """
    Generate dropdown options for different mushroom features.

    This function maps predefined category dictionaries to specific features,
    ensuring consistent and meaningful input options.
    """
    feature_mapping = {
        "cap-shape": cap_shape_categories_dict,
        "cap-color": color_categories_dict,
        "gill-color": color_categories_dict,
        "stem-color": color_categories_dict,
        "habitat": habitat_categories_dict,
        "season": season_categories_dict,
    }

    # Return predefined options or default binary options
    if feature in feature_mapping:
        return list(feature_mapping[feature].keys())
    return ["yes", "no"] if feature in ["does-bruise-or-bleed", "has-ring"] else []


def predict_mushroom(selected_features):
    """
    Send mushroom feature data to remote prediction API.

    Args:
        selected_features (dict): Mushroom characteristics collected from user inputs

    Returns:
        str: Predicted mushroom name or error message
    """
    # Convert inputs to required format for API
    features = {
        "cap-shape": selected_features["cap-shape"],
        "cap-color": selected_features["cap-color"],
        "cap-diameter": float(selected_features["cap-diameter"]),
        "does-bruise-or-bleed": selected_features["does-bruise-or-bleed"],
        "gill-color": selected_features["gill-color"],
        "stem-color": selected_features["stem-color"],
        "stem-height": float(selected_features["stem-height"]),
        "stem-width": float(selected_features["stem-width"]),
        "has-ring": selected_features["has-ring"],
        "habitat": selected_features["habitat"],
        "season": selected_features["season"],
    }

    # Remote prediction API endpoint
    url = (
        "http://fungi-classifier.eba-rpcwcrqg.eu-central-1.elasticbeanstalk.com/predict"
    )

    try:
        # Send POST request to prediction API
        response = requests.post(url, json=features)
        result = response.json()
        return result["fungi"]
    except requests.exceptions.RequestException as e:
        # Handle network or API errors gracefully
        return f"Prediction error: {str(e)}"


def main():
    """
    Main Streamlit application for Mushroom Identification System.

    Sets up the UI, handles user inputs, and manages prediction workflow.
    """
    # Configure Streamlit page settings
    st.set_page_config(
        page_title="fungi Incognita",
        page_icon="🍄",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Load primary mushroom data at startup
    primary_data = pd.read_csv("./data/raw/primary_data_edited.csv", sep=";")

    # Title and warning
    st.title("🍄 fungi Incognita 🍄‍🟫")
    st.subheader("Mushroom Identification System")
    st.warning(
        """**Please note:** This system is for educational purposes only and should not be used as a definitive guide for mushroom identification."""
    )

    # Prediction button
    predict_button = st.button("Identify Mushroom", type="primary")

    # Input section layout
    st.header("Input Features")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Enter Mushroom Characteristics")

        # Nested columns for input organization
        input_col1, input_col2 = st.columns(2)

        with input_col1:
            # First column of numerical inputs
            num_inputs = {}
            for feature in ["cap-diameter", "stem-height"]:
                num_inputs[feature] = st.number_input(
                    feature.replace("-", " ").capitalize(),
                    min_value=0.0,
                    max_value=100.0,
                    value=5.0,
                    step=0.1,
                    key=f"num_{feature}",
                )

            # First half of categorical inputs
            cat_inputs = {}
            for feature in [
                "cap-shape",
                "cap-color",
                "does-bruise-or-bleed",
                "gill-color",
            ]:
                options = get_options_for_feature(feature)
                label = feature.replace("-", " ").capitalize()
                cat_inputs[feature] = st.selectbox(
                    label,
                    options=options,
                    key=f"cat_{feature}",
                )

        with input_col2:
            # Second column of inputs
            # Remaining numerical input
            num_inputs["stem-width"] = st.number_input(
                "Stem Width",
                min_value=0.0,
                max_value=100.0,
                value=5.0,
                step=0.1,
                key="num_stem-width",
            )

            # Second half of categorical inputs
            for feature in [
                "stem-color",
                "has-ring",
                "habitat",
                "season",
            ]:
                options = get_options_for_feature(feature)
                label = feature.replace("-", " ").capitalize()
                cat_inputs[feature] = st.selectbox(
                    label,
                    options=options,
                    key=f"cat_{feature}",
                )

        # Combine categorical and numerical inputs
        selected_features = {**cat_inputs, **num_inputs}

    # Prediction workflow
    if predict_button:
        with st.spinner("Analyzing..."):
            prediction = predict_mushroom(selected_features)

            # Error handling for prediction
            if isinstance(prediction, str) and prediction.startswith(
                "Prediction error"
            ):
                st.error(prediction)
            else:
                # Success message placed prominently
                st.success(f"Identified Mushroom: {prediction}")

                # Image display in col2
                with col2:
                    try:
                        # Use columns to display images side by side
                        image_cols = st.columns(3)
                        for i, suffix in enumerate(["_1", "_2"]):
                            cleaned_prediction = prediction.replace(" ", "_").replace(
                                "'", ""
                            )
                            image_path = (
                                f"src/services/images/{cleaned_prediction}{suffix}.jpg"
                            )
                            if os.path.exists(image_path):
                                image = Image.open(image_path)
                                image_cols[i].image(
                                    image, use_container_width=True, caption=prediction
                                )
                    except Exception as e:
                        st.warning(f"Error loading images: {e}")

                # Species overview in col3
                with col3:
                    st.header("Species Overview")

                    # Copy dataframe to avoid warnings and ensure clean manipulation
                    pred_overview = primary_data[
                        primary_data["name"] == prediction
                    ].copy()

                    # Rename columns for clarity
                    rename_dict = {
                        "class": "Edibility",
                        "cap-shape": "Cap Shape",
                        "cap-surface": "Cap Surface",
                        "cap-color": "Cap Color",
                        "does-bruise-or-bleed": "Bruising",
                        "gill-attachment": "Gill Attachment",
                        "gill-spacing": "Gill Spacing",
                        "gill-color": "Gill Color",
                        "stem-height": "Stem Height",
                        "stem-width": "Stem Width",
                        "stem-root": "Stem Root",
                        "stem-surface": "Stem Surface",
                        "stem-color": "Stem Color",
                        "veil-type": "Veil Type",
                        "veil-color": "Veil Color",
                        "has-ring": "Has Ring",
                        "ring-type": "Ring Type",
                        "spore-print-color": "Spore Color",
                        "habitat": "Habitat",
                        "season": "Season",
                    }
                    pred_overview.rename(columns=rename_dict, inplace=True)

                    # Transpose for better readability
                    overview_df = pred_overview.T
                    overview_df.columns = ["Value"]
                    st.table(overview_df, )


if __name__ == "__main__":
    main()
