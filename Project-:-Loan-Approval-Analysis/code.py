# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank = pd.read_csv(path)


#Code starts here

#Step1
categorical_var = bank.select_dtypes(include='object')
print(categorical_var)

numerical_var = bank.select_dtypes(include='number')
print(numerical_var)


#Step2
banks = bank.drop('Loan_ID',axis=1)
banks.isnull().sum()
bank_mode = banks.mode().iloc[0]
banks.fillna(bank_mode,inplace=True)
banks.isnull().sum()

#Step3
avg_loan_amount = banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'],values=['LoanAmount'],aggfunc='mean')
print(round(avg_loan_amount['LoanAmount'][1],2))

#Step4
loan_approved_se=banks.loc[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y'),['Loan_Status']].count()

loan_approved_nse=banks.loc[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y'),['Loan_Status']].count()

percentage_se = round((loan_approved_se/(banks['Loan_Status'].count()))*100,2)

percentage_nse = round((loan_approved_nse/(banks['Loan_Status'].count()))*100,2)

#Step5
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)
big_loan_term = loan_term[loan_term>=25].count()

#Step6
loan_groupby = banks.groupby('Loan_Status')['ApplicantIncome', 'Credit_History']

mean_values=loan_groupby.agg(np.mean)

print(mean_values.iloc[1,0])




