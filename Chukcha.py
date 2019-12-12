from graph import *
import math

windowSize(1900,1000)
canvasSize(1700, 800)
def ellips(a, b, XC, YC, color, nak=0):
    alfa = 0
    A = []
    nak = nak * 0.0175
    for i in range(25):
        x = a * math.cos(alfa)
        y = b * math.sin(alfa)
        X = x * math.cos(nak) + y * math.sin(nak)
        Y = -x * math.sin(nak) + y * math.cos(nak)
        A.append((X + XC, Y + YC))
        alfa += math.pi / 12
    brushColor(color)
    penColor(color)
    elip = polygon(A)
    return elip


def polu_ellips(a, b, XC, YC, color, nak=0):
    alfa = 0
    A = []
    for i in range(13):
        x = a * math.cos(alfa)
        y = b * math.sin(alfa)
        X = x * math.cos(nak) + y * math.sin(nak)
        Y = -x * math.sin(nak) + y * math.cos(nak)
        A.append((X + XC, Y + YC))
        alfa += math.pi / 12
    brushColor(color)
    penColor(color)
    poluelip = polygon(A)
    return poluelip


def chukcha(Xc, Yc, raz=1):
    A=[]
    ar = 50 * raz
    br = 20 * raz
    at = 90 * raz
    bt = -200 * raz
    ak = 70 * raz
    bk = 50 * raz
    asapk = 50 * raz
    bsapk = 30 * raz
    al = 40 * raz
    bl = 20 * raz
    Xt = Xk = Xs = Xl = Xc
    Yk = Ys = Yl = Yc
    Yt = Yc + 200 * raz
    Yrp = Yc + 100 * raz
    Yrbp = Yc + 115 * raz
    Xrp = Xc - 2 * ar
    Xrbp = Xc + 2 * ar - 10 * raz
    kopushon = ellips(ak, bk, Xk, Yk, 'red')

    shapka = ellips(asapk, bsapk, Xs, Ys, 'green')
    lico = ellips(al, bl, Xl, Yl, 'red')
    telo = polu_ellips(at, bt, Xt, Yt, 'blue')
    ruka_s_palkoi = ellips(ar, br, Xrp, Yrp, 'red')
    ruka_bez_palki = ellips(ar, br, Xrbp, Yrbp, 'red', -35)

    A.append(kopushon)
    A.append(lico)
    A.append(telo)
    A.append(ruka_bez_palki)
    A.append(ruka_s_palkoi)
    A.append(shapka)
    return A

chuk1 = chukcha(220, 200, 0.7)
def perem():

    for k in range(len(chuk1)):
        if chuk1[k]==1:
            moveObjectBy(chuk1[k], 10, 10)
        moveObjectBy(chuk1[k], 30,30)
        print(yCoord(chuk1[k]))

    print('end')

onTimer(perem, 300)
run()
