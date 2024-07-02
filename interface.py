import os


class Interface:
    def __init__(self):

        self.__numero_para_raca = {
            1: 'humano',
            2: 'anão',
            3: 'elfo',
            4: 'gnomo',
            5: 'orc',
            6: 'troll',
            7: 'tauren',
            8: 'morto-vivo',
            0: 'não filtrar por raça'
        }

        self.__numero_para_classe = {
            1: 'guerreiro',
            2: 'mago',
            3: 'ladino',
            4: 'paladino',
            5: 'xamã',
            0: 'não filtrar por classe'
        }

        self.__numero_para_nivel = {
            1: 'novato (1 a 15)',
            2: 'adepto (16 a 30)',
            3: 'mestre (31 a 45)',
            4: 'lendário (46 a 60)',
            0: 'não filtrar por nível'
        }

        self._limpar_terminal()

    def _limpar_terminal(self):
        os.system('clear')

    def _pular_linha(self):
        print(' ')

    def _aguardando(self):
        input('Aperte enter para prosseguir.')


    def _recebe_operacao(self, valores_validos):
        validando = True
        while validando:
            try:
                operacao = int(input('Selecione: '))
                if operacao in valores_validos:
                    validando = False
                else:
                    raise Exception
            except:
                print('Valor inválido, tente novamente.')

        return operacao

    def bemvindo(self):
        print('Seja bem-vindo, siga o menu abaixo.')
    
    def operacoes_menu_principal(self):
        self._limpar_terminal()
        
        print('1 - Busca de personagens')
        print('2 - Inclusão de um novo personagem')
        print('3 - Remoção de um personagem')
        print('4 - Mostrar todos os personagens')
        print('5 - Carga de dados')
        print('0 - Sair')

        self._pular_linha()

        return self._recebe_operacao([1, 2, 3, 4, 5, 0])
    
    def _seleciona_nome(self):
        self._limpar_terminal()

        nome = input('Insira um nome: ')

        self._pular_linha()

        return nome

    def _seleciona_raca(self):
        self._limpar_terminal()

        print('Selecione uma raça.')
        
        self._pular_linha()

        for operacao_indice, raca in self.__numero_para_raca.items():
            print(f'{operacao_indice} - {raca}')

        self._pular_linha()

        indice_raca = self._recebe_operacao(list(self.__numero_para_raca.keys()))

        return indice_raca, self.__numero_para_raca.get(indice_raca)
    
    def _seleciona_classe(self):
        self._limpar_terminal()

        for operacao_indice, classe in self.__numero_para_classe.items():
            print(f'{operacao_indice} - {classe}')

        self._pular_linha()

        indice_classe = self._recebe_operacao(list(self.__numero_para_classe.keys()))

        return indice_classe, self.__numero_para_classe.get(indice_classe)
    
    def _seleciona_nivel_grupo(self):
        self._limpar_terminal()

        for operacao_indice, nivel in self.__numero_para_nivel.items():
            print(f'{operacao_indice} - {nivel}')

        self._pular_linha()

        indice_nivel = self._recebe_operacao(list(self.__numero_para_nivel.keys()))

        return indice_nivel, self.__numero_para_nivel.get(indice_nivel)

    def _seleciona_nivel(self):
        self._limpar_terminal()

        print('Insira um nível, de 1 a 60.')

        return self._recebe_operacao([numeros for numeros in range(1, 61)])

    def busca_formulario(self):
        self._limpar_terminal()

        print('Busque personagens com base em raça, classe e nível.')
        self._pular_linha()

        indice_raca, raca = self._seleciona_raca()
        indice_classe, classe = self._seleciona_classe()
        indice_nivel, nivel = self._seleciona_nivel_grupo()

        self._pular_linha()

        print('Busca por:')
        print(f'Raça: {raca}')
        print(f'Classe: {classe}')
        print(f'Nível: {nivel}')

        self._pular_linha()

        self._aguardando()

        return indice_raca, indice_classe, indice_nivel

    def imprime_personagens(self, personagens):
        self._limpar_terminal()

        print('Os personagens encontrados na sua busca são: ')

        self._pular_linha()

        if personagens is None:
            print('Nenhum personagem confere com a busca solicitada.')
        else:
            for personagem in personagens:
                id = personagem['id']
                nome = personagem['nome']
                raca = self.__numero_para_raca.get(personagem['raca'])
                classe = self.__numero_para_classe.get(personagem['classe'])
                nivel = self.__numero_para_nivel.get(personagem['nivel'])

                print(f'ID: {id} | {nome}, {raca} {classe} {nivel}')

        self._pular_linha()

        self._aguardando()

    def imprime_todos_personagens(self, personagens):
        self._limpar_terminal()

        if len(personagens) == 0:
            print('Não há personagens.')
        else:
            print('Os personagens presentes na base de dados são: ')

            for personagem in personagens:
                id = personagem['id']
                nome = personagem['nome']
                raca = self.__numero_para_raca.get(personagem['raca'])
                classe = self.__numero_para_classe.get(personagem['classe'])
                nivel = self.__numero_para_nivel.get(personagem['nivel'])

                print(f'ID: {id} | {nome}, {raca} {classe} {nivel}')

        self._pular_linha()

        self._aguardando()

    def incluir_personagem(self):
        self._limpar_terminal()

        print('Incluir novo personagem, inserido nome, raça, classe e nível.')
        self._pular_linha()

        nome = self._seleciona_nome()
        indice_raca, raca = self._seleciona_raca()
        indice_classe, classe = self._seleciona_classe()
        nivel = self._seleciona_nivel()

        print(f'Inclusão de um {raca} {classe} nível {nivel}, chamado {nome}.')

        self._aguardando()

        return nome, indice_raca, indice_classe, nivel
    
    def remove_personagem(self, indices_validos):
        self._limpar_terminal()

        print('Remova um personagem com base em um ID.')
        self._pular_linha()

        selecionando_id = True
        while selecionando_id:
            try:
                id = int(input('Insira um ID: '))
                if id in indices_validos:
                    selecionando_id = False
                else:
                    print('Não existe personagem com esse ID')
            except:
                print('Valor inválido, IDs são valores inteiros positivos não nulos!')
        
        self._pular_linha()

        print(f'Removendo personagem de índice {id}.')

        self._aguardando()

        return id
    
    def imprime_falta_filtros(self):
        self._limpar_terminal()

        print('É necessário pelo menos um filtro para fazer a busca.')
        print('Se quiser imprimir todos os personagens, utilize a opção 4 do menu principal.')

        self._pular_linha()

        self._aguardando()

    def carrega_dados(self):
        self._limpar_terminal()

        print('Dados carregados.')

        self._pular_linha()

        self._aguardando()

    def dados_carregados(self):
        self._limpar_terminal()

        print('Os dados já foram carregados, não é possível carregar mais de uma vez.')

        self._pular_linha()

        self._aguardando()
