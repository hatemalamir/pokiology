import sys
import json
import requests


def run_classifier(pokimon):
    '''
    Input
        pokimon: json object with pokimon properties
    '''
    print(f'>>> Classifying pokimon: {pokimon["name"]} ...')
    pok_class = None
    print(f'Pokimon: {pokimon["name"]} ---> Class: {pok_class}')
    return pok_class


if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as pf:
            pokimon = json.load(pf)
    else:
        pokimon = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu').json()
    pok_class = run_classifier(pokimon)
