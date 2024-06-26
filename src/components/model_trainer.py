import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from dataclasses import dataclass 

import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_data_path, test_data_path):
        try:
            logging.info("Getting data from train and test sets")
            train_array = pd.read_csv(train_data_path)
            test_array = pd.read_csv(test_data_path)

            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            #Encoding the target column
            label_encoder = LabelEncoder()
            y_e_train = label_encoder.fit_transform(y_train)
            y_e_test = label_encoder.fit_transform(y_test)

            models = {
                "Logictic Regression" : LogisticRegression(),
                "Logistic Regression with L1 Regularization": LogisticRegression(penalty='l1', solver='liblinear'),
                "Logistic Regression with L2 Regularization": LogisticRegression(penalty='l2'),
                "K-Neighbors Classifier": KNeighborsClassifier(),
                "Decision Tree Classifier": DecisionTreeClassifier(),
                "Random Forest Classifier": RandomForestClassifier(),
                "XGBClassifier": XGBClassifier(), 
                'MultinomialNB': MultinomialNB(),
                'SVC': SVC(kernel='linear')
            }

            model_report = self.evaluate_models(X_train=X_train,y_train=y_e_train,X_test=X_test,y_e_test=y_test,models=models)
            
            sorted_model_report = model_report.sort_values(by=['Accuracy', 'F1 Score'], ascending=[False, False])
            best_model_name = sorted_model_report.iloc[0]['Model Name']
            best_model_accuracy = sorted_model_report.iloc[0]['Accuracy']
            best_model_f1score = sorted_model_report.iloc[0]['F1 Score']

            if best_model_accuracy<0.7 or best_model_f1score<0.7:
                raise CustomException("No best model found")
            
            best_model = models[best_model_name]
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            logging.info("Saved the pickle for best model")

        except CustomException as e:
            raise CustomException(e, sys)

    def evaluate_models(X_train, y_train,X_test,y_test,models):
        try:
            results = []

            for i in range(len(list(models))):
                model = list(models.values())[i]
                model.fit(X_train, y_train)
                y_test_pred= model.predict(X_test)

                accuracy = accuracy_score(y_test, y_test_pred)
                f1score = f1_score(y_test, y_test_pred, average='macro')

                results.append({
                    'Model Name': list(models.key())[i],
                    'Accuracy': accuracy,
                    'F1 Score': f1score
                })
                        
            return pd.DataFrame(results)
        
        except Exception as e:
            raise CustomException(e, sys)
        
