import pandas as pd
import numpy as np

pd1 = pd.read_csv("/Users/ritambharac/Documents/SCU/OMIS3000/Code/diabetes_012_health_indicators_final.csv")

pd2=pd.DataFrame(pd1)
## Age < 45, 45 -69, 70 >
count0 =0
count1 = 0 
count2 = 0 
for inx in pd2['Age']:
    if inx < 5:
        count2 = count2+1
    elif 5<inx <10:
        count1 = count1+1
    else:
        count0 = count0+1
print(count0, count1, count2)

X_Age_less_45 = []
X_Age_45_to_70 = []
X_Age_70_up = []

for Age in  pd2['Age']:
    if Age<5:
        X_Age_less_45.append(1)
        X_Age_45_to_70.append(0)
        X_Age_70_up.append(0)
    elif 5 < Age < 10:
        X_Age_less_45.append(0)
        X_Age_45_to_70.append(1)
        X_Age_70_up.append(0)
    else:
        X_Age_less_45.append(0)
        X_Age_45_to_70.append(0)
        X_Age_70_up.append(1)

pd2['X_Age_less_45'] = X_Age_less_45
pd2['X_Age_45_to_70'] = X_Age_45_to_70
pd2['X_Age_70_up'] = X_Age_70_up

pd2.to_csv("/Users/ritambharac/Documents/SCU/OMIS3000/Code/diabetes_012_health_indicators_final.csv", index = False)

pd1=pd.DataFrame(pd2)

##print (pd1.columns.tolist())

pd1 = pd1[['HighBP', 'HighChol', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'DiffWalk', 'Sex', 'Age',  'X_Age_less_45', 'X_Age_45_to_70', 'X_Age_70_up', 'Education', 'Income','Diabetes_012']]

print (pd1.columns.tolist())
pd1.to_csv("/Users/ritambharac/Documents/SCU/OMIS3000/Code/diabetes_012_health_indicators_final.csv", index = False)
