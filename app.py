from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from src.pipeline.predict import CustomData,PredictPipeline
from src.utils import other_results

app=Flask(__name__)

df = pd.read_csv("artifacts/Training.csv")
symptoms_list=df.columns[:-1].to_list()
symptoms_dict = {col: idx for idx, col in enumerate(df.columns[:-1])}
target_features = df['prognosis']

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html', symptoms_list=symptoms_list)
    else:

        data=CustomData(
            symptom1=request.form.get('symptom1'),
            symptom2=request.form.get('symptom2'),
            symptom3=request.form.get('symptom3'),
            symptom4=request.form.get('symptom4'),
        )
        pred_df=data.get_data_as_one_hot_encoding(symptoms_dict=symptoms_dict)
        predict_pipeline=PredictPipeline()
        result=predict_pipeline.predict(pred_df)

        label_encoder= LabelEncoder()
        label_encoder.fit(target_features)
        predicted_disease = label_encoder.inverse_transform(result)[0]

        description,precaution,medicine,diet,workout= other_results(predicted_disease)


        return render_template('home.html',predicted_disease=predicted_disease,
                               description=description, precaution=precaution, medicine=medicine,
                               diet=diet, workout=workout)
    
if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)