import streamlit as st
import plotly.express as px
from backend import get_data

st.set_page_config(layout="wide", page_title="Home")

st.header("Weather Forecast")
location_input = st.text_input(label="Location")
days_input = st.slider(label="Forecast Days", min_value=0, max_value=5,
                       help="Select number of days to show")
option_input = st.selectbox(label="Select data to view", options=("Temperature", "Sky"))
st.subheader(f"{option_input} for the next {days_input} days in {location_input}")

get_data(location_input, days_input, option_input)

figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperatures"})
st.plotly_chart(figure)

# def user_request(location=location_input, days=days_input, data=option_input):
#     print(location)
#     print(days)
#     print(data)
