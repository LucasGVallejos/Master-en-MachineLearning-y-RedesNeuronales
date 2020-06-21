import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

#para usar fondo oscuro
plt.style.use('seaborn-dark-palette')

data = pd.read_csv('wdi/Indicators.csv')
data.head()

filterArg = data['CountryName'] == 'Argentina'
data[filterArg].head()

#Cuantos Paises hay?
countries = data['CountryName'].unique().tolist()
print('Paises -> ', len(countries))

#Cuantos Codigos de paises hay?
codes = data['CountryCode'].unique().tolist()
print('Codigo de Paises -> ', len(codes))

#Cuantos Indicadores hay?
indicators = data['IndicatorName'].unique().tolist()
print('Indicadores -> ', len(indicators))

#De Cuantos Años tenemos informacion?
years = data['Year'].unique().tolist()
print('Años -> ', len(years))

#Dentro de que marco temporal nos estamos encontrando?
print('Desde -> ',min(years),' Hasta -> ',max(years))

####################
# GRAFICOS BASICOS #
####################

#Exploremos las emisiones de C02 de un pais
hist_indicator = 'CO2 emissions \(metric'
hist_countryCode = 'ARG'

mask1 = data['IndicatorName'].str.contains(hist_indicator)
mask2 = data['CountryCode'].str.contains(hist_countryCode)

#Aplicamos ambas mascaras
total_CO2 = data[mask1 & mask2]
total_CO2.tail()

#Cómo cambiaron las emisiones a lo largo del tiempo dentro de nuestro pais
years = total_CO2['Year']
co2 = total_CO2['Value']
#dibujamos grafico de barras.
#x: years
#y: co2
plt.bar(years,co2)
plt.show()

#Grafico de lineas
plt.plot(total_CO2['Year'],total_CO2['Value'])

#Label
plt.xlabel('Año')

#En Y puedo poner directamente el nombre del indicador
plt.ylabel('Emisiones de CO2 (Toneladas Métricas per capita)')

#Label en la figura
plt.title('Emisiones de CO2 en ARG')

#***************************
#*****IMPORTANTE************
#***************************
#Notar como podemos retorcar las escalas
plt.axis([1959, 2011, 0,5])

plt.show()

#Usaremos histogramas para explorar la distribucion de los valores
hist_data = total_CO2['Value']
hist_data

plt.hist(hist_data, 10, facecolor='green')

plt.xlabel(total_CO2['IndicatorName'].iloc[0])
plt.ylabel('# de Años')
plt.title('Histogram')

plt.grid(True)
plt.show()

#¿Como esta nuestro pais con respecto a otros paises?

#Seleccionamos todos los paises del año 2011
hist_year = 2011

mask1 = data['IndicatorName'].str.contains(hist_indicator)
mask2 = data['Year'].isin([hist_year])

#Aplicamos las masks
co2_2011 = data[mask1 & mask2]
co2_2011.head()

#subplots returns a touple with the Figure, axis attributes.
fig, ax = plt.subplots()

ax.annotate('ARG',
           xy=(20,5), xycoords='data',
            xytext=(23,30), textcoords = 'data',
            arrowprops=dict(arrowstyle='->',
                           connectionstyle='arc3'),
            )
plt.hist(co2_2011['Value'],10,normed=False,facecolor='green')

plt.xlabel(total_CO2['IndicatorName'].iloc[0])
plt.ylabel('# of Countries')
plt.title('Histogram of CO2 Emissions Per Capita')

plt.grid(True)
plt.show()

#Seleccionando el PIB de ARG
hist_indicator = 'GDP per capita \(constant 2005'
hist_country = 'ARG'

mask1 = data['IndicatorName'].str.contains(hist_indicator)
mask2 = data['CountryCode'].str.contains(hist_country)

gdp_stage = data[mask1 & mask2]
gdp_stage.head()

plt.plot(gdp_stage['Year'].values, gdp_stage['Value'].values)

plt.xlabel('Año')
plt.ylabel(gdp_stage['IndicatorName'].iloc[0])

plt.title('PBI Per Capita Argentina')

plt.show()

#Grafico de dispersion para comparar PIB vs CO2
#Para este 'Scatter plot' nos tenemos que asegurar que estamos viendo tanto PBI
#como en CO2 las mismas ventanas temporales

print('PIB Min Year -> ',gdp_stage['Year'].min(),'Max -> ', gdp_stage['Year'].max())
print('CO2 Min Year -> ',total_CO2['Year'].min(),'Max -> ', total_CO2['Year'].max())

gdp_stage_trunc = gdp_stage[gdp_stage['Year'] < 2012]
print(len(gdp_stage_trunc))
print(len(gdp_stage))

fig, axis = plt.subplots()

axis.yaxis.grid(True)
axis.set_title('CO2 Emissions vs GDP \(per capita)',fontsize=10)
axis.set_xlabel(gdp_stage_trunc['IndicatorName'].iloc[0], fontsize=10)
axis.set_ylabel(total_CO2['IndicatorName'].iloc[0],fontsize=10)

x = gdp_stage_trunc['Value']
y = total_CO2['Value']

axis.scatter(x,y)
plt.show()

np.corrcoef(x,y)
#Hay una fuerte relacion dado que se acercan los valores