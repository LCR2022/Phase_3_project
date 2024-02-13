# Importing relevant packages
import base64
import pandas as pd
import streamlit as st
from joblib import load

# Load pre-trained model
model = load('model.pkl')
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
img = get_img_as_base64("image.jpg")
# Define function to make predictions using the model
def predict_churn(input_df):
    predictions = model.predict(input_df)
    return 'Yes' if predictions[0] == 1 else 'No'

# Main function for Streamlit web app
def main():
    # Set page title and Syriatel logo
    st.set_page_config(page_title="Syriatel Churn Prediction", page_icon="📞")
    st.image('syriatel.png', width=400)

    # Display header
    st.title("Syriatel Churn Prediction App")

    page_bg_img = f"""
	<style>
	[data-testid="stAppViewContainer"] > .main {{
	background-image: url("data:image/png;base64,{img}");
	background-size: cover;
	background-position: top right;
	background-repeat: no-repeat;
	background-attachment: fixed;
    
	}}
    [data-testid="stWidgetLabel"] p {{
    color: black;
    font-size: 20px;    
    }}
    [data-testid="stMarkdownContainer"] p {{
    color: black;
    font-size: 20px;   
    }}
    [data-testid="stTickBarMax"] {{
    color: black;
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
   [data-testid="stToolbar"] {{
   right: 2rem;
   }}


	</style>
	"""
	

	# header
    st.markdown(page_bg_img, unsafe_allow_html=True)
    # st.sidebar.header("Configuration")
    # Input fields for customer information
    subscription_period= st.number_input('Number of months the customer has been with the company:', min_value=0, max_value=250, value=0)
    international_plan = st.radio('The customer has an international plan:', ['No', 'Yes'])
    voice_mail_plan = st.radio('The customer has a voice mail plan:', ['No', 'Yes'])
    number_vmail_messages = st.slider('Number of voice-mail messages:', min_value=0, max_value=60, value=0)
    total_day_minutes = st.slider('Total minutes of day calls:', min_value=0, max_value=360, value=100)
    total_day_calls = st.slider('Total day calls:', min_value=0, max_value=200, value=50)
    # total_day_charge = st.slider('Total day charge:', min_value=0, max_value=60, value=0)
    total_eve_minutes = st.slider('Total minutes of evening calls:', min_value=0, max_value=400, value=200)
    total_eve_calls = st.slider('Total number of evening calls:', min_value=0, max_value=200, value=100)
    # total_eve_charge = st.slider('Total evening charge:', min_value=0, max_value=40, value=0)
    total_night_minutes = st.slider('Total minutes of night calls:', min_value=0, max_value=400, value=200)
    total_night_calls = st.slider('Total number of night calls:', min_value=0, max_value=200, value=100)
    # total_night_charge = st.slider('Total night charge:', min_value=0, max_value=30, value=0)
    total_intl_minutes = st.slider('Total minutes of international calls:', min_value=0, max_value=30, value=0)
    total_intl_calls = st.slider('Total number of international calls:', min_value=0, max_value=30, value=0)
    # total_intl_charge = st.slider('Total international charge:', min_value=0, max_value=20, value=0)
    customer_service_calls = st.slider('Number of calls to customer service:', min_value=0, max_value=10, value=0)
    total_charge = st.slider('Total charge:', min_value=0, max_value=100, value=59)
    # total_calls = st.slider('Total number of calls:', min_value=0, max_value=500, value=305)

    # Create input dictionary
    input_dict = {
        'subscription_period': subscription_period,
        'international_plan': 1 if international_plan == 'Yes' else 0,
        'voice_mail_plan': 1 if voice_mail_plan == 'Yes' else 0,
        'number_vmail_messages': number_vmail_messages,
        'total_day_minutes': total_day_minutes,
        'total_day_calls': total_day_calls,
        'total_eve_minutes': total_eve_minutes,
        'total_eve_calls': total_eve_calls,
        'total_night_minutes': total_night_minutes,
        'total_night_calls': total_night_calls,
        'total_intl_minutes': total_intl_minutes,
        'total_intl_calls': total_intl_calls,
        'customer_service_calls': customer_service_calls,
        'total_charge': total_charge,
       
    }

    # Convert input dictionary to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Make prediction when button is clicked
    if st.button("Predict Churn"):
        churn_prediction = predict_churn(input_df)
        st.success(f"Likely to Leave: {churn_prediction}")

# Run the main function if the script is executed
if __name__ == '__main__':
    main()
