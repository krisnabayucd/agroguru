import streamlit as st
import pandas as pd

crops = {
    'rice': {
        'N': 100,
        'P': 50,
        'K': 75,
        'Ideal Temperature': '25-30°C',
        'Humidity': '60-70%',
        'pH Range': '6.0-7.0',
        'Rainfall': '800-1000 mm',
    },
    'maize': {
        'N': 80,
        'P': 60,
        'K': 90,
        'Ideal Temperature': '20-25°C',
        'Humidity': '70-80%',
        'pH Range': '5.5-6.5',
        'Rainfall': '1000-1200 mm',
    },
    'chickpea': {
        'N': 40,
        'P': 60,
        'K': 40,
        'Ideal Temperature': '20-25°C',
        'Humidity': '50-60%',
        'pH Range': '6.0-7.0',
        'Rainfall': '400-500 mm',
    },
    'kidneybeans': {
        'N': 50,
        'P': 40,
        'K': 60,
        'Ideal Temperature': '20-30°C',
        'Humidity': '50-60%',
        'pH Range': '6.0-7.5',
        'Rainfall': '400-600 mm',
    },
    'pigeonpeas': {
        'N': 60,
        'P': 40,
        'K': 40,
        'Ideal Temperature': '25-35°C',
        'Humidity': '50-70%',
        'pH Range': '5.0-7.0',
        'Rainfall': '600-800 mm',
    },
    'mothbeans': {
        'N': 20,
        'P': 40,
        'K': 20,
        'Ideal Temperature': '20-25°C',
        'Humidity': '50-70%',
        'pH Range': '5.0-6.5',
        'Rainfall': '500-700 mm',
    },
    'mungbean': {
        'N': 40,
        'P': 60,
        'K': 30,
        'Ideal Temperature': '25-35°C',
        'Humidity': '60-80%',
        'pH Range': '6.0-7.0',
        'Rainfall': '600-800 mm',
    },
    'blackgram': {
        'N': 40,
        'P': 60,
        'K': 30,
        'Ideal Temperature': '25-35°C',
        'Humidity': '60-80%',
        'pH Range': '6.0-7.5',
        'Rainfall': '600-800 mm',
    },
    'lentil': {
        'N': 40,
        'P': 40,
        'K': 20,
        'Ideal Temperature': '20-25°C',
        'Humidity': '50-70%',
        'pH Range': '5.0-7.0',
        'Rainfall': '450-650 mm',
    },
    'pomegranate': {
        'N': 80,
        'P': 40,
        'K': 40,
        'Ideal Temperature': '25-35°C',
        'Humidity': '40-60%',
        'pH Range': '5.5-7.0',
        'Rainfall': '500-800 mm',
    },
    'banana': {
        'N': 200,
        'P': 60,
        'K': 300,
        'Ideal Temperature': '25-30°C',
        'Humidity': '60-70%',
        'pH Range': '5.5-7.0',
        'Rainfall': '1000-2000 mm',
    },
    'mango': {
        'N': 80,
        'P': 40,
        'K': 120,
        'Ideal Temperature': '24-30°C',
        'Humidity': '50-80%',
        'pH Range': '6.0-7.5',
        'Rainfall': '1000-1500 mm',
    },
    'grapes': {
        'N': 80,
        'P': 40,
        'K': 120,
        'Ideal Temperature': '15-35°C',
        'Humidity': '50-70%',
        'pH Range': '5.5-7.5',
        'Rainfall': '600-800 mm',
    },
    'watermelon': {
        'N': 80,
        'P': 40,
        'K': 120,
        'Ideal Temperature': '24-30°C',
        'Humidity': '70-90%',
        'pH Range': '6.0-7.0',
        'Rainfall': '500-800 mm',
    },
    'muskmelon': {
        'N': 80,
        'P': 40,
        'K': 120,
        'Ideal Temperature': '20-30°C',
        'Humidity': '60-70%',
        'pH Range': '6.0-7.0',
        'Rainfall': '500-700 mm',
    },
    'apple': {
        'N': 100,
        'P': 50,
        'K': 100,
        'Ideal Temperature': '15-25°C',
        'Humidity': '60-70%',
        'pH Range': '6.0-7.0',
        'Rainfall': '600-1000 mm',
    },
    'orange': {
        'N': 100,
        'P': 50,
        'K': 100,
        'Ideal Temperature': '15-30°C',
        'Humidity': '50-70%',
        'pH Range': '6.0-7.5',
        'Rainfall': '600-1200 mm',
    },
    'papaya': {
        'N': 100,
        'P': 50,
        'K': 100,
        'Ideal Temperature': '25-35°C',
        'Humidity': '60-70%',
        'pH Range': '5.5-7.0',
        'Rainfall': '1000-1500 mm',
    },
    'coconut': {
        'N': 50,
        'P': 40,
        'K': 80,
        'Ideal Temperature': '20-30°C',
        'Humidity': '60-80%',
        'pH Range': '5.0-8.0',
        'Rainfall': '1500-2500 mm',
    },
    'cotton': {
        'N': 120,
        'P': 60,
        'K': 40,
        'Ideal Temperature': '20-30°C',
        'Humidity': '60-80%',
        'pH Range': '5.5-7.5',
        'Rainfall': '500-800 mm',
    },
    'jute': {
        'N': 80,
        'P': 40,
        'K': 40,
        'Ideal Temperature': '25-35°C',
        'Humidity': '70-90%',
        'pH Range': '6.0-7.5',
        'Rainfall': '1500-2000 mm',
    },
    'coffee': {
        'N': 120,
        'P': 60,
        'K': 40,
        'Ideal Temperature': '20-30°C',
        'Humidity': '70-80%',
        'pH Range': '6.0-6.5',
        'Rainfall': '1500-2000 mm',
    },
}



def display_crop_info(crop):
    crop_info = crops.get(crop)
    if crop_info:
        st.write(f"**Crop: {crop}**")
        st.write(f"N: {crop_info['N']}")
        st.write(f"P: {crop_info['P']}")
        st.write(f"K: {crop_info['K']}")
        st.write(f"Ideal Temperature: {crop_info['Ideal Temperature']}")
        st.write(f"Humidity: {crop_info['Humidity']}")
        st.write(f"pH Range: {crop_info['pH Range']}")
        st.write(f"Rainfall: {crop_info['Rainfall']}")
        # Add more attributes as needed
    else:
        st.write("Crop not found.")

def main():
    st.title("Learn About Crops in Our System")
    selected_crops = st.multiselect("Select crop(s)", list(crops.keys()))
    
    crop_table_data = []
    for crop in selected_crops:
        crop_info = crops.get(crop)
        if crop_info:
            crop_table_data.append([
                crop,
                crop_info['N'],
                crop_info['P'],
                crop_info['K'],
                crop_info['Ideal Temperature'],
                crop_info['Humidity'],
                crop_info['pH Range'],
                crop_info['Rainfall']
            ])

    if crop_table_data:
        crop_df = pd.DataFrame(
            crop_table_data,
            columns=['Crop', 'N', 'P', 'K', 'Ideal Temperature', 'Humidity', 'pH Range', 'Rainfall']
        )
        st.write("Selected Crops:")
        st.dataframe(crop_df)
    else:
        st.write("No crops selected.")

    for crop in selected_crops:
        display_crop_info(crop)

if __name__ == '__main__':
    main()