import numpy as np
import pandas as pd
import pickle
def myinput_network(text):
    columns = ['obscene','insult','toxic','severe_toxic','identity_hate','threat']
    l=[text]
    f='vect'
    vect= pickle.load(open(f, 'rb'))
    user_data = vect.transform(l)
    results2 = pd.DataFrame(columns=columns)
    mymodels={}
    for i in range(6):
        filename='model_'+str(i)
        mymodels[columns[i]]= pickle.load(open(filename, 'rb'))
    for i in range(6):
        user_results = mymodels[columns[i]].predict_proba(user_data)[:,1]
        results2[columns[i]] = user_results
    x = columns
    return results2.iloc[0].values,x