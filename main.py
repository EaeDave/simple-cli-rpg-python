from random import randint

lista_npcs = []  # Lista inicialmente vazia

player = {
    'nome': 'Laerze',
    'level': 1,
    'exp': 0,
    'exp_max': 50,
    'hp': 100,
    'hp_max': 100,
    'dano': 25,

}

# Função responsável por criar o NPC
def criar_npc():
    level = randint(0, 20)

    npc = {
        'nome': f'Monstro #{level}',
        'level': level,
        'dano': 5 * level,
        'hp': 100 * level,
        'exp': 7 * level
    }

    return npc


# Função responsável por gerar os NPCs
def gerar_npcs(numero_npcs):
    for x in range(numero_npcs):
        npc = criar_npc()
        lista_npcs.append(npc)


# Função responsável por exibir os NPCs
def exibir_npcs():
    for npc in lista_npcs:
        print(f'Nome: {npc['nome']} | Level: {npc['level']} | Dano: {npc['dano']} | HP: {npc['hp']}')


def atacar_npc(npc):
    npc['hp'] -= player['dano']

