#Calcula o volume de uma fossa sépica para estabelecimentos residenciais em conformidade com a NBR 7229/1993
'''
    Entre com os dados da Fossa Séptica
'''
print('\nVerifique as opões abaixo:\n') # Exibe uma mensagem na tela com o menu de empreendimentos!
empreendimentos = {1: 'Residencia', 2: 'Hotel', 3: 'Alojamento', 4: 'Escritório', 5: 'Restaurantes e Similares',
          6: 'Fábrica e Geral', 7: 'Edifícios Públicos ou Comerciais', 8: 'Escolas(Externatos) e Locais de Longa Permanência',
          9: 'Bares'}
    
    #    Apresenta um menu com os tipos de empreendimentos!

tipo = 1
while tipo >= 1 or tipo <= 9:
    for key, value in empreendimentos.items():
        print(f'\t{key}: {value}')
    tipo = int(input('\nEscolha o tipo de empreendimento para o qual deseja dimensionar a fossa séptica: \n'))
    if tipo == 1:
        print('\nVocê selecionou Dimensionamento de uma Fossa Séptica para estabelecimentos do tipo Residencial em conformidade com a NBR 7229/1993:')
        break
    elif tipo == 2:
        print('\nVocê selecionou Dimensionamento de uma Fossa Séptica para estabelecimentos do tipo Hotel em conformidade com a NBR 7229/1993:')
        break
    elif tipo == 3:
        print('\nVocê selecionou Dimensionamento de uma Fossa Séptica para estabelecimentos do tipo Alojamento em conformidade com a NBR 7229/1993:')
        break
    elif tipo == 4:
        print('\nVocê selecionou Dimensionamento de uma Fossa Séptica para estabelecimentos do tipo Escritório em conformidade com a NBR 7229/1993:')
        break
    elif tipo == 5:
        print('\nVocê selecionou Dimensionamento de uma Fossa Séptica para estabelecimentos do tipo Restaurantes e Similares em conformidade com a NBR 7229/1993:')
        break
    elif tipo == 6:
        print('\nVocê selecionou Dimensionamento de uma Fossa Séptica para estabelecimentos do tipo Fábrica em Geral em conformidade com a NBR 7229/1993:')
        break
    elif tipo == 7:
        print('\nVocê selecionou Dimensionamento de uma Fossa Séptica para estabelecimentos do tipo Edifícios Públicos ou Comerciais em conformidade com a NBR 7229/1993:')
        break
    elif tipo == 8:
        print('\nVocê selecionou Dimensionamento de uma Fossa Séptica para estabelecimentos do tipo Escolas(Externatos) e Locais de Longa Permanência em conformidade com a NBR 7229/1993:')
        break
    elif tipo == 9:
        print('\nVocê selecionou Dimensionamento de uma Fossa Séptica para estabelecimentos do tipo Bares em conformidade com a NBR 7229/1993:')
        break
    else:
        print('ERROR! Verifique a opção desejada!')
        tipo = 1
        continue
N = 1
while N != 0:
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
        if limpeza < 0 or limpeza > 5:
            print('ERROR!O intervalo de limpeza deve está entre 1 ano e 5 anos!\n')
            continue
        else:
            padrao = input('Digite o padrão resiencial (a para alto, m para médio ou b para baixo):\n ')
            if padrao == 'a' or padrao == 'A':
                C = 160
                padrao = 'alto'
            elif padrao == 'm' or padrao == 'M':
                C = 130
                padrao = 'médio'
            elif padrao == 'b' or padrao == 'B':
                C = 100
                padrao = 'baixo'
            else:
                print('ERROR!Verifique a opção desejada digite apenas a, b ou m!\n')
                continue
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
        print('\nMEMÓRIA DE CÁLCULO\n')
        print(f'Polulação: {N} contribuintes;\nPadrão Residencial: {padrao};\nTemperatura Média: {temperatura}C;\nContribuição Diária (C): {C} Litros;\nTemmpo de Detenção (Td): {T};')
        print(f'Contribuição de Lodo Fresco (Lf): {Lf};\nIntervalo de Limmpeza {limpeza} anos;\nVolume Útil: {V} Litros\n')