import pickle
import streamlit as st

# Membaca model
try:
    diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
except FileNotFoundError:
    st.error("File model 'diabetes_model.sav' tidak ditemukan.")
    st.stop()

# Judul web
st.title('Data Mining Prediksi Diabetes')

# Membagi kolom
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.text_input('Input Nilai Pregnancies', value='0')

with col2:
    Insulin = st.text_input('Input Nilai Insulin', value='0')

with col1:
    Glucose = st.text_input('Input Nilai Glucose', value='0')
    
with col2:
    BMI = st.text_input('Input Nilai BMI', value='0')

with col1:
    BloodPressure = st.text_input('Input Nilai Blood Pressure', value='0')
    
with col2:
    DiabetesPedigreefunction = st.text_input('Input Nilai Diabetes Pedigree Function', value='0')

with col1:   
    SkinThickness = st.text_input('Input Nilai Skin Thickness', value='0') 
    
with col2:
    Age = st.text_input('Input Nilai Age', value='0')

# Code untuk prediksi
diab_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    try:
        # Mengonversi input menjadi float
        pregnancies = float(pregnancies)
        Glucose = float(Glucose)
        BloodPressure = float(BloodPressure)
        SkinThickness = float(SkinThickness)
        Insulin = float(Insulin)
        BMI = float(BMI)
        DiabetesPedigreefunction = float(DiabetesPedigreefunction)
        Age = float(Age)
        
        # Melakukan prediksi
        diab_prediction = diabetes_model.predict([[pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreefunction, Age]])
        
        # Menentukan diagnosa berdasarkan prediksi
        if diab_prediction[0] == 1:
            diab_diagnosis = 'Pasien Terkena Diabetes'
        else:
            diab_diagnosis = 'Pasien Tidak Terkena Diabetes'
        
        st.success(diab_diagnosis)

    except ValueError:
        st.error("Pastikan semua input adalah angka valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memproses prediksi: {e}")


