# SON 14 PERO USAMOS 5
e = 3
hAM = [""] * (e)
hAM2 = [""] * (e)
pRECIO = [0] * (e)
sHAM = [0] * (e)
t = [0] * (e)
sHAM2 = [0] * (e)
sLOCAL = [0] * (3)
cONTLOCAL = [0] * (3)
pROMEDIO = [0] * (3)
lOCAL = [""] * (12)

tOT = -1
for h in range(0, e - 1 + 1, 1):
    print("Ingrese nombre de la hamburguesa y el precio")
    hAM[h] = input()
    pRECIO[h] = int(input())
for h in range(0, e - 1 + 1, 1):
    sHAM[h] = 0
    t[h] = 0
    sHAM2[h] = 0
for h in range(0, 3 - 1 + 1, 1):
    pROMEDIO[h] = 0
print("Ingrese Local - Nombre - Puntos - Dia ")
l = input()
n = input()
p = int(input())
d = int(input())
while l != "FIN":
    for h in range(0, 2 + 1, 1):
        if n == hAM[h]:
            sHAM2[h] = sHAM2[h] + 1
    sENIAL = 0
    for h in range(0, tOT + 1, 1):
        if l == lOCAL[h]:
            sLOCAL[h] = sLOCAL[h] + p
            cONTLOCAL[h] = cONTLOCAL[h] + 1
            sENIAL = 1
    if sENIAL == 0:
        lOCAL[h] = l
        sLOCAL[h] = p
        cONTLOCAL[h] = 1
        tOT = tOT + 1
    if d >= 10 and d <= 30:
        for h in range(0, 2 + 1, 1):
            if n == hAM[h]:
                sHAM[h] = sHAM[h] + 1
    print("Ingrese Local - Nombre - Puntos - Dia ")
    l = input()
    n = input()
    p = int(input())
    d = int(input())

# PUNTO A
for h in range(0, 3 - 1 + 1, 1):
    pROMEDIO[h] = pROMEDIO[h] + float(sLOCAL[h]) / cONTLOCAL[h]
print("LOCAL        PROMEDIO")
for h in range(0, 3 - 1 + 1, 1):
    print(lOCAL[h] + "        " + str(pROMEDIO[h]))

# PUNTO B
pASO = 0
while True:    #This simulates a Do Loop
    s = 0
    for h in range(0, 1 - pASO + 1, 1):
        if sHAM2[h] < sHAM2[h + 1]:
            aUX = sHAM2[h]
            sHAM2[h] = sHAM2[h + 1]
            sHAM2[h] = aUX
            s = 1
    pASO = pASO + 1
    if not(s == 1): break   #Exit loop
print("HAMBURGUESA        CANTIDAD X MES")
for h in range(0, e - 1 + 1, 1):
    print(hAM[h] + "        " + str(sHAM2[h]))

# PUNTO C
for h in range(0, e - 1 + 1, 1):
    t[h] = t[h] + pRECIO[h] * sHAM[h]
for h in range(0, e - 1 + 1, 1):
    if h == 0:
        mAX = t[h]
    else:
        if t[h] > mAX:
            mAX = t[h]

# 
print("Las Hamburguesas con mayor importe vendido son : ")
for h in range(0, e - 1 + 1, 1):
    if mAX == t[h]:
        print(hAM[h])
