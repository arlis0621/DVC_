import numpy as np
import os
import pandas as pd

data={'Name':['Alice','Bob','Charlie'],'Age':[25,30,45],'City':['New_York','Los Angeles','Chicago']
      

}
df=pd.DataFrame(data)

#adding new row to df
#n_row={'Name: 'V2, 'Age':20 ,'City':'City1'}
#df.loc[len(df.index)]=n_row

#adding new row to df for v3
# n_row1={'Name':'V3','Age':30,'City':'City1'}
# df.loc[len(df.index)]=n_row1
data_dir='data'
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)


