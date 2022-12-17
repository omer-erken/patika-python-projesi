eski = [[1, 2], [3, 4], [5, 6, 7]]
yeni = []
def cevirme(eski):
    for i in eski[::-1]:
        yeni.append(i[::-1])
    return yeni
print(cevirme(eski))