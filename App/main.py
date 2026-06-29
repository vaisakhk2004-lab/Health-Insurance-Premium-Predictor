import streamlit as st
from prediction import predict

st.set_page_config(
    page_title="Health Insurance Price Predictor",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Health Insurance Price Predictor")
st.write("Enter the customer details to predict the insurance premium.")

st.divider()

col1, col2 ,col3= st.columns(3)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30,
        step=1
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    region = st.selectbox(
        "Region",
        ["Northwest",
         "Northeast",
         "Southwest",
         "Southeast"]
    )

    marital_status = st.selectbox(
        "Marital Status",
        ["Married", "Unmarried"]
    )
with col2:
    number_of_dependants = st.number_input(
        "Number of Dependants",
        min_value=0,
        max_value=10,
        value=0,
        step=1
    )

    bmi_category = st.selectbox(
        "BMI Category",
        [
            "Underweight",
            "Normal",
            "Overweight",
            "Obesity"
        ]
    )



    smoking_status = st.selectbox(
        "Smoking Status",
        [
            "No Smoking",
            "Occasional",
            "Regular"
        ]
    )

    employment_status = st.selectbox(
        "Employment Status",
        [
            "Salaried",
            "Self-Employed",
            "Freelancer"
        ]
    )



with col3:
    income_lakhs = st.number_input(
        "Annual Income (Lakhs)",
        min_value=1.0,
        max_value=100.0,
        value=10.0,
        step=0.5
    )

    medical_history = st.selectbox(
        "Medical History",
        ['Diabetes','High blood pressure', 'No Disease','Diabetes & High blood pressure',
               'Thyroid','Heart disease','High blood pressure & Heart disease','Diabetes & Thyroid',
              'Diabetes & Heart disease']

    )

    insurance_plan = st.selectbox(
        "Insurance Plan",
        [
            "Bronze",
            "Silver",
            "Gold"

        ]
    )
    genetical_risk = st.number_input(
        "Genetical Risk",
        value=0,  # or your calculated value
        step=1,
        disabled=True
    )

st.divider()

button= st.button(
    "Predict Insurance Premium",
    use_container_width=True
)
input_data = {
        "age": age,
        "gender": gender,
        "region": region,
        "marital_status": marital_status,
        "number_of_dependants": number_of_dependants,
        "bmi_category": bmi_category,
        "smoking_status": smoking_status,
        "employment_status": employment_status,
        "income_lakhs": income_lakhs,
        "medical_history": medical_history,
        "insurance_plan": insurance_plan
    }

if button:
   predicted=predict(input_data)
   st.success(f'Predicted Insurance Premium: {predicted}')



    # st.write("### Input Data")
    # st.json(input_data)

    # prediction = model.predict(...)
    # st.success(f"Predicted Premium: ₹ {prediction[0]:,.2f}")
