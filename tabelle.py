import pandas as pd 
numero_colonne=eval(input('inserisci il numero di colonne che deve avere la tabella '))
lista_colonne=[]
i=1
while i<= numero_colonne :
    print('inserisci il nome della colonna numero ',i)
    nome=input('')
    lista_colonne.append(nome)
    i+=1

diz={}
for colonna in lista_colonne :
    ex=True 
    lista_dati=[]
    i=0
    while ex==True :
        print('aggiungi un valore alla colonna ', colonna, ' (se vuoi fermarti scrivi STOP oppure stop)')
        dato=input('')
        if dato=='STOP' or dato=='stop' :
            ex=False
        elif ex==True :
            if len(lista_dati)<i+1 :
                lista_dati.append('')
            lista_dati[i]=dato
            lista_lunghezze=[]
            diz[colonna]=lista_dati
            for chiave in diz :       #se il numero di righe per ogni colonna non è lo stesso pandas mi darà errore, aggiungo quindi degli spazi nelle righe mancanti
                lista_lunghezze.append(len(diz[chiave]))
            lunghezza=max(lista_lunghezze)
            differenza=lunghezza-len(lista_dati) 
            if len(lista_dati)<lunghezza :
                while differenza>0 :
                    lista_dati.append('')
                    differenza-=1
            tabella=pd.DataFrame(diz)
            print(tabella)
        i+=1

nome=str(input('inserisci il nome del file '))
nome.strip()
nome_file=nome+'.xlsx'
percorso_parziale="C:\\Users\\utente\\OneDrive\\Desktop\\"
percorso=percorso_parziale+nome_file
tabella.to_excel(percorso)






            


        
        
