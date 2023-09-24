import pickle
import streamlit as st
import pandas as pd

final_model = pickle.load(open('xgb_model.pkl','rb'))

# Define the app layout
st.title('Loan Outcome Prediction App')

st.sidebar.header('User Input')
st.sidebar.subheader('Enter User Information:')

# Input fields for age and cash_incoming_30days
age = st.sidebar.number_input('Age', min_value=18, max_value=110, value=30)
cash_incoming_30days = st.sidebar.number_input('Cash Incoming in 30 Days (KES)', min_value=0.0, value=50000.0)

# Create a DataFrame with user input
input_data = pd.DataFrame({'age': [age], 'cash_incoming_30days': [cash_incoming_30days]})

if st.sidebar.button('Predict'):
    # Make a prediction
    prediction = final_model.predict(input_data)
    prediction_prob = final_model.predict_proba(input_data)

    # Display the prediction
    st.subheader('Prediction Result:')
    if prediction[0] == 1:
        st.success('Loan will be repaid.')
    else:
        st.error('Loan will be defaulted.')

    # Display prediction probabilities
    st.subheader('Prediction Probabilities:')
    st.write(f'Probability of Defaulted: {prediction_prob[0, 0]:.2f}')
    st.write(f'Probability of Repaid: {prediction_prob[0, 1]:.2f}')



