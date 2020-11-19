# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file


#Creating a new variable to store the value counts
loan_status = data['Loan_Status'].value_counts()

#Plotting bar plot
loan_status.plot(kind='bar')
plt.title('Loan Status', fontsize=17)


# Step 2
#Plotting an unstacked bar plot
property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar',stacked=False)
plt.title('Property and Loan', fontsize=18)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()




# Step 3
#Plotting a stacked bar plot
education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()

education_and_loan.plot(kind='bar',stacked=True)
plt.title('Education and Loan Status Correlation')
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate = data[data['Education']=='Graduate']

#Subsetting the dataframe based on 'Education' column
not_graduate = data[data['Education']=='Not Graduate']

#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind='density',label='Graduate')

#Plotting density plot for 'Not Graduate'
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')

#For automatic legend display


# Step 5
fig ,(ax_1,ax_2,ax_3)=plt.subplots(1,3, figsize=(20,7))

ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])
ax_1.set_xlabel('Applicant Income')
ax_1.set_ylabel('Loan Amount')
ax_1.set_title('Applicant Income',fontsize=18)

ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'],color='green')
ax_2.set_title('Coapplicant Income', fontsize=18)
ax_2.set_xlabel('Coapplicant Income')
ax_2.set_ylabel('Loan Amount')

data['TotalIncome']=data['CoapplicantIncome']+data['ApplicantIncome']
ax_3.scatter(data['TotalIncome'],data['LoanAmount'], color='red')
ax_3.set_title('Total Income', fontsize=18)
ax_3.set_xlabel('Total Income')
ax_3.set_ylabel('Loan Amount');


