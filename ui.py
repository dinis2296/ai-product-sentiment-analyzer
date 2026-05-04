
import streamlit as st
from predict import predict

st.title("Hacker News Post Predictor")

title = st.text_input("Enter a post title:")

if st.button("Predict"):
    prob = predict(title)

    st.write(f"Probability: {prob:.3f}")

    if prob > 0.5:
        st.success("High engagement")
    else:
        st.error("Low engagement")
