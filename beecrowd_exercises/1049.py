'''
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.
'''
p1 = input("")

if p1 == "vertebrado":
  vertebrado = input("")

  if vertebrado == "ave":
    ave = input("")

    if ave == "carnivoro":
      print("aguia")
    else:
      print("pomba")

  elif vertebrado == "mamifero":
    mamifero = input("")
    if mamifero == "onivoro":
      print("homem")
    else:
      print("vaca")

if p1 == "invertebrado":
  invertebrado = input("")

  if invertebrado == "inseto":
    inseto = input("")

    if inseto == "hematofago":
      print("pulga")
    else:
      print("lagarta")
  
  elif invertebrado == "anelideo":
    anelideo = input("")
    if anelideo == "hematofago":
      print("sanguessuga")
    else:
      print("minhoca")

