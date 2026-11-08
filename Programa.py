class Pilha:
    def __init__(self):
        self.topo = -1
        self.capacidade = 5
        self.pilha = [None] * self.capacidade

    def inserir_documento(self, elemento):
        if self.topo + 1 >= self.capacidade:
            print("ERRO: pilha cheia. Não é possível inserir outro documento.")
            return
        if self.topo == -1:
            self.topo += 1
            self.pilha[self.topo] = elemento
        else:
            for i in range(self.topo, -1, -1):
                if self.pilha[i].get("codigo") == elemento.get("codigo"):
                    print("ERRO: já existe esse código na pilha.")
                    return
            self.topo += 1
            self.pilha[self.topo] = elemento

    def retirar_documento(self):
        if self.topo < 0:
            print("ERRO: pilha vazia. Não há documento para retirar.")
            return

        self.pilha[self.topo] = None
        self.topo -= 1

    def consultar_topo(self):
        if self.topo < 0:
            print("ERRO: pilha vazia. Não há documentos armazenados.")
            return

        print(f"[{self.pilha[self.topo].get('codigo')}] {self.pilha[self.topo].get('descricao')}")

    def exibir_pilha(self):
        if self.topo < 0:
            print("ERRO: pilha vazia. Não há documentos armazenados.")
            return

        for i in range(self.topo, -1, -1):
            print(f"[{self.pilha[i].get('codigo')}] {self.pilha[i].get('descricao')}")

    def pesquisar_documento(self, codigo):
        if self.topo < 0:
            print("ERRO: pilha vazia. Não há documentos armazenados.")
            return

        quant_documento = 0
        for i in range(self.topo, -1, -1):
            if codigo == int(self.pilha[i].get('codigo')):
                quant_documento += 1
                print(f"[{self.pilha[i].get('codigo')}] {self.pilha[i].get('descricao')}")

        if quant_documento == 0:
            print("ERRO: documento não encontrado. Este índice não existe na parte ocupada da pilha.")

    def exibir_estatisticas(self):
        documentos_armazenados = self.topo + 1
        print(f"Capacidade máxima: {self.capacidade}\nDocumentos armazenados: {documentos_armazenados}\nPosições livres: {(self.capacidade - documentos_armazenados)}\nOcupação: {(documentos_armazenados / self.capacidade * 100):.2f}%\n",)

def exibir_menu():

    pilha = Pilha()

    while True:
        print("=== ESTRUTURA DE PILHA ===")
        print("0. Encerrar o programa\n1. Inserir documento\n2. Retirar documento\n3. Consultar documento do topo\n4. Exibir todos os documentos\n5. Pesquisar documento por código\n6. Exibir estatísticas")
        while True:
            try:
                opcao = int(input("Insira uma opção: "))
                break
            except ValueError:
                print("Valor inválido. Tente novamente.")
        match opcao:
            case 0:
                break
            case 1:
                entrada_documento = input("Insira o código do documento e sua descrição: ").split(" ")
                codigo_documento = entrada_documento[0]
                descricao_documento = entrada_documento[1]
                documento = dict(codigo = codigo_documento, descricao = descricao_documento)
                pilha.inserir_documento(documento)
            case 2:
                pilha.retirar_documento()
            case 3:
                pilha.consultar_topo()
            case 4:
                pilha.exibir_pilha()
            case 5:
                while True:
                    try:
                        codigo = int(input("Insira o código do item na pilha: "))

                        break
                    except:
                        print("Valor de código inválido. Tente novamente.")
                pilha.pesquisar_documento(codigo)
            case 6:
                pilha.exibir_estatisticas()
            case _:
                print("Opção invalida. Tente novamente.")

exibir_menu()