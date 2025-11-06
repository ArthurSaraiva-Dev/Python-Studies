class Televisao:
    def __init__(self, pcanal, cmin, cmax):
        self.canal = pcanal
        self.cmin = cmin
        self.cmax = cmax

    def mudar_canal_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax

    def mudar_canal_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin
        
def main():
    tv1 = Televisao(5, 2, 10)
    print(tv1.canal)
    for y in range(15):
        tv1.mudar_canal_cima()
        print(tv1.canal)

    tv2 = Televisao(10, 2, 10)
    print(tv2.canal)
    for x in range(12):
        tv2.mudar_canal_baixo()
        print(tv2.canal)
        

if __name__ == '__main__':
    main()

