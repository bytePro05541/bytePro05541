
import pandas as pd
import numpy as np

f = open("/Users/ritambharac/Documents/SCU/OMIS3000/Code/diabetes_012_health_indicators_BRFSS2015.csv", "r")

pd1 = pd.read_csv(f)


pd2=pd.DataFrame(pd1)

pd2.drop(['CholCheck','AnyHealthcare','NoDocbcCost','GenHlth','MentHlth','PhysHlth'],axis=1, inplace = True)

pd2.to_csv("/Users/ritambharac/Documents/SCU/OMIS3000/Code/diabetes_012_health_indicators_final.csv", index = False)

pd1=pd.DataFrame(pd2)

print (pd1.columns.tolist())