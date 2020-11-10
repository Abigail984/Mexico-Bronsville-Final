import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

#Se le el csv de Fronteras, que contiene a US-Canada Border y a US-Mexico Border del año 1996 a febrero de 2020
fronteras= pd.read_csv('front2.csv')

#Se seleccionan los datos que se desean
s_Cal=fronteras["Port Name"]== "Brownsville"
es_PD=fronteras["Measure"]=="Pedestrians"

#Se cambia el formato de la fecha
fronteras["Date"]= pd.to_datetime(fronteras["Date"], format ="%m/%d/%Y")
es_2019=fronteras["Date"].dt.strftime("%Y")=="2019"
es_2018=fronteras["Date"].dt.strftime("%Y")=="2018"
es_2017=fronteras["Date"].dt.strftime("%Y")=="2017"
es_2016=fronteras["Date"].dt.strftime("%Y")=="2016"
es_2015=fronteras["Date"].dt.strftime("%Y")=="2015"
es_2014=fronteras["Date"].dt.strftime("%Y")=="2014"
es_2013=fronteras["Date"].dt.strftime("%Y")=="2013"
es_2012=fronteras["Date"].dt.strftime("%Y")=="2012"
es_2011=fronteras["Date"].dt.strftime("%Y")=="2011"
es_2010=fronteras["Date"].dt.strftime("%Y")=="2010"
es_2009=fronteras["Date"].dt.strftime("%Y")=="2009"
es_2008=fronteras["Date"].dt.strftime("%Y")=="2008"
es_2007=fronteras["Date"].dt.strftime("%Y")=="2007"
es_2006=fronteras["Date"].dt.strftime("%Y")=="2006"
es_2005=fronteras["Date"].dt.strftime("%Y")=="2005"
es_2004=fronteras["Date"].dt.strftime("%Y")=="2004"
es_2003=fronteras["Date"].dt.strftime("%Y")=="2003"
es_2002=fronteras["Date"].dt.strftime("%Y")=="2002"
es_2001=fronteras["Date"].dt.strftime("%Y")=="2001"
es_2000=fronteras["Date"].dt.strftime("%Y")=="2000"

es_enero=fronteras["Date"].dt.strftime("%m")=="01"
es_febrero=fronteras["Date"].dt.strftime("%m")=="02"
es_marzo=fronteras["Date"].dt.strftime("%m")=="03"
es_abril=fronteras["Date"].dt.strftime("%m")=="04"
es_mayo=fronteras["Date"].dt.strftime("%m")=="05"
es_junio=fronteras["Date"].dt.strftime("%m")=="06"
es_julio=fronteras["Date"].dt.strftime("%m")=="07"
es_agosto=fronteras["Date"].dt.strftime("%m")=="08"
es_septiembre=fronteras["Date"].dt.strftime("%m")=="09"
es_octubre=fronteras["Date"].dt.strftime("%m")=="10"
es_noviembre=fronteras["Date"].dt.strftime("%m")=="11"
es_diciembre=fronteras["Date"].dt.strftime("%m")=="12"

#Se agrupan los datos de 5 en 5 años por mes
frontCalenede5en5=fronteras[s_Cal & (es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_enero]
frontCalfebde5en5=fronteras[s_Cal & (es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_febrero]
frontCalmarde5en5=fronteras[s_Cal & (es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_marzo]
frontCalabrde5en5=fronteras[s_Cal & (es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_abril]
frontCalmayde5en5=fronteras[s_Cal & (es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_mayo]
frontCaljunde5en5=fronteras[s_Cal & (es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_junio]
frontCaljulde5en5=fronteras[s_Cal & (es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_julio]
frontCalagode5en5=fronteras[s_Cal & (es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_agosto]
frontCalsepde5en5=fronteras[s_Cal & (es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_septiembre]
frontCaloctde5en5=fronteras[s_Cal & (es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_octubre]
frontCalnovde5en5=fronteras[s_Cal & (es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_noviembre]
frontCaldicde5en5=fronteras[s_Cal & (es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_diciembre]

anioenede5en5=frontCalenede5en5.describe()
aniofebde5en5=frontCalfebde5en5.describe()
aniomarde5en5=frontCalmarde5en5.describe()
anioabrde5en5=frontCalabrde5en5.describe()
aniomayde5en5=frontCalmayde5en5.describe()
aniojunde5en5=frontCalmayde5en5.describe()
aniojulde5en5=frontCaljulde5en5.describe()
anioagode5en5=frontCalagode5en5.describe()
aniosepde5en5=frontCalsepde5en5.describe()
aniooctde5en5=frontCaloctde5en5.describe()
anionovde5en5=frontCalnovde5en5.describe()
aniodicde5en5=frontCaldicde5en5.describe()

# Se muestra el describe() de cada mes de 5 en 5 años
print(anioenede5en5)
print(aniofebde5en5)
print(aniomarde5en5)
print(anioabrde5en5)
print(aniomayde5en5)
print(aniojunde5en5)
print(aniojulde5en5)
print(anioagode5en5)
print(aniosepde5en5)
print(aniooctde5en5)
print(anionovde5en5)
print(aniodicde5en5)

frontCalene19 = fronteras[s_Cal & es_2019 & es_PD & es_enero]
frontCalfeb19 = fronteras[s_Cal & es_2019 & es_PD & es_febrero]
frontCalmar19 = fronteras[s_Cal & es_2019 & es_PD & es_marzo]
frontCalabr19 = fronteras[s_Cal & es_2019 & es_PD & es_abril]
frontCalmay19 = fronteras[s_Cal & es_2019 & es_PD & es_mayo]
frontCaljun19 = fronteras[s_Cal & es_2019 & es_PD & es_junio]
frontCaljul19 = fronteras[s_Cal & es_2019 & es_PD & es_julio]
frontCalago19 = fronteras[s_Cal & es_2019 & es_PD & es_agosto]
frontCalsep19 = fronteras[s_Cal & es_2019 & es_PD & es_septiembre]
frontCaloct19 = fronteras[s_Cal & es_2019 & es_PD & es_octubre]
frontCalnov19 = fronteras[s_Cal & es_2019 & es_PD & es_noviembre]
frontCaldic19 = fronteras[s_Cal & es_2019 & es_PD & es_diciembre]

anioene19=frontCalene19.describe()
aniofeb19=frontCalfeb19.describe()
aniomar19=frontCalmar19.describe()
anioabr19=frontCalabr19.describe()
aniomay19=frontCalmay19.describe()
aniojun19=frontCaljun19.describe()
aniojul19=frontCaljul19.describe()
anioago19=frontCalago19.describe()
aniosep19=frontCalsep19.describe()
aniooct19=frontCaloct19.describe()
anionov19=frontCalnov19.describe()
aniodic19=frontCaldic19.describe()

# Se muestra el describe() de cada mes del 2019 
print(anioene19)
print(aniofeb19)
print(aniomar19)
print(anioabr19)
print(aniomay19)
print(aniojun19)
print(aniojul19)
print(anioago19)
print(aniosep19)
print(aniooct19)
print(anionov19)
print(aniodic19)

# Se muestran las gráficas de 5 en 5 años

#x=frontCalenede5en5['Date']
#y=frontCalenede5en5['Value']
#plt.plot(x,y)
#plt.show()
#plt.savefig('MexBrownsville2000-2005-2010-2015-2018- enero.png')

#x=frontCalfebde5en5['Date']
#y=frontCalfebde5en5['Value']
#plt.plot(x,y)
#plt.show()
#plt.savefig('MexBrownsville2000-2005-2010-2015-2018- febrero.png')

#x=frontCalmarde5en5['Date']
#y=frontCalmarde5en5['Value']
#plt.plot(x,y)
#plt.show()
#plt.savefig('MexBrownsville2000-2005-2010-2015-2018- marzo.png')


#x=frontCalabrde5en5['Date']
#y=frontCalabrde5en5['Value']
#plt.plot(x,y)
#plt.show()
#plt.savefig('MexBrownsville2000-2005-2010-2015-2018- abril.png')


#x=frontCalmayde5en5['Date']
#y=frontCalmayde5en5['Value']
#plt.plot(x,y)
#plt.show()
#plt.savefig('MexBrownsville2000-2005-2010-2015-2018- mayo.png')


#x=frontCaljunde5en5['Date']
#y=frontCaljunde5en5['Value']
#plt.plot(x,y)
#plt.show()
#plt.savefig('MexBrownsville2000-2005-2010-2015-2018- junio.png')


#x=frontCaljulde5en5['Date']
#y=frontCaljulde5en5['Value']
#plt.plot(x,y)
#plt.show()
#plt.savefig('MexBrownsville2000-2005-2010-2015-2018- julio.png')


#x=frontCalagode5en5['Date']
#y=frontCalagode5en5['Value']
#plt.plot(x,y)
#plt.show()
#plt.savefig('MexBrownsville2000-2005-2010-2015-2018- agosto.png')


#x=frontCalsepde5en5['Date']
#y=frontCalsepde5en5['Value']
#plt.plot(x,y)
#plt.show()
#plt.savefig('MexBrownsville2000-2005-2010-2015-2018- septiembre.png')


#x=frontCaloctde5en5['Date']
#y=frontCaloctde5en5['Value']
#plt.plot(x,y)
#plt.show()
#plt.savefig('MexBrownsville2000-2005-2010-2015-2018- octubre.png')


#x=frontCalnovde5en5['Date']
#y=frontCalnovde5en5['Value']
#plt.plot(x,y)
#plt.show()
#plt.savefig('MexBrownsville2000-2005-2010-2015-2018- noviembre.png')


x=frontCaldicde5en5['Date']
y=frontCaldicde5en5['Value']
plt.plot(x,y)
#plt.show()
plt.savefig('MexBrownsville2000-2005-2010-2015-2018- diciembre.png')

