# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

# Code starts here
data['Gender'].replace('-','Agender',inplace=True)

good_over_evil=pd.DataFrame(data['Alignment'].value_counts())

plt.figure(figsize=(10,5))
plt.bar(good_over_evil.index,good_over_evil.Alignment)
plt.title('Does Good Overpower Evil?', fontsize=17)
plt.show()

data['Intelligence'].corr(data['Combat'])
data['Strength'].corr(data['Combat'])

best_ofbest=data['Total'].quantile(0.99)

best_names=data.loc[data['Total']>=best_ofbest][['Name']]
super_best_names=list(best_names['Name'])




