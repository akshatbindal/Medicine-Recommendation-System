import os
import sys

import numpy as np 
import pandas as pd
import pickle

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

    precautions = pd.read_csv("artifacts/precautions_df.csv")
    workout = pd.read_csv("artifacts/workout_df.csv")
    description = pd.read_csv("artifacts/description.csv")
    medications = pd.read_csv('artifacts/medications.csv')
    diets = pd.read_csv("artifacts/diets.csv")

    desc = description[description['Disease'] == disease]['Description']
    desc = " ".join([w for w in desc])

    pre = precautions[precautions['Disease'] == disease][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]
    pre = [col for col in pre.values]

    med = medications[medications['Disease'] == disease]['Medication'].to_list()

    die = diets[diets['Disease'] == disease]['Diet'].to_list()

    wrkout = workout[workout['disease'] == disease] ['workout'].tolist()

    return desc,pre,med,die,wrkout
    
