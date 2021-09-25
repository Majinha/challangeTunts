# library pandas
import pandas as pd
# headline
tabela = pd.read_csv("tabela.csv")
dados = len(tabela)
average = 0
naf = 0
max = 60 # that's the maximum of classes they had

for i in range(dados): # loop to read all names
    # searching on the csv file
    linha = tabela.iloc[i]
    p1 = linha["P1"]
    p2 = linha["P2"]
    p3 = linha["P3"]
    faltas = linha["Faltas"]
    name = linha["Aluno"]
    average = round((p1+p2+p3)/3) # calculating average
    print(name)
    if faltas >= (25/100)*max:
        print('REPROVADO POR FALTAS\n---------------')
        
    elif faltas <= (25/100)*max:
        if average < 50:
            print('FAILED BY GRADE')
            print('naf: 0')
            
        elif 50 <= average < 70:
            print('FINAL EXAM')
            naf = 140 - average 
            print('naf: ',naf)
            
        else:
            print('APPROVED')
            print('naf: 0')
        print('Average = ', average, '\n---------------')