'''
    Dimensionamento de uma Fossa Séptica em conformidade com a NBR 7229/1993:
'''
'''
    Entre com os dados da Fossa Séptica
'''
N = 1
while N > 0:
    N = int(input('Digite o número de contribuintes ou 0 (zero) para encerrar:\n '))
    if N == 0:
        print('Você finalizou o programa!')
        break
    elif N < 0:
        print('ERROR! Você digitou um valor inválido!\n Digite um valor maior que zero ou 0 para encerrar')
        continue
    else:
        temperatura = float(input('Digite a temperatura média do local em Graus Celsius:\n '))
        limpeza = float(input('Digite o intervalo de limpeza em anos:\n '))
        padrao = input('Digite o padrão resiencial (a para alto, m para médio ou b para baixo):\n ')
        if padrao == 'a':
            C = 160
        elif padrao == 'm':
            C = 130
        elif padrao == 'b':
            C = 100
        else:
            print('ERROR!Verifique a opção desejada!')
        if limpeza == 1:
            if temperatura <= 10:
                k = 94
            elif temperatura > 10 and temperatura <= 20:
                k = 65
            else:
                k = 57
        elif limpeza == 2:
            if temperatura <= 10:
                k = 134
            elif temperatura > 10 and temperatura <= 20:
                k = 105
            else:
                k = 97
        elif limpeza == 3:
            if temperatura <= 10:
                k = 174
            elif temperatura > 10 and temperatura <= 20:
                k = 145
            else:
                k = 137
        elif limpeza == 4:
            if temperatura <= 10:
                k = 214
            elif temperatura > 10 and temperatura <= 20:
                k = 185
            else:
                k = 177
        elif limpeza == 5:
            if temperatura <= 10:
                k = 254
            elif temperatura > 10 and temperatura <= 20:
                k = 225
            else:
                k = 217
        else:
            print('ERROR! O tempo de detenção não pode ser superior a 5 anos!')

        contribuicao_diaria = N * C
        if contribuicao_diaria <= 0:
            print('ERRROR! Não é possível dimensionar o volume da fossa - N e C devem se maior que zero!')
        elif contribuicao_diaria > 0 and contribuicao_diaria<= 1500:
            T = T
        elif contribuicao_diaria > 1500 and contribuicao_diaria <= 3000:
            T = 0.92
        elif contribuicao_diaria > 3000 and contribuicao_diaria <= 4500:
            T = 0.83
        elif contribuicao_diaria > 4500 and contribuicao_diaria <= 6000:
            T = 0.75
        elif contribuicao_diaria >= 6000 and contribuicao_diaria <= 7500:
            T = 0.67
        elif contribuicao_diaria > 7500 and contribuicao_diaria <= 9000:
            T = 0.58
        else:
            T = 0.50
        Lf = 1
        print('Tratando apenas de empreendimentos residenciais, conforme NBR 7229/1993 Lf = 1!')

        V = 1000 + N*(C*T + k*Lf)
        print('O Volume Útil da Fossa Septica calculado é de : %5.2f Litros' % V)