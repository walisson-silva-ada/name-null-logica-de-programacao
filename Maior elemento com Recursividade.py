def maior_numero (lista):
  
  if len(lista) == 1:
    return lista[0]

  elif len(lista) == 2:
    if lista[0] > lista [1]:
      return lista[0]
    else:
      return lista[1]

  else:
    num_auxiliar = maior_numero(lista[1:])
    if lista[0] > num_auxiliar:
      return lista[0]
    else:
      return num_auxiliar