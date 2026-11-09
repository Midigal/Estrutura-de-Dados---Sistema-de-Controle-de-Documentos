import time #Para dar para ver a resposta do menu antes de já voltar a aparecer

class Pilha:
    def __init__(self):
        self.topo = -1
        self.capacidade = 5
        self.pilha = [None] * self.capacidade

    def inserir_documento(self, elemento):
        if self.topo + 1 >= self.capacidade:
            print("\nERRO: pilha cheia. Não é possível inserir outro documento.")
            time.sleep(1)
            return
        if self.topo == -1:
            self.topo += 1
            self.pilha[self.topo] = elemento
            print(f"\nDocumento código[{elemento['codigo']}] adicionado ao topo.")
            time.sleep(1)
        else:
            for i in range(self.topo, -1, -1):
                if self.pilha[i].get("codigo") == elemento.get("codigo"):
                    print("\nERRO: já existe esse código na pilha.")
                    time.sleep(1)
                    return
            self.topo += 1
            self.pilha[self.topo] = elemento
            print(f"\nDocumento código[{elemento['codigo']}] adicionado ao topo.")
            time.sleep(1)
            if self.topo == 3:
                print("\nPilha quase cheia, resta 1 espaço vazio.")
                time.sleep(1)
            elif self.topo == 4:
                print("\nPilha completa, remova documentos para poder inserir novos.")
                time.sleep(1)


    def retirar_documento(self):
        if self.topo < 0:
            print("\nERRO: pilha vazia. Não há documento para retirar.")
            time.sleep(1)
            return
        else:
            print("\nDocumento removido do topo.")
            time.sleep(1)
        self.pilha[self.topo] = None
        self.topo -= 1

    def consultar_topo(self):
        if self.topo < 0:
            print("\nERRO: pilha vazia. Não há documentos armazenados.")
            time.sleep(1)
            return

        print(f"\n[{self.pilha[self.topo].get('codigo')}] {self.pilha[self.topo].get('descricao')}")
        time.sleep(1)

    def exibir_pilha(self):
        if self.topo < 0:
            print("\nERRO: pilha vazia. Não há documentos armazenados.")
            time.sleep(1)
            return

        for i in range(self.topo, -1, -1):
            print(f"[{self.pilha[i].get('codigo')}] {self.pilha[i].get('descricao')}")
        time.sleep(1)

    def pesquisar_documento(self, codigo):
        if self.topo < 0:
            print("\nERRO: pilha vazia. Não há documentos armazenados.")
            time.sleep(1)
            return

        quant_documento = 0
        for i in range(self.topo, -1, -1):
            if codigo == int(self.pilha[i].get('codigo')):
                quant_documento += 1
                print(f"\n[{self.pilha[i].get('codigo')}] {self.pilha[i].get('descricao')}")
                time.sleep(1)

        if quant_documento == 0:
            print("\nERRO: documento não encontrado. Este índice não existe na parte ocupada da pilha.")
            time.sleep(1)

    def exibir_estatisticas(self):
        documentos_armazenados = self.topo + 1
        print(f"\nCapacidade máxima: {self.capacidade}\nDocumentos armazenados: {documentos_armazenados}\nPosições livres: {(self.capacidade - documentos_armazenados)}\nOcupação: {(documentos_armazenados / self.capacidade * 100):.0f}%\n",)
        time.sleep(1)
    def limpar_pilha(self):
        if self.topo < 0:
            print("\nERRO: Pilha já vazia.")
            time.sleep(1)
        else:
            verifica = input("Deseja mesmo apagar todos os documentos da lista? (s/n): ")
            if verifica == 's':
                self.pilha.clear()
                self.topo = -1
                print('\nPilha esvaziada.')
            elif verifica == 'n':
                return
            else:
                print("\nERRO: Opção inválida.")
                return
            time.sleep(1)


def exibir_menu():

    pilha = Pilha()

    while True:
        print("\n=== ESTRUTURA DE PILHA ===")
        print("0. Encerrar o programa\n1. Inserir documento\n2. Retirar documento\n3. Consultar documento do topo\n4. Exibir todos os documentos\n5. Pesquisar documento por código\n6. Exibir estatísticas\n7. Limpar pilha")
        while True:
            try:
                opcao = int(input("Insira uma opção: "))
                break
            except ValueError:
                print("\nValor inválido. Tente novamente.")
                time.sleep(1)
        match opcao:
            case 0:
                break
            case 1:
                cod = input("Insira o código do documento: ")
                descr = input("Insira a descrição do documento: ")
                documento = {"codigo": cod, "descricao": descr}
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
                        print("\nValor de código inválido. Tente novamente.")
                        time.sleep(1)
                pilha.pesquisar_documento(codigo)
            case 6:
                pilha.exibir_estatisticas()
            case 7:
                pilha.limpar_pilha()
            case _:
                print("\nOpção invalida. Tente novamente.")
                time.sleep(1)

exibir_menu()