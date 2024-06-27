import sys
import os
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            model=load_object(file_path=model_path)
            preds=model.predict(features)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)

class CustomData:
    def __init__(self, symptom1, symptom2, symptom3, symptom4):
        self.symptoms = [symptom1, symptom2, symptom3, symptom4]

    def get_data_as_one_hot_encoding(self, symptoms_dict):
        try:
            input_vector = np.zeros(len(symptoms_dict))
            for item in self.symptoms:
                try:
                    input_vector[symptoms_dict[item]]=1
                except:
                    pass
            
            return input_vector.reshape(1,-1)
        
        except Exception as e:
            raise CustomException(e, sys)