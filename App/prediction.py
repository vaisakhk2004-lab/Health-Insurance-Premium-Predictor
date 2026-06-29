import pandas as pd
from joblib import load
high_age_model=load("models\\high_age_model.joblib")
low_age_model=load("models\\low age model.joblib")
high_scale=load("models\\scaler_high_age.joblib")
low_scale=load("models\\scaler_young.joblib")
def preprocess_input(input_dict):
    columns=['age', 'number_of_dependants', 'income_level', 'income_lakhs','insurance_plan',
       'genetical_risk','normalised_score', 'gender_Male', 'region_Northwest',
       'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
       'bmi_category_Obesity', 'bmi_category_Overweight',
       'bmi_category_Underweight', 'smoking_status_Occasional',
       'smoking_status_Regular', 'employment_status_Salaried',
       'employment_status_Self-Employed']

    insurance_plan_encoding= {'Bronze':1,'Silver':2,'Gold':3}
    df=pd.DataFrame(0,columns = columns,index=[0])
    for key,value in input_dict.items():
        if key== 'insurance_plan':
           df['insurance_plan'] = insurance_plan_encoding.get(value)
        if key=='age':
            df['age'] = value
        if key=='gender' and value=='male':
            df['gender_Male']=1

        elif key == 'region':
            if value == 'Northwest':
                df['region_Northwest'] = 1
            elif value == 'Southeast':
                df['region_Southeast'] = 1
            elif value == 'Southwest':
                df['region_Southwest'] = 1
            # Northeast -> all region columns remain 0

        elif key == 'marital_status':
            if value == 'Unmarried':
                df['marital_status_Unmarried'] = 1
            # Married -> 0

        elif key == 'bmi_category':
            if value == 'Obesity':
                df['bmi_category_Obesity'] = 1
            elif value == 'Overweight':
                df['bmi_category_Overweight'] = 1
            elif value == 'Underweight':
                df['bmi_category_Underweight'] = 1
            # Normal -> 0

        elif key == 'smoking_status':
            if value == 'Occasional':
                df['smoking_status_Occasional'] = 1
            elif value == 'Regular':
                df['smoking_status_Regular'] = 1
            # No Smoking -> 0

        elif key == 'employment_status':
            if value == 'Salaried':
                df['employment_status_Salaried'] = 1
            elif value == 'Self-Employed':
                df['employment_status_Self-Employed'] = 1
    df['normalised_score'] = calculate_risk_scores(input_dict['medical_history'])
    df=scaling(input_dict['age'],df)
    return df

def calculate_risk_scores(medical_history):
    risk_scores = {
        'diabetes': 6,
        'heart disease': 8,
        'high blood pressure': 6,
        'thyroid': 5,
        'no disease': 0,
        'none': 0
    }

    # Values from training
    min_score = 0
    max_score = 14
    total_score = 0

    diseases = [d.strip().lower() for d in medical_history.split('&')]

    for disease in diseases:
        total_score += risk_scores.get(disease, 0)

    normalised_score = (total_score - min_score) / (max_score - min_score)

    return normalised_score

def scaling(age,df):
    if age<=25:
       scaler=low_scale
    else:
        scaler=high_scale
    cols_to_scale=scaler['columns']
    scaler_used=scaler['scaler']
    df['income_level']=None
    df[cols_to_scale]=scaler_used.transform(df[cols_to_scale])
    df.drop(columns='income_level',inplace=True)
    return df
def predict(input_dict):
    input_df=preprocess_input(input_dict)
    if input_dict['age']<=25:
        predictor=low_age_model.predict(input_df)
    else:
        predictor=high_age_model.predict(input_df)
    return int(predictor[0])
