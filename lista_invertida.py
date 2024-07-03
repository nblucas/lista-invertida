from personagem import Personagem
from interface import Interface

class ListaInvertida:

    def __init__(self):
        self.__personagens = list()
        self.__indices_racas = dict()
        self.__indices_classes = dict()
        self.__indices_niveis = dict()

        self.__indices_gerador = 0
        self.__carregou_dados = False

        self.__interface = Interface()

    def _gera_indice(self):
        self.__indices_gerador += 1
        return self.__indices_gerador

    def _adiciona_indices(self, indices, chave, valor):
        if chave not in indices:
            indices[chave] = []
        indices[chave].append(valor)

    def _carrega_dados(self):
        with open('dados_carga.txt', 'r') as arquivo:
            lendo_arquivo = True
            while lendo_arquivo:
                linha = arquivo.readline()

                if not linha:
                    lendo_arquivo = False
                else:
                    dados = linha.strip().split(',')

                    nome = dados[0]
                    id_raca = int(dados[1])
                    id_classe = int(dados[2])
                    nivel = int(dados[3])

                    self._adiciona_personagem(nome, id_raca, id_classe, nivel)

    def _formata_niveis(self, nivel):
        if nivel <= 15:
            return 1  # novato
        if nivel <= 30:
            return 2  # adepto
        if nivel <= 45:
            return 3  # mestre
        return 4  # lendario

    def _adiciona_personagem(self, nome, id_raca, id_classe, nivel):
        id_personagem = self._gera_indice()

        nivel = self._formata_niveis(nivel)  # ajustando o nível numérico para um grupo

        novo_personagem = Personagem(id_personagem, nome, id_raca, id_classe, nivel)
        self.__personagens.append(novo_personagem)

        self._adiciona_indices(self.__indices_racas, id_raca, id_personagem)
        self._adiciona_indices(self.__indices_classes, id_classe, id_personagem)
        self._adiciona_indices(self.__indices_niveis, nivel, id_personagem)
    
    def _remove_indices(self, categoria, lista_indices, id):
        lista_indices.get(categoria).remove(id)

    def _remove_personagem(self, id):

        personagem_para_remocao = None

        for personagem in self.__personagens:
            if personagem.id == id:
                personagem_para_remocao = personagem
        
        if personagem_para_remocao is None:
            return None

        self.__personagens.remove(personagem_para_remocao)

        self._remove_indices(personagem_para_remocao.raca, self.__indices_racas, id)
        self._remove_indices(personagem_para_remocao.classe, self.__indices_classes, id)
        self._remove_indices(personagem_para_remocao.nivel, self.__indices_niveis, id)

    def _personagem_para_dict(self, personagem):
        return {
            'id': personagem.id,
            'nome': personagem.nome,
            'raca': personagem.raca,
            'classe': personagem.classe,
            'nivel': personagem.nivel
        }

    def _retorna_todos_personagens(self):
        return [self._personagem_para_dict(personagem) for personagem in self.__personagens]
    
    def _retorna_todos_indices(self):
        return [personagem.id for personagem in self.__personagens]

    def _retorna_conjuntos(self, item_pedido, indices):     
        for chave, valor in indices.items():
            if chave == item_pedido:
                return set(valor)
        return set()

    def _busca_personagem(self, pedido):
        indices = []

        id_raca_pedida = pedido['raca_id']
        id_classe_pedida = pedido['classe_id']
        id_nivel_pedido = pedido['nivel_grupo_id']

        if id_raca_pedida != 0:        
            indices.append(self._retorna_conjuntos(id_raca_pedida, self.__indices_racas))

        if id_classe_pedida != 0:
            indices.append(self._retorna_conjuntos(id_classe_pedida, self.__indices_classes))

        if id_nivel_pedido != 0:
            indices.append(self._retorna_conjuntos(id_nivel_pedido, self.__indices_niveis))

        for i in range(len(indices)):
            if i == 0:
                interseccao = indices[i]
            else:
                interseccao = interseccao.intersection(indices[i])

        if len(interseccao) == 0:
            return None

        personagens_procurados = []

        for indice_interseccao in interseccao:
            for personagem in self.__personagens:
                if personagem.id == indice_interseccao:
                    personagens_procurados.append(self._personagem_para_dict(personagem))

        return personagens_procurados

    def executa_sistema(self):
        self.__interface.bemvindo()
        
        executando = True
        while executando:
            operacao = self.__interface.operacoes_menu_principal()

            if operacao == 1:
                busca_dados = self.__interface.busca_formulario()

                if busca_dados == (0, 0, 0):
                    self.__interface.imprime_falta_filtros()
                else:
                    pedido = {
                        'raca_id': busca_dados[0],
                        'classe_id': busca_dados[1],
                        'nivel_grupo_id': busca_dados[2]
                    }

                    personagens = self._busca_personagem(pedido)

                    self.__interface.imprime_personagens(personagens)

            elif operacao == 2:
                nome, raca, classe, nivel = self.__interface.incluir_personagem()

                self._adiciona_personagem(nome, raca, classe, nivel)

            elif operacao == 3:
                indices = self._retorna_todos_indices()

                indice_personagem = self.__interface.remove_personagem(indices)

                self._remove_personagem(indice_personagem)

            elif operacao == 4:
                personagens = self._retorna_todos_personagens()

                self.__interface.imprime_todos_personagens(personagens)

            elif operacao == 5:
                if(self.__carregou_dados):
                    self.__interface.dados_carregados()
                else:
                    self._carrega_dados()
                    self.__carregou_dados = True    
                
                    self.__interface.carrega_dados()
                        

            elif operacao == 0:
                executando = False
