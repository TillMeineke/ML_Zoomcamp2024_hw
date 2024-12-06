import os

import pandas as pd
import requests
import streamlit as st
from PIL import Image

from src.data_cat import (
    cap_shape_categories_dict,
    cap_surface_categories_dict,
    color_categories_dict,
    gill_attachment_categories_dict,
    gill_spacing_categories_dict,
    habitat_categories_dict,
    ring_type_categories_dict,
    season_categories_dict,
    stem_root_categories_dict,
    stem_surface_categories_dict,
    veil_type_categories_dict,
)


def map_and_rename_categorical_features(df: pd.DataFrame) -> pd.DataFrame:
    """Maps encoded categorical features to their full names"""
    df_mapped = df.copy()

    category_mappings = {
        "cap-shape": cap_shape_categories_dict,
        "cap-surface": cap_surface_categories_dict,
        "gill-attachment": gill_attachment_categories_dict,
        "gill-spacing": gill_spacing_categories_dict,
        "stem-root": stem_root_categories_dict,
        "stem-surface": stem_surface_categories_dict,
        "veil-type": veil_type_categories_dict,
        "ring-type": ring_type_categories_dict,
        "habitat": habitat_categories_dict,
        "season": season_categories_dict,
    }

    boolean_mappings = {
        "does-bruise-or-bleed": {"t": True, "f": False},
        "has-ring": {"t": True, "f": False},
        "class": {"e": "edible", "p": "poisonous"},
    }

    color_columns = [
        "cap-color",
        "gill-color",
        "stem-color",
        "veil-color",
        "spore-print-color",
    ]

    def process_value(val, mapping):
        if isinstance(val, str) and val.startswith("["):
            # Parse string list manually instead of using eval
            clean_val = val.strip("[]").replace("'", "").replace('"', "")
            items = [item.strip() for item in clean_val.split(",")]
            return [mapping.get(item) for item in items]
        return mapping.get(val)

    # Map standard categories
    for col, mapping in category_mappings.items():
        reverse_mapping = {v: k for k, v in mapping.items()}
        df_mapped[col] = df_mapped[col].apply(
            lambda val: process_value(val, reverse_mapping)
        )

    # Map color categories
    color_mapping = {v: k for k, v in color_categories_dict.items()}
    for col in color_columns:
        df_mapped[col] = df_mapped[col].apply(
            lambda val: process_value(val, color_mapping)
        )

    # Map boolean values
    for col, mapping in boolean_mappings.items():
        df_mapped[col] = df_mapped[col].map(mapping)

    return df_mapped


def get_options_for_feature(feature):
    """Generate dropdown options for different mushroom features"""
    feature_mapping = {
        "cap-shape": cap_shape_categories_dict,
        "cap-color": color_categories_dict,
        "gill-color": color_categories_dict,
        "stem-color": color_categories_dict,
        "habitat": habitat_categories_dict,
        "season": season_categories_dict,
    }

    if feature in feature_mapping:
        return list(feature_mapping[feature].keys())
    return ["yes", "no"] if feature in ["does-bruise-or-bleed", "has-ring"] else []


def predict_mushroom(selected_features):
    """Send mushroom feature data to remote prediction API"""
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

    url = (
        "http://fungi-classifier.eba-rpcwcrqg.eu-central-1.elasticbeanstalk.com/predict"
    )

    try:
        response = requests.post(url, json=features)
        result = response.json()
        return result["fungi"]
    except requests.exceptions.RequestException as e:
        return f"Prediction error: {str(e)}"


def main():
    """Main Streamlit application for Mushroom Identification System"""
    st.set_page_config(
        page_title="fungi Incognita",
        page_icon="🍄",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    primary_data = pd.read_csv("./data/raw/primary_data_edited.csv", sep=";")
    primary_data = map_and_rename_categorical_features(primary_data)

    st.title("🍄 fungi Incognita 🍄")
    st.subheader("Mushroom Identification System")
    st.warning(
        "**Please note:** This system is for educational purposes only and should not be used as a definitive guide for mushroom identification."
    )

    predict_button = st.button("Identify Mushroom", type="primary")

    st.header("Input Features")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Enter Mushroom Characteristics")
        input_col1, input_col2 = st.columns(2)

        with input_col1:
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
            num_inputs["stem-width"] = st.number_input(
                "Stem Width",
                min_value=0.0,
                max_value=100.0,
                value=5.0,
                step=0.1,
                key="num_stem-width",
            )

            for feature in ["stem-color", "has-ring", "habitat", "season"]:
                options = get_options_for_feature(feature)
                label = feature.replace("-", " ").capitalize()
                cat_inputs[feature] = st.selectbox(
                    label,
                    options=options,
                    key=f"cat_{feature}",
                )

        selected_features = {**cat_inputs, **num_inputs}

    if predict_button:
        with st.spinner("Analyzing..."):
            prediction = predict_mushroom(selected_features)

            if isinstance(prediction, str) and prediction.startswith(
                "Prediction error"
            ):
                st.error(prediction)
            else:
                st.success(f"Identified Mushroom: {prediction}")

        with col2:
            st.subheader("Visual Reference")
            try:
                image_cols = st.columns(3)
                for i, suffix in enumerate(["_1", "_2"]):
                    cleaned_prediction = prediction.replace(" ", "_").replace("'", "")
                    image_path = f"src/services/images/{cleaned_prediction}{suffix}.jpg"

                    if os.path.exists(image_path):
                        image = Image.open(image_path)
                        image_cols[i].image(
                            image, use_container_width=True, caption=prediction
                        )
            except Exception as e:
                st.warning(f"Error loading images: {e}")

        with col3:
            st.header("Species Overview")
            pred_overview = primary_data[primary_data["name"] == prediction].copy()

            # Map categorical features
            #            pred_overview = map_and_rename_categorical_features(pred_overview)

            # Rename columns for display
            rename_dict = {
                "name": "Name",
                "family": "Family",
                "class": "Edibility",
                "cap-diameter": "Cap Diameter",
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
            pred_overview.set_index("Name", inplace=True)
            overview_df = pred_overview.T
            st.table(overview_df)


if __name__ == "__main__":
    main()
