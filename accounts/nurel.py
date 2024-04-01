
#from flask import Flask,render_template,request
import joblib
import numpy as np
from keras.models import load_model
from keras import backend as K 


model = load_model('accounts/eximius1.model')

scaler_data = joblib.load('accounts/scaler_data.sav')
scaler_target = joblib.load('accounts/scaler_target.sav')




def ann(age,gender,bmi,situation_of_the_patient,sergery_type,seriousness_of_the_surgery):
#def ann():
	#name=result['name']
	#gender=float(result['gender'])
	gender = 1
	#age=float(result['age'])
	age = 34
	#bmi=float(result['BMI'])
	bmi = 26
	#situation_of_the_patient=float(result['SOP'])
	situation_of_the_patient = 3
	#sergery_type =float(result['ST'])
	sergery_type=3
	#seriousness_of_the_surgery=float(result['SOS'])
	seriousness_of_the_surgery = 1


	test_data = np.array([age,gender,bmi,situation_of_the_patient,sergery_type,seriousness_of_the_surgery]).reshape(1,-1)

	test_data = scaler_data.transform(test_data)

	prediction = model.predict(test_data)

	prediction = scaler_target.inverse_transform(prediction)

	print(prediction)

	return prediction
		
	#resultdic = {"name":name,"surgery_time": prediction[0][0]} 

	#return render_template('patient_results.html',results=resultdic)

#pred = ann()
#print(pred)





