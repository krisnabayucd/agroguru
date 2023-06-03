import streamlit as st
import numpy as np
import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), 'decision_tree.pkl')
model = joblib.load(model_path)

st.set_page_config(
    page_title = "Crop Recommendation",
    page_icon = "👨‍🌾"
)

st.sidebar.success("### Choose Page")

def main():
    st.markdown("<h2 style='color: #FF9933;'>🥒 What Crop Should You Grow? 🍌</h2>", unsafe_allow_html=True)
    st.write('##### Enter your data:')
    # Create input fields for the features
    feature1 = st.number_input('N (ratio of Nitrogen content in soil)', value=0)
    feature2 = st.number_input('P (ratio of Phosphorous content in soil)', value=0)
    feature3 = st.number_input('K (ratio of Potassium content in soil)', value=0)
    feature4 = st.number_input('Temperature (in degree Celsius)', value=0)
    feature5 = st.number_input('Humidity (relative humidity in %)', value=0)
    feature6 = st.number_input('Ph (ph value of the soil)', value=0)
    feature7 = st.number_input('Rainfall (rainfall in mm)', value=0)

    # Create a button to trigger the prediction
    if st.button('Predict'):
        # Prepare the input data
        data = np.array([[feature1, feature2, feature3, feature4, feature5, feature6, feature7]])

        # Make the prediction using the loaded model
        prediction = model.predict(data)

        # Display the prediction result
        st.write('''
		    ## Result  
		    ''')
        st.success(f"{prediction.item().title()} is recommended based on your data")

        st.text_area("Leave your feedback")
        if st.button('Submit'):
            st.success('Thank you for your feedback!')
        # st.write('Recommended Crop:', prediction)	

if __name__ == '__main__':
    main()
