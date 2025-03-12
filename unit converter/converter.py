import streamlit as st
#Functionality
def Distance_converter(from_unit,to_unit,value):
   units = {
       "Meter": 1,
       "Kilometer": 1000,
       "Feet": 0.3048,
       "Miles": 1609.34,
   }
   result = value * units[from_unit] / units[to_unit]
   return result

def Temperature_Converter(from_unit,to_unit,value):
    if from_unit == "Celcius" and to_unit == "Ferenheit":
       result = (value * 9/5) + 32
    elif from_unit == "Ferenhiet" and to_unit == "Celcius":
       result = (value - 32) * 5/9
    else:
       result = value
    return result   

def Weight_converter(from_unit,to_unit,value):
   units = {
       "Mililitter": 0.001,
       "Litter": 1,
       "Ponds": 0.453592,
       "Ounce": 0.0283495,
   }
   result = value * units[from_unit] / units[to_unit]
   return result

def Pressure_Converter(from_unit,to_unit,value):
   units = {
       "Pascals": 1,
       "Hectopascals": 100,
       "Torr": 133.32,
       "Bar": 100000,
   }
   result = value * units[from_unit] / units[to_unit]
   return result   

#Ui
st.title("🎉Welcome To🎉")
st.title("📇 My Unit Converter App✨")

category= st.selectbox("✅Select your category",["Distance","Temperature","Weight","Pressure"])

   #For Distance!
if category == "Distance":
   from_unit = st.selectbox("From",["Meter","Kilometer","Feet","Miles"])
   to_unit = st.selectbox("To",["Meter","Kilometer","Feet","Miles"])
   value = st.number_input("Enter Your Value")
   if  st.button("Convert💡"):
       result = Distance_converter(from_unit,to_unit,value)
       st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

   #For Temperature!
elif category == "Temperature":
   from_unit = st.selectbox("From",["Celcius","Ferenheit"])
   to_unit = st.selectbox("To",["Celcius","Ferenheit"])
   value = st.number_input("Enter Your Value")
   if  st.button("Convert💡"):
       result = Temperature_Converter(from_unit,to_unit,value)
       st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

   #For Weight!
elif category == "Weight":  
   from_unit = st.selectbox("From",["Litter","Mililitter","Ponds","Ounce"])
   to_unit = st.selectbox("To",["Litter","Mililitter","Ponds","Ounce"])
   value = st.number_input("Enter Your Value")
   if  st.button("Convert💡"):
       result = Weight_converter(from_unit,to_unit,value)
       st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

   #For Pressure!
elif category == "Pressure":
   from_unit = st.selectbox("From",["Pascals","Hectopascals","Torr","Bar"])
   to_unit = st.selectbox("To",["Pascals","Hectopascals","Torr","Bar"])
   value = st.number_input("Enter Your Value")
   if  st.button("Convert💡"):
       result = Pressure_Converter(from_unit,to_unit,value)
       st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")   
