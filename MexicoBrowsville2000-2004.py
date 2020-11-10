import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

#Se le el csv de Fronteras, que contiene a US-Canada Border y a US-Mexico Border del año 1996 a febrero de 2020
#print('FRONTERAS')
fronteras = pd.read_csv('frontera.csv')



#Para convertir la fecha a formato de fecha (mm/dd/YYYY) mediante la función de pd.to_datetime
fronteras['Date'] = pd.to_datetime(fronteras['Date'],format='%m/%d/%Y')
#print(fronteras.dtypes)

#EJERCICIO - 2 -

#------------------------------------------------------------------------------------------------------------

#                                             2000 - 20004

#------------------------------------------------------------------------------------------------------------
#Se seleccionan los datos que sean del año 2000 al 2004,  tengan frontera US-Mexico Border y Port Name sea Brownsville

#mes x

#Se seleccionan los datos que correspondan con los años 2000, 2001, 2002, 2003, 2004
#fecha1 = fronteras["Date"].dt.strftime("%Y") == "2000"
fecha1 = fronteras["Date"].dt.strftime("%Y").isin(["2004","2003","2002","2002","2001"])
#Se seleccionan los datos que correspondan con Port Name = Brownsville
brow1 = fronteras["Port Name"] == "Brownsville"
#Se seleccionan los datos que correspondan con  Measure = Pedestrians 
ped1 = fronteras["Measure"] == "Pedestrians"
#Se seleccionan los datos que correspondan con el mes x, según sea el mes que se desean los datos
mes1 = fronteras["Date"].dt.strftime("%m") == "01"
#Se unen en la variable ejer21 todos los datos seleccionados anteriormente
ejer21 = fronteras[fecha1 & brow1 & ped1 & mes1]
print(ejer21)
#Mediante la función describe() podemos obtener la media
des1 = ejer21.describe()
print(des1)

















