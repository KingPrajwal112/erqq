from django.shortcuts import render
from joblib import load
import pickle
#model=load("./SaveModels/model12")
model=pickle.load(open('/SaveModels/ee','rb'))
def predictor(request):
    return render(request,"index.html")

def formInfo(request):
    Age=int(request.GET["age"])
    Sex=int(request.GET["sex"])
    chest_pain=int(request.GET["chest_pain"])
    bp=int(request.GET["bp"])
    choresterol=int(request.GET["choresterol"])
    fbp=int(request.GET["fbp"])
    electrograph=int(request.GET["electrograph"])
    max=int(request.GET["max"])
    angina=int(request.GET["angina"])
    oldpeak=int(request.GET["oldpeak"])
    slope=int(request.GET["slope"])
    vessels=int(request.GET["vessels"])
    thal=int(request.GET["thal"])
    

    kk=model.predict([[Age,Sex,chest_pain,bp,choresterol,fbp,electrograph,max,angina,oldpeak,slope,vessels,thal]])
    return render(request,"result.html",{"result":kk})
