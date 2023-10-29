import streamlit as st
import requests
import json
from shared import constants, utils


# Get available models from the API
def get_available_models():
    try:
        response = requests.get(constants.OPENROUTER_API_BASE + "/models")
        response.raise_for_status()
        models = json.loads(response.text)["data"]
        return [model["id"] for model in models]
    except requests.exceptions.RequestException as e:
        st.error(f"Error getting models from API: {e}")
        return []


# Handle the model selection process
def handle_model_selection(available_models, selected_model, default_model):
    # Determine the index of the selected model
    if selected_model and selected_model in available_models:
        selected_index = available_models.index(selected_model)
    else:
        selected_index = available_models.index(default_model)
    selected_model = st.selectbox(
        "Select a model", available_models, index=selected_index
    )
    return selected_model
