#importando as bilbiotecas 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import time
plt.rcParams['figure.figsize'] = (13, 7) #deixando os gráficos mais compridos

print('Programa para fazer gráfico dos casos de covid no estado do Rio de Janeiro')

#interagindo com o usuário
while True:
	salvar=input('\nDeseja salvar os gráficos? [S/N] ')
	if salvar!= 'S' and salvar!='N' and salvar!='s' and salvar!='n':
		print('Digite S ou N.')
	else:
		if salvar=='S' or salvar=='s':
			salvar=True
		else:
			salvar=False
		break

#baixando os dados
print('Baixando os dados de http://painel.saude.rj.gov.br...')
t0=time.time()
df=pd.read_csv("http://painel.saude.rj.gov.br/arquivos/COVID.CSV",sep=';',\
               encoding='latin1', parse_dates=['dt_sintoma'], dayfirst=True, index_col='dt_sintoma',low_memory=False)
t1=time.time()
tempo=round(t1-t0,1)
print('\nDados baixados!')
print('Tempo: '+str(tempo)+'s')

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
if salvar:
	plt.savefig('Casos Acumulados Rio de Janeiro '+ str(hoje),dpi=300)
	plt.close()
else:
	plt.show()

#plotando os casos diários
df2=df.groupby(['dt_sintoma']).sum()
df2['casos'].plot(color='black')
plt.title('Casos Diários - RJ '+ str(datetime.today().strftime('%d-%m-%Y')))
plt.xlabel('Data')
plt.ylabel('Casos Diários')
if salvar:
	plt.savefig('Casos Diários Rio de Janeiro '+ str(hoje),dpi=300)
	plt.close()
	print('\nGráficos salvos na pasta atual.')
else:
	plt.show()

print('\nFeito por: Gustavo M. Marzullo de Britto')

a=input('Aperte ENTER para sair.')
