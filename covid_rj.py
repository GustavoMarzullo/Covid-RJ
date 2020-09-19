#importando as bilbiotecas 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
plt.rcParams['figure.figsize'] = (13, 7) #deixando os gráficos mais compridos

#baixando os dados
print('Baixando os dados...')
df=pd.read_csv("http://painel.saude.rj.gov.br/arquivos/COVID.CSV",sep=';',\
               encoding='latin1', parse_dates=['dt_sintoma'], dayfirst=True, index_col='dt_sintoma')
print('\nDados baixados!')

df=df.sort_values('dt_sintoma') #botando os dados em ordem

#fazendo os casos totais e casos diários
tot=0
casos_acumulados=[]
casos=[]
for i in range(len(df)):
    tot+=1
    casos_acumulados.append(tot)
    casos.append(1)
    
df['casos_acumulados']=casos_acumulados
df['casos']=casos

hoje=datetime.today().strftime('%d-%m-%Y')
#plotando os casos acumulados
df['casos_acumulados'].plot(color='black')
plt.title('Casos Acumulados - RJ '+ str(datetime.today().strftime('%d-%m-%Y')))
plt.xlabel('Data')
plt.ylabel('Casos Acumulados')
plt.savefig('Casos Acumulados Rio de Janeiro '+ str(hoje),dpi=300)
plt.close()

#plotando os casos diários
df2=df.groupby(['dt_sintoma']).sum()
df2['casos'].plot(color='black')
plt.title('Casos Diários - RJ '+ str(datetime.today().strftime('%d-%m-%Y')))
plt.xlabel('Data')
plt.ylabel('Casos Diários')
plt.savefig('Casos Diários Rio de Janeiro '+ str(hoje),dpi=300)
plt.close()





