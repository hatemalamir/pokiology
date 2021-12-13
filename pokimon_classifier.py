import sys
import json
import requests


def run_classifier(pokimon):
    '''
    Input
        pokimon: json object with pokimon properties
    '''
    print(f'>>> Preprocessing pokimon: {pokimon["name"]} ...')
    pok_attributes, pok_true_classes = preprocess(pokimon)
    print(f'<<< Preprocessing pokimon: {pokimon["name"]} done!\n')

    print(f'>>> Classifying pokimon: {pokimon["name"]} ...')
    pok_classes = random_forest_classifier(pok_attributes)
    print(f'<<< Predicted class: {pok_classes}, true classes: {pok_true_classes}\n')
    return pok_classes


def preprocess(pokimon_raw):
    pokimon_attributes = {
        'base_experience': pokimon_raw['base_experience'],
        'height': pokimon_raw['height'],
        'weight': pokimon_raw['weight'],
        'order': pokimon_raw['order'],
    }
    # TODO: extract the rest of useful attribute
    # TODO: encode categorical variables

    pokimon_true_classes = []
    for pok_type in pokimon_raw['types']:
        pokimon_true_classes.append(pok_type['name'])
    # TODO: vector-encode classes

    return pokimon_attributes, pokimon_true_classes


def random_forest_classifier(pokimon_attributes):
    pok_classes = None
    # TODO: build (or load) classifier from training data
    return pok_classes


if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as pf:
            pokimon = json.load(pf)
    else:
        pokimon = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu').json()
    pok_class = run_classifier(pokimon)
