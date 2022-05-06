import pandas as pd
import numpy as np

pd1 = pd.read_csv("/Users/ritambharac/Documents/SCU/OMIS3000/Code/diabetes_012_health_indicators_final.csv")

pd2=pd.DataFrame(pd1)
## Income 35000 or less, 35000 to 75000, 75000 or more
count0 =0
count1 = 0 
count2 = 0 
for inx in pd2['Income']:
    if inx < 6:
        count2 = count2+1
    elif 5<inx<7:
        count1 = count1+1
    elif inx==8:
        count0 = count0+1
print(count0, count1, count2)

X_Income_35000_or_less = []
X_Income_35000_to_75000 = []
X_Income_75000_or_more = []

for Education in  pd2['Income']:
    if Education<6:
        X_Income_35000_or_less.append(1)
        X_Income_35000_to_75000.append(0)
        X_Income_75000_or_more.append(0)
    elif 5<Education<8 :
        X_Income_35000_or_less.append(0)
        X_Income_35000_to_75000.append(1)
        X_Income_75000_or_more.append(0)
    elif Education == 8:
        X_Income_35000_or_less.append(0)
        X_Income_35000_to_75000.append(0)
        X_Income_75000_or_more.append(1)

pd2['X_Income_35000_or_less'] = X_Income_35000_or_less
pd2['X_Income_35000_to_75000'] = X_Income_35000_to_75000
pd2['X_Income_75000_or_more'] = X_Income_75000_or_more

pd2.to_csv("/Users/ritambharac/Documents/SCU/OMIS3000/Code/diabetes_012_health_indicators_final.csv", index = False)

pd1=pd.DataFrame(pd2)

print (pd1.columns.tolist())

pd1 = pd1[['HighBP', 'HighChol', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'DiffWalk', 'Sex', 'Age', 'X_Age_less_45', 'X_Age_45_to_70', 'X_Age_70_up', 'Education', 'X_high_school_or_less', 'X_Some_College', 'X_Graduate', 'Income', 'X_Income_35000_or_less', 'X_Income_35000_to_75000', 'X_Income_75000_or_more', 'Diabetes_012']]

print (pd1.columns.tolist())

pd1.to_csv("/Users/ritambharac/Documents/SCU/OMIS3000/Code/diabetes_012_health_indicators_final.csv", index = False)
