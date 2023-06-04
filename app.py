import streamlit as st
import numpy as np
import joblib
import os
import pyrebase
import requests
import streamlit.components.v1 as components

model_path = os.path.join(os.path.dirname(__file__), 'decision_tree.pkl')
model = joblib.load(model_path)

#ConfigKey
firebaseConfig = {
  'apiKey': "AIzaSyCQsNeoB_KiCz0yhdyvt-2NKXEFSXVNvWQ",
  'authDomain': "ml-data-41350.firebaseapp.com",
  'projectId': "ml-data-41350",
  'databaseURL': "https://ml-data-41350-default-rtdb.asia-southeast1.firebasedatabase.app/",
  'storageBucket': "ml-data-41350.appspot.com",
  'messagingSenderId': "740391764656",
  'appId': "1:740391764656:web:b6e5ec31a9192cd1abb175",
  'measurementId': "G-VTV0TM6HZ4"
}

# FirebaseAuth
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# DB
db = firebase.database()
storage = firebase.storage()

st.set_page_config(
    page_title="Crop Recommendation",
    page_icon="👨‍🌾",
    layout="centered"
)

api_key = "3cece0f8bf1538ff23725385d1b622ff"

#API Cuaca
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},ID&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if "main" not in data or "temp" not in data["main"]:
        st.error("Failed to retrieve weather data.")
        return None, None, None
    
    temperature = data["main"]["temp"] - 273.15  # Convert temperature from Kelvin to Celsius
    humidity = data["main"]["humidity"]
    
    rainfall = 0
    if "rain" in data and "1h" in data["rain"]:
        rainfall = data["rain"]["1h"]
    
    return temperature, humidity, rainfall
    

#WebApp
#WebApp
def main():
    st.markdown("<h2 style='color: #FF9933; text-align: center;'>🥒 What Crop Should You Grow? 🍌</h2>",
                unsafe_allow_html=True)
    st.write('##### Enter your data:')
    
    # Enhancements: Add labels, tooltips, and default values to input fields
    feature1 = st.number_input('N (ratio of Nitrogen content in soil)', value=0)
    feature2 = st.number_input('P (ratio of Phosphorous content in soil)', value=0)
    feature3 = st.number_input('K (ratio of Potassium content in soil)', value=0)
    feature6 = st.number_input('Ph (ph value of the soil)', value=0)
    
    # Select city
    city = st.selectbox('Select City in Indonesia', [    "Ambon",
    "Banda Aceh",
    "Bandar Lampung",
    "Bandung",
    "Banjarmasin",
    "Banyumas",
    "Banyuwangi",
    "Bekasi",
    "Bengkulu",
    "Bima",
    "Binjai",
    "Blitar",
    "Cirebon",
    "Denpasar",
    "Ende",
    "Gorontalo",
    "Jakarta Barat",
    "Jakarta Pusat",
    "Jakarta Selatan",
    "Jakarta Timur",
    "Jakarta Utara",
    "Jambi",
    "Jayapura",
    "Kediri",
    "Kendari",
    "Kisaran",
    "Klaten",
    "Kupang",
    "Larantuka",
    "Langsa",
    "Lhokseumawe",
    "Lombok Tengah",
    "Lubuklinggau",
    "Madiun",
    "Magelang",
    "Makassar",
    "Manado",
    "Manokwari",
    "Mataram",
    "Maumere",
    "Medan",
    "Metro",
    "Padang",
    "Pagar Alam",
    "Palangkaraya",
    "Palembang",
    "Pangkal Pinang",
    "Pangkalpinang",
    "Pekalongan",
    "Pekanbaru",
    "Pematangsiantar",
    "Pontianak",
    "Prabumulih",
    "Praya",
    "Probolinggo",
    "Purworejo",
    "Purwokerto",
    "Raba",
    "Ruteng",
    "Sabang",
    "Samarinda",
    "Semarang",
    "Serang",
    "Sibolga",
    "Singaraja",
    "Sleman",
    "Solo",
    "Sorong",
    "Sumbawa Besar",
    "Surabaya",
    "Surakarta",
    "Tangerang",
    "Tanjung Balai",
    "Tanjung Pandan",
    "Tebing Tinggi",
    "Tegal",
    "Ternate",
    "Yogyakarta"])

                                                     
    # Retrieve weather data
    temperature, humidity, rainfall = get_weather_data(city)
    
    feature4 = st.number_input('Temperature (in degree Celsius)', value=temperature)
    feature5 = st.number_input('Humidity (relative humidity in %)', value=humidity)
    feature7 = st.number_input('Rainfall (rainfall in mm)', value=rainfall)

    # Create a button to trigger the prediction
    if st.button('Predict'):
        # Loading indicator while making predictions
        with st.spinner('Predicting...'):
            # Prepare the input data
            data = np.array([[feature1, feature2, feature3, feature4, feature5, feature6, feature7]])

            # Make the prediction using the loaded model
            prediction = model.predict(data)

            # Display the prediction result
            st.write('''
                ## Result  
                ''')
            st.success(f"{prediction.item().title()} is recommended based on your data")

            # Save data to Firebase
            features_ref = db.child("features").push({
                "feature1": feature1,
                "feature2": feature2,
                "feature3": feature3,
                "feature4": feature4,
                "feature5": feature5,
                "feature6": feature6,
                "feature7": feature7,
                "prediction": prediction.item().title()
            })

            feedback = st.text_area("Leave your feedback", key="feedback_input")
            if st.button('Submit'):
                # Save feedback to Firebase
                feedback_ref = db.child("feedback").push({
                    "feedback": feedback
                })
                st.success('Thank you for your feedback!')




if __name__ == '__main__':
    main()

st.text("")
st.text("")

st.subheader("Having Trouble?")
search = st.text_input("Browse the web to help with your input", value="Suhu di Sidoarjo")
components.iframe(f"https://www.google.com/search?igu=1&ei=&q={search}", height=595)
