v1 = (2,3)
v2 = (4,6)

#1 Проверяем коллинеарность через константу if x1/x2 == y1/y2
if v1[0] / v2[0] == v1[1] / v2[1]:
    print("Vecrors are collinear")
    #2 Проверяем направление if k > 0 or k < 0
    if v1[0] / v2[0] > 0:
        print("Vectors have the same direction")
    else:
        print("Vectors have the opposite direction ")
else:
    print("Vectors aren't collinear")


