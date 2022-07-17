def selecionar_filmes(lista):
  n = int(input('Informe quantos filmes deseja listar: '))
  for i in range(n):
    lista.append(input('informe o filme: '))
  print('\nOs filmes apresentados na pesquisa serão: ')
  for i in lista:
    print(i)


filmes = []
selecionar_filmes(filmes)


def assistiu(usuario):
  for i in filmes:
    print('Já assistiu o filme', i, '? (responda com S/N)')
    resposta = input().lower()
    if resposta == 's':
      resposta = True
    elif resposta == 'n':
      resposta = False
    else:
      print('Resposta inválida, por favor responda com "s" para sim, e "n" para não')
      return assistiu(usuario)
    usuario.append(resposta)


print('\nUsuario 1 ======================================================\n')
usuario1 = []
assistiu(usuario1)
print('\nUsuário 2 ======================================================\n')
usuario2 = []
assistiu(usuario2)


def recomendar(usuarioA, usuarioB):
  recomendadosA = []
  recomendadosB = []
  for i in range(len(usuarioA)):
    if usuarioA[i] == True and usuarioB[i] == False:
      recomendadosB.append(filmes[i])
    elif usuarioA[i] == False and usuarioB[i] == True:
      recomendadosA.append(filmes[i])
  print('\nPara o primeiro usuário, recomendamos o(s) seguinte(s) filmes: ')
  for i in recomendadosA:
    print(i)
  print('\nPara o segundo usuário, recomendamos o(s) seguinte(s) filmes: ')
  for i in recomendadosB:
    print(i)


recomendar(usuario1, usuario2)
