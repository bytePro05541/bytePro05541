import pandas as pd
import numpy as np

pd1 = pd.read_csv("/Users/ritambharac/Documents/SCU/OMIS3000/Code/diabetes_012_health_indicators_final.csv")

pd2=pd.DataFrame(pd1)
## Education high school or less, some college, graduate
count0 =0
count1 = 0 
count2 = 0 
for inx in pd2['Education']:
    if inx < 5:
        count2 = count2+1
    elif inx==5:
        count1 = count1+1
    elif inx==6:
        count0 = count0+1
print(count0, count1, count2)

X_high_school_or_less = []
X_Some_College = []
X_Graduate = []

for Education in  pd2['Education']:
    if Education<5:
        X_high_school_or_less.append(1)
        X_Some_College.append(0)
        X_Graduate.append(0)
    elif Education ==5:
        X_high_school_or_less.append(0)
        X_Some_College.append(1)
        X_Graduate.append(0)
    elif Education == 6:
        X_high_school_or_less.append(0)
        X_Some_College.append(0)
        X_Graduate.append(1)

pd2['X_high_school_or_less'] = X_high_school_or_less
pd2['X_Some_College'] = X_Some_College
pd2['X_Graduate'] = X_Graduate

pd2.to_csv("/Users/ritambharac/Documents/SCU/OMIS3000/Code/diabetes_012_health_indicators_final.csv", index = False)

pd1=pd.DataFrame(pd2)

print (pd1.columns.tolist())

pd1 = pd1[['HighBP', 'HighChol', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'DiffWalk', 'Sex', 'Age', 'X_Age_less_45', 'X_Age_45_to_70', 'X_Age_70_up', 'Education', 'X_high_school_or_less', 'X_Some_College', 'X_Graduate', 'Income', 'Diabetes_012']]

print (pd1.columns.tolist())

pd1.to_csv("/Users/ritambharac/Documents/SCU/OMIS3000/Code/diabetes_012_health_indicators_final.csv", index = False)
