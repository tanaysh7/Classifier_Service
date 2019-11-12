# Reads pickled model and predicts for user

#Save first then use unpickled

import pickle
import os
import sklearn



vec=pickle.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vectorizer.pk'), 'rb'))
loaded_model = pickle.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'clf.pk'), 'rb'))

def predict(text):
    
    try:
        if loaded_model.predict(vec.transform([text]))[0]:
            
            return {
            "class" :"C",
            "probability_score":max(loaded_model.predict_proba(vec.transform([text]))[0])}
        else:
            return {"class" :"B",
            "probability_score":max(loaded_model.predict_proba(vec.transform([text]))[0])}
    except:
        return {
            "class" :"C",
            "probability_score":"0.6"}
