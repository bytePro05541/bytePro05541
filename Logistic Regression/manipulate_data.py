import pandas as pd
import numpy as np

## Dependent variable
pd1 = pd.read_csv("/Users/ritambharac/Documents/SCU/OMIS3000/Code/diabetes_012_health_indicators_final.csv")

pd2=pd.DataFrame(pd1)

pd2['Diabetes_012'] = np.where(pd2['Diabetes_012'] == 2 ,1,0)

pd2.to_csv("/Users/ritambharac/Documents/SCU/OMIS3000/Code/diabetes_012_health_indicators_final.csv", index = False)




