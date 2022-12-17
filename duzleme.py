def duzle(eski):
    """
    Bu fonksiyonda verilen diziyi tek boyuta çevirir
    """
    yeni = []
    for i in eski:
        if type(i) is list:
            for a in i:
                if type(a) is list:
                    for x in a:
                        yeni.append(x)
                else:
                    yeni.append(a)
        else:
            yeni.append(i)
    return yeni

dizi = [1,2,3,4,["cat",315,[2,3,21],4],[7,5]]

print(duzle(dizi))

