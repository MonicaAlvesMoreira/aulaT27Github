def achar_elemento(elem ,arr):
    achou = False
    cumprimento = len(arr)

    for i in range(cumprimento):
        if (arr[ i ]== elem):
            achou = True


    if(achou == True):
        print("Achou o nome :" + elem)
    else:
        print("Não achei o nome:" + elem)

nomes = ["rafael", "Arturo", "Karen","Julia"]
achar_elemento("luiz", nomes)



                