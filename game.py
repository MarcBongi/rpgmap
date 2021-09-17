class cycle:
    def __init__(self, c):
        self._c = c
        self._index = -1

    def __next__(self):
        self._index += 1
        if self._index>=len(self._c):
            self._index = 0
        return self._c[self._index]

    def previous(self):
        self._index -= 1
        if self._index < 0:
            self._index = len(self._c)-1
        return self._c[self._index]

caminho = []
vermelho=[2, 3, 4, 5, 6]
preto=[3, 5, 7, 9]
passos = int(0)
sala_atual = int(1)
proxima_atual = int(0)

def func_caminho():
    value = int(input("Você esta na sala 1:\n Escolha o seu caminho:\n [1] - Vermelho \n [2] - Preto \n"))
    if(value != 1 and value !=2):
        return func_caminho()
    return value

if (func_caminho() == 1):
    caminho = cycle(vermelho)
else:
    caminho = cycle(preto)

def func_proxima_sala(sala_atual, passos):
    passos = passos + 1
    func_valida_passos(passos)
    print("Sala Atual: %d" % (sala_atual))
    proxima_sala = int(input("Escolha o proximo passo: \n"))

    proxima_atual = next(caminho)

    if(proxima_sala == 9 and proxima_atual == 9):
        print("você ganhou!")
        exit()
    if(proxima_sala == proxima_atual):
        return proxima_sala
    else:
        caminho.previous()
        print("Sala errada!")
        
        return func_proxima_sala(sala_atual, passos)

def func_valida_passos(passos):
    if(passos >7):
        print("Você deu mais de 7 passos e perdeu tente novamente!")
        exit()
    else:
        return


while (1) :
    sala_atual = int(func_proxima_sala(sala_atual, passos))