import streamlit as st
import pandas as pd
import pickle

# Load the model
data = pickle.load(open(r'D:\Ammar\jupyter notebook\car.sav', 'rb'))

# Streamlit page setup
st.header('Car Price Prediction')
st.sidebar.header('Feature Selection')
st.sidebar.info('Easy Application for Predicting Car Prices')

# Display image
st.image('D:\\Ammar\\50%.png')

# Manufacturer
m1 = ['LEXUS', 'CHEVROLET', 'HONDA', 'FORD', 'HYUNDAI', 'TOYOTA', 'MERCEDES-BENZ', 'OPEL', 'PORSCHE', 'BMW', 
      'JEEP', 'VOLKSWAGEN', 'AUDI', 'RENAULT', 'NISSAN', 'SUBARU', 'DAEWOO', 'KIA', 'MITSUBISHI', 'SSANGYONG', 
      'MAZDA', 'GMC', 'FIAT', 'INFINITI', 'ALFA ROMEO', 'SUZUKI', 'ACURA', 'LINCOLN', 'VAZ', 'GAZ', 'CITROEN', 
      'LAND ROVER', 'MINI', 'DODGE', 'CHRYSLER', 'JAGUAR', 'ISUZU', 'SKODA', 'DAIHATSU', 'BUICK', 'TESLA', 
      'CADILLAC', 'PEUGEOT', 'BENTLEY', 'VOLVO', 'სხვა', 'HAVAL', 'HUMMER', 'SCION', 'UAZ', 'MERCURY', 'ZAZ', 
      'ROVER', 'SEAT', 'LANCIA', 'MOSKVICH', 'MASERATI', 'FERRARI', 'SAAB', 'LAMBORGHINI', 'ROLLS-ROYCE', 
      'PONTIAC', 'SATURN', 'ASTON MARTIN', 'GREATWALL']
m2 = [16, 12, 17, 43, 27, 45, 35, 31, 6, 41, 9, 3, 21, 30, 40, 26, 14, 11, 42, 24, 32, 2, 8, 29, 10, 23, 20, 
      0, 44, 19, 39, 7, 25, 4, 33, 47, 15, 5, 38, 18, 34, 22, 28, 36, 46, 1, 37, 13]

manu_mapping = dict(zip(m1, m2))
manu1 = st.selectbox("Manufacturer", m1)
manu2 = manu_mapping[manu1]

# Model
c1 = ['RX 450', 'Equinox', 'FIT', 'Escape', 'Santa FE', 'Prius', 'Sonata', 'Camry', 'RX 350', 'E 350']
c2 = [347, 334, 683, 616, 697, 194, 167, 313, 294, 430]

model_mapping = dict(zip(c1, c2))
model1 = st.selectbox("Model", c1)
model2 = model_mapping[model1]

# Category
cat1 = ['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon', 'Universal', 'Coupe', 'Minivan', 'Cabriolet', 'Limousine',
        'Pickup']
cat2 = [3, 4, 8, 9, 6, 0, 1, 5, 2, 7]

category_mapping = dict(zip(cat1, cat2))
category1 = st.selectbox("Category", cat1)
category2 = category_mapping[category1]

# Leather interior
l1 = ['Yes', 'No']
l2 = [1, 2]
leather_mapping = dict(zip(l1, l2))
leather1 = st.selectbox("Leather interior", l1)
leather2 = leather_mapping[leather1]

# Fuel type
f1 = ['Petrol', 'Hybrid', 'Diesel', 'Plug-in Hybrid', 'LPG', 'CNG']
f2 = [4, 2, 1, 5, 3, 0]

fuel_mapping = dict(zip(f1, f2))
fuel1 = st.selectbox("Fuel type", f1)
fuel2 = fuel_mapping[fuel1]

# Mileage
mileage = st.number_input('Mileage')

# Gear box type
gb1 = ['Variator', 'Automatic', 'Tiptronic', 'Manual']
gb2 = [3, 0, 2, 1]

gear_box_mapping = dict(zip(gb1, gb2))
gear_box1 = st.selectbox("Gear box type", gb1)
gear_box2 = gear_box_mapping[gear_box1]

# Drive wheels
dw1 = ['Front', '4x4', 'Rear']
dw2 = [1, 0, 2]

drive_wheels_mapping = dict(zip(dw1, dw2))
drive_wheels1 = st.selectbox("Drive wheels", dw1)
drive_wheels2 = drive_wheels_mapping[drive_wheels1]

# Wheel
w1 = ['Right-hand drive', 'Left wheel']
w2 = [0, 1]

wheel_mapping = dict(zip(w1, w2))
wheel1 = st.selectbox("Wheel", w1)
wheel2 = wheel_mapping[wheel1]

# Color
col1 = ['Black', 'White', 'Silver', 'Grey', 'Blue', 'Sky blue', 'Red', 'Orange', 'Green', 'Yellow', 'Brown', 
        'Golden', 'Beige', 'Carnelian red', 'Purple', 'Pink']
col2 = [1, 14, 12, 7, 2, 13, 11, 8, 6, 15, 3, 5, 0, 4, 10, 9]

color_mapping = dict(zip(col1, col2))
color1 = st.selectbox("Color", col1)
color2 = color_mapping[color1]

# Levy
levy = st.number_input('Levy')

# Engine volume
engine = st.selectbox('Engine volume', [1.3, 2.5, 2.0, 1.8, 2.4, 1.6, 2.2, 1.5, 1.4, 2.3, 1.2, 1.7, 2.9, 1.9, 2.7, 
                                        3.5, 2.1, 1.0, 0.8, 3.0, 3.3, 2.8, 3.2, 1.1])

# Cylinders
cylinders = st.selectbox('Cylinders', [6., 4., 8., 1., 12., 3., 2., 16., 5., 7., 9., 10., 14.])

# Airbags
airbags = st.selectbox('Airbags', [2, 0, 4, 12, 8, 10, 6, 1, 16, 7, 9, 5, 11, 3, 14, 15, 13])

# Age
age = st.number_input('Age')

# Prepare the DataFrame
df = pd.DataFrame({
    'Manufacturer': [manu2],
    'Model': [model2],
    'Leather interior': [leather2],
    'Fuel type': [fuel2],
    'Wheel': [wheel2],
    'Color': [color2],
    'Drive wheels': [drive_wheels2],
    'Gear box type': [gear_box2],
    'Category': [category2],
    'Engine volume': [engine],
    'Airbags': [airbags],
    'Age': [age],
    'Mileage': [mileage],
    'Levy': [levy],
    'Cylinders': [cylinders]
})

# Get the expected feature names from the model
expected_features = data.get_booster().feature_names if hasattr(data, 'get_booster') else data.feature_names_in_

# Reorder the DataFrame columns to match the model's expected features
df = df[expected_features]

# Prediction
p = st.sidebar.button('Predict the price')
if p:
    try:
        price = data.predict(df)
        st.sidebar.write("The price is:", price,"USD$")
    except Exception as e:
        st.sidebar.write("Prediction Error:", e)
