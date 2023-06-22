from ia import *
import copy

class Cobaia:
    def __init__(self, nome, entradas, estrutura: list = [3,3],chance_mutacao=0.05) -> None:
        self.nome = "Cobaia_" + nome
        self.cerebro = Cerebro("Cerebro_" + self.nome, entradas, estrutura, [self.zero, self.um], chance_mutacao)
        self.pontos = 0
        self.resultado = None
    
    def um(self):
        self.resultado = 1
    
    def zero(self):
        self.resultado = 0
    
    def pulse(self, valor: list[int]):
        self.cerebro.pulse(valor)
        return self.resultado
    
    def mutar(self):
        self.cerebro.mutar()
    
    def Add_pontos(self, pontos):
        self.pontos += pontos
    

class Tabuleiro:
    def __init__(self, limite_geracoes=100, qtd_selecao_melhores = 10) -> None:
        self.cobaias: list[Cobaia] = []
        
        self.geracao = 0
        self.limite_geracoes = limite_geracoes
        
        self.qtd_selecao_melhores = qtd_selecao_melhores
        
    
    def Init_cobaias(self,quantidade,  entradas, estrutura: list = [3,3],chance_mutacao=0.05):
        for cobaia in range(quantidade):
            nova_cobaia = Cobaia(str(cobaia-1), entradas, estrutura,chance_mutacao)
            self.cobaias.append(nova_cobaia)
    
    def Get_melhores(self) -> list[Cobaia]: 
        melhores = sorted(self.cobaias,key=lambda x: x.pontos, reverse=True)[0:self.qtd_selecao_melhores]
                
        return melhores

    def Nova_Geracao(self):
        cobaias = self.cobaias
        qtd_cobaias = len(cobaias)
        
        melhores_cobaias = self.Get_melhores()
        
        copias =  self.qtd_selecao_melhores/qtd_cobaias

        novas_cobaias: list[Cobaia] = []


        index = 0
        index_melhor = 0
        copiados = 1
        
        indexes = []
        
        for i in range(qtd_cobaias):
            indexes.append(i)

        
        
        while len(novas_cobaias) < qtd_cobaias:
            
            cont = 0
            for i in indexes:
                if type(i) == type(1):            
                    cont += 1
            
            
            if cont > 0:
                index = None
                
                while not(type(index) == type(1)):
                    index = random.sample(indexes,k=1)[0]
                    
                cobaia_pai: Cobaia =  copy.deepcopy(melhores_cobaias[index_melhor])
                cobaia_pai.mutar()
                # cobaia_pai.pontos = 0
                indexes[index] = cobaia_pai
                
                if copiados == len(melhores_cobaias):
                    copiados = 0
                    index_melhor += 1
                else:
                    copiados += 1
            
                self.cobaias = indexes
                self.geracao += 1
            else:
                break
                

    def Pulse(self, valor: list[int], esperado: list[int]):
        for cobaia in self.cobaias:
            results = []
            
            for index, val in enumerate(valor):
                # print(val)
                cobaia.pulse(val)
                if cobaia.resultado == esperado[index]:
                    results.append(True)
                else:
                    results.append(False)
            
            if False in results:
                cobaia.Add_pontos(-1)
            else:
                cobaia.Add_pontos(1)
           
                
    
    
    def TESTE_add_pontos(self):
        for cobaia in self.cobaias:
            cobaia.Add_pontos(random.randint(0,100))

tab = Tabuleiro(limite_geracoes=10000,qtd_selecao_melhores=10)
tab.Init_cobaias(100,1, estrutura=[2,1])

contagem = 0
melhor_pontuacao = 0

while tab.geracao < tab.limite_geracoes:
    contagem += 1 
    cls()
    
    for i in range(10):
        tab.Pulse([[0],[1]],[0,1])
    
    melhor_cobaia = tab.Get_melhores()[0]
    print("="*40)
    print("Geração: ", tab.geracao)
    print("Contagem: ", contagem+1)
    print("Melhor Cobaia: ", melhor_cobaia.nome)
    melhor_pontuacao = melhor_cobaia.pontos
    print("Pontos: ", melhor_pontuacao)
    
    melhores = tab.Get_melhores()
    
    print(f"{'n°':<2} |{'Cobaia':<10}|{'Pontos':>10}|{'Teste 0':>10}|{'Teste 1':>10}")
    print(f"{'1°':<2} |{melhores[0].nome:<10}|{melhores[0].pontos:>10}|{melhores[0].pulse([0]):>10}|{melhores[0].pulse([1]):>10}")
    print(f"{'2°':<2} |{melhores[1].nome:<10}|{melhores[1].pontos:>10}|{melhores[1].pulse([0]):>10}|{melhores[1].pulse([1]):>10}")
    print(f"{'3°':<2} |{melhores[2].nome:<10}|{melhores[2].pontos:>10}|{melhores[2].pulse([0]):>10}|{melhores[2].pulse([1]):>10}")
    print(f"{'4°':<2} |{melhores[3].nome:<10}|{melhores[3].pontos:>10}|{melhores[3].pulse([0]):>10}|{melhores[3].pulse([1]):>10}")
    print(f"{'5°':<2} |{melhores[4].nome:<10}|{melhores[4].pontos:>10}|{melhores[4].pulse([0]):>10}|{melhores[4].pulse([1]):>10}")
    print(f"{'6°':<2} |{melhores[5].nome:<10}|{melhores[5].pontos:>10}|{melhores[5].pulse([0]):>10}|{melhores[5].pulse([1]):>10}")
    print(f"{'7°':<2} |{melhores[6].nome:<10}|{melhores[6].pontos:>10}|{melhores[6].pulse([0]):>10}|{melhores[6].pulse([1]):>10}")
    print(f"{'8°':<2} |{melhores[7].nome:<10}|{melhores[7].pontos:>10}|{melhores[7].pulse([0]):>10}|{melhores[7].pulse([1]):>10}")
    print(f"{'9°':<2} |{melhores[8].nome:<10}|{melhores[8].pontos:>10}|{melhores[8].pulse([0]):>10}|{melhores[8].pulse([1]):>10}")
    print(f"{'10°':<2}|{melhores[9].nome:<10}|{melhores[9].pontos:>10}|{melhores[9].pulse([0]):>10}|{melhores[9].pulse([1]):>10}")
    
    
    
    if melhor_pontuacao >= 10:
        break
    else:
        tab.Nova_Geracao()
    
print("="*40)    
print("Melhor Pontuacao: ", melhor_pontuacao)
print("Geração: ", tab.geracao)

melhor_cobaia = tab.Get_melhores()[0]
print("Teste do melhor! ", melhor_cobaia.nome)
print("Pontos: ", melhor_cobaia.pontos)

melhor_cobaia.pulse([0],[0])
print("Teste 0: ", melhor_cobaia.resultado)
melhor_cobaia.pulse([0],[0])
print("Teste 0: ", melhor_cobaia.resultado)
melhor_cobaia.pulse([0],[0])
print("Teste 0: ", melhor_cobaia.resultado)
melhor_cobaia.pulse([1],[1])
print("Teste 1: ", melhor_cobaia.resultado)
melhor_cobaia.pulse([1],[1])
print("Teste 1: ", melhor_cobaia.resultado)
melhor_cobaia.pulse([1],[1])
print("Teste 1: ", melhor_cobaia.resultado)