import os
import sys

import numpy as np 
import pandas as pd
import pickle
import ast

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def other_results(disease):
    try:
        precautions = pd.read_csv("artifacts/precautions_df.csv")
        workout = pd.read_csv("artifacts/workout_df.csv")
        description = pd.read_csv("artifacts/description.csv")
        medications = pd.read_csv('artifacts/medications.csv')
        diets = pd.read_csv("artifacts/diets.csv")

        desc = description[description['Disease'] == disease]['Description']
        desc = " ".join([w for w in desc])

        pre = precautions.loc[precautions['Disease'] == disease, ['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values.tolist()[0]

        med = medications[medications['Disease'] == disease]['Medication'].iloc[0]
        med = ast.literal_eval(med) 

        die = diets[diets['Disease'] == disease]['Diet'].iloc[0]
        die = ast.literal_eval(die)

        wrkout = workout[workout['disease'] == disease] ['workout'].tolist()

        return desc,pre,med,die,wrkout
    
    except Exception as e:
        raise CustomException(e,sys)
