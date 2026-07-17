import streamlit as st
from ai_engine import search_alarm

st.set_page_config(
    page_title="AI PLC Alarm Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI PLC Alarm Troubleshooting Assistant")

st.write("### Enter Alarm Code")

alarm_code = st.text_input(
    "Alarm Code",
    placeholder="Example: 1"
)

if st.button("Search Alarm"):

    if alarm_code == "":
        st.warning("Please enter Alarm Code")
        st.stop()

    result = search_alarm(alarm_code)

    if result is None:
        st.error("❌ Alarm Not Found")

    else:

        st.success(f"Alarm Found : {result['AlarmName']}")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Root Cause")
            st.info(result["Cause"])

            st.subheader("Electrical Check")
            st.write(result["ElectricalCheck"])

            st.subheader("Mechanical Check")
            st.write(result["MechanicalCheck"])

        with col2:
            st.subheader("Solution")
            st.success(result["Solution"])

            st.subheader("Recommended Spare")
            st.warning(result["SparePart"])
