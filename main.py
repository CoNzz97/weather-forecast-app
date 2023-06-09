import streamlit as st


st.set_page_config(layout="wide", page_title="Home")

st.header("Weather Forecast")
location_input = st.text_input(label="Location")
days_input = st.slider(label="Forecast Days", min_value=0, max_value=5,
                       help="Select number of days to show")
option_input = st.selectbox(label="Select data to view", options=("Temperature", "Sky"))
st.subheader(f"{option_input} for the next {days_input} days in {location_input}")
st.line_chart(data=[1, 2, 5, 6, 2, 8, 0, 9])


def user_request(location=location_input, days=days_input, data=option_input):
    print(location)
    print(days)
    print(data)
