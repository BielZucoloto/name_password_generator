import random

#abro meu arquivo txt e leio todas as senhas, linha por linha. Depois adiciono todas as senhas na variável senhas
arquivo = open('C:/Users/usuario/Documents/codigo//texto.txt')
senhas=arquivo.readlines()

#crio uma lista vazia e adiciono todas as senhas da variável senhas na minha lista historico
historico = []
[historico.append(line.rstrip("\n"))for line in senhas]

resp = ''

while resp != 'N':
    
    usuario = input('Nome do cliente: ')

    prime_letra = usuario[0].upper()
    ultim_letra = usuario[-1]

    #aqui é possível decidir o intervalo para gerar o numero aleatorio, eu escolhi de 1000 até 9999
    numero_aleatorio = random.sample(range(1000,10000),1)

    #aqui é onde eu monto a senha, baseado na primiera letra do nome + o numero aleatorio gerado + a ultima letra do nome
    senha = (str(prime_letra + str(numero_aleatorio[0]) + ultim_letra))

    """
    aqui eu vejo se a senha gerada não está na minha lista de senhas, se isso for verdade eu adiciono a senha 
    na lista e depois eu pego as novas senhas geradas dentro da lista e adiciono em um arquivo txt
    """
    if senha not in historico:
        historico.append(senha)
        with open('C:/Users/usuario/Documents/codigo//texto.txt', 'w') as f:
            for item in historico:
                f.write("%s\n" % item)
        print('Senha gerada com sucesso!')
        print('A senha gerada foi: ',senha)
        
    else:
        print('senha já cadastrada!')

    resp = input('''
    Executar novamente? 
    S-(SIM) / N-(Não): ''').upper()
    
