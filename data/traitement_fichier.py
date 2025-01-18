import pandas as pd
import math
import numpy as np
import os

df = pd.read_csv('data/new_data.csv')

df = df.rename(columns={'c_ext (um^2)': 'C_ext'})
df = df.rename(columns={'c_sca (um^2)': 'C_sca'})


df_660 = df[df.iloc[:, 0] == 660]
df_660 = df_660.reset_index(drop=True)
df_467 = df[df.iloc[:, 0] == 467]
df_467 = df_467.reset_index(drop=True)
df_530 = df[df.iloc[:, 0] == 530]
df_530 = df_530.reset_index(drop=True)

#MEC dans les 3 df
df_660['MEC_660'] = df_660['C_ext'] / df_660['mass_total  (g)'] 
df_530['MEC_530'] = df_530['C_ext'] / df_530['mass_total  (g)'] 
df_467['MEC_467'] = df_467['C_ext'] / df_467['mass_total  (g)'] 


#CBAC dans les 3 df
df_660['Cbac_660']=df_660['C_sca'] / 4*math.pi 
df_530['Cbac_530']=df_530['C_sca'] / 4*math.pi
df_467['Cbac_467']=df_467['C_sca'] / 4*math.pi

#LR dans les 3 df
df_660['LR_660'] = df_660['C_ext'] / df_660['Cbac_660']
df_530['LR_530'] = df_530['C_ext'] / df_530['Cbac_530']
df_467['LR_467'] = df_467['C_ext'] / df_467['Cbac_467']


#MBC dans les 3 df
df_660['MBC_660'] = df_660['MEC_660']/df_660['LR_660'] 
df_530['MBC_530'] = df_530['MEC_530']/df_530['LR_530']
df_467['MBC_467'] = df_467['MEC_467']/df_467['LR_467'] 



last_index_660 = df[df.iloc[:, 0] == 660].index[-1]
df_new= df.loc[:last_index_660, :] #suppression des lignes à partir de la derniere observation de lambda=660nm
df_new=df_new.iloc[:, 1:] #suppression colonne des longueurs d'onde


# Rajout des colonnes calculées dans le nouveau set de données
df_new['MEC_660'] = df_660['MEC_660']
df_new['MEC_530'] = df_530['MEC_530']
df_new['MEC_467'] = df_467['MEC_467']

df_new['Cbac_660'] = df_660['Cbac_660']
df_new['Cbac_530'] = df_530['Cbac_530']
df_new['Cbac_467'] = df_467['Cbac_467']

df_new['LR_660'] = df_660['LR_660']
df_new['LR_530'] = df_530['LR_530']
df_new['LR_467'] = df_467['LR_467']

df_new['MBC_660'] = df_660['MBC_660']
df_new['MBC_530'] = df_530['MBC_530']
df_new['MBC_467'] = df_467['MBC_467']


#CR dans les 3 df
df_new['CR_660_530'] = df_660['Cbac_660']/df_530['Cbac_530']
df_new['CR_530_467'] = df_530['Cbac_530']/df_467['Cbac_467'] 
df_new['CR_467_660'] = df_467['Cbac_467']/df_660['Cbac_660'] 


#BAE dans les 3 df
df_new['BAE_660_530'] = np.log(df_new['CR_660_530'])/np.log(660/530) 
df_new['BAE_530_467'] = np.log(df_new['CR_530_467'])/np.log(530/467)  
df_new['BAE_467_660'] = np.log(df_new['CR_467_660'])/np.log(467/660) 



#Conversion des colonnes des masses de grammes en fentogrammes
df_new['mass_bc (g)'] = df_new['mass_bc (g)'] * 1e15
df_new['mass_organics (g)'] = df_new['mass_organics (g)'] * 1e15
df_new['mass_total  (g)'] = df_new['mass_total  (g)'] * 1e15

df_new = df_new.rename(columns={'mass_total  (g)': 'mass_total  (fg)'})	
df_new = df_new.rename(columns={'mass_organics (g)': 'mass_organics (fg)'})
df_new = df_new.rename(columns={'mass_bc (g)': 'mass_bc (fg)'})

#Enregistrement
df_new.to_csv('new_data_modifié.csv', index=False)
