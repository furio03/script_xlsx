import pandas as pd 
print('ogni quanti pezzi viene applicato lo sconto?')
periodo=int(input(''))
numero_colonne=6
lista_colonne=[]
lista_colonne.append('prezzo')
i=1
nome_col=periodo
print('inserisci il tasso di sconto da applicare ogni',periodo,' pezzi acquistati (inserisci lo sconto come intero)')
inp=float(input(''))
sconto=inp/100
while i<= numero_colonne :
    lista_colonne.append('pezzi: '+str((nome_col)))
    nome_col+=periodo
    i+=1
diz={}
for elemento in lista_colonne :
    diz[elemento]=[]
stp=True
while stp==True :
    print('inserisci il prezzo di un prodotto, per fermarti scrivi stop')
    prezzo=input('')
    if prezzo =='STOP' or prezzo =='stop' :
        break
    elif prezzo !='STOP' or prezzo != 'stop' :
        diz['prezzo'].append(float(prezzo))
lista_colonne.pop(0)
lunghezza_col=len(diz['prezzo'])
k=1
for unità in lista_colonne :
    i=1
    while i<= len(diz['prezzo']):
        aggiunta=diz['prezzo'][i-1]-(diz['prezzo'][i-1]*(sconto*k))
        diz[unità].append(round(aggiunta,2))
        i+=1
    k+=1
tabella=pd.DataFrame(diz)
nome=str(input('inserisci il nome del file '))
nome.strip()
nome_file=nome+'.xlsx'
percorso_parziale="C:\\Users\\utente\\OneDrive\\Desktop\\"
percorso=percorso_parziale+nome_file
tabella.to_excel(percorso)






            


        
        
