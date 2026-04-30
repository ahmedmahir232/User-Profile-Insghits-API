import streamlit as st
import requests
import pandas as pd

st.title("User Profile Insights")

url = "https://randomuser.me/api/?results=10"
response = requests.get(url)
data = response.json()["results"]

users = []

for user in data:
    users.append({
        "First Name": user["name"]["first"],
        "Last Name": user["name"]["last"],
        "Gender": user["gender"],
        "Age": user["dob"]["age"],
        "Country": user["location"]["country"],
        "Email": user["email"]
    })

df = pd.DataFrame(users)

st.dataframe(df)
