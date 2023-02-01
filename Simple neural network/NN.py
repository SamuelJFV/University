#importar numpy e mnist
from numpy import array, random, dot, exp
from mnist import MNIST as mni

# funçao sigmoide e (x)*(1-x)
def sigm(x,not_sigmoide):
    a = 1
    if not_sigmoide:
        return (x)*(1-x)
    return ((1/(1+exp(-1*a*x))))

# somas e calculo de matrizes
def f(i,a,ns=False):
    return sigm(dot(a,i),ns)
    # return array([(sigm(sum((i.transpose()*a)[x]),d)) for x in range(len(i.transpose()*a))])
    # antiga função para multiplicar matrizes

# backpropagation (error_cost)
def error(w,error_layer,i):
    return dot(w.transpose(),error_layer)*(sigm(i,True))
    
# backpropagation ( w + delta_w)
def delta(w,i,error):
    delta_w = i*error.reshape(len(error),1) #cria matriz para fazer ajustes
    w += delta_w
    return w

# defenição de variaveis iniciais
V = 2
V2 = 2*V
NW = 20 # numero dos neuronios em cada camada intermedia (existem duas)
w1 = V2 * random.rand(NW,784) - V
w2 = V2 * random.rand(NW,NW) - V
w3 = V2 * random.rand(10,NW) - V
name = array(["1","2","3","4","5","6","7","8","9","0"])
sol = array([[1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1]])


            ##########################
            ### INICIO DO PROGRAMA ###
            ##########################


while True:
    op = input("Treinar(1) Testar(2) Sair(3) -> ")
    if op == "1":
        print()
        # importar os dados
        images = mni("samples")
        (i, lb) = images.load_training()

        # programa percorre as imagens todas e faz ajustes às matrizes iniciais (matrizes w)
        for x in range(0,len(i)):
            s = sol[int(lb[x]-1)]
            inp = array(i[x])/255 # neurónios da primeira camada
            i1 = f(inp,w1) # neurónios da segunda camada
            i2 = f(i1,w2) # neurónios da terceira camada
            iout = f(i2,w3) # neurónios da ultima camada
            error_out = (s-iout)*sigm(iout,True) # erro da ultima camada
            delta(w3,i2,error_out) # ajustes feitos a w3 
            delta(w2,i1,error(w3,error_out,i2)) # ajustes feitos a w2
            delta(w1,inp,error(w2,error(w3,error_out,i2),i1)) # ajustes feitos a w1

        
        print("Treino completo!\n")
    elif op == "2":
        print()
        # importar os dados
        images = mni("samples")
        (i, lb) = images.load_testing()
        
        # seleçao da imagem
        ID = int(input("ID da imagem -> "))
        mostrar = input("Ver imagem(S/N) -> ")

        # outputs 
        print("Solução : ",lb[ID])
        if mostrar == "S" or mostrar == "s":
            print(images.display(i[ID]))
        inp = array(i[ID])
        out = f(f(f(inp,w1),w2),w3)
        [print("Resposta dada : ",name[x]) for x in range(len(out)) if max(out) == out[x]]

        print("Testado!\n")
    elif op == "3":
        # sair
        print()
        break
        print("Sair!\n")
    else:
        # opçao invalida
        print("\nOpção inválida!\n")
