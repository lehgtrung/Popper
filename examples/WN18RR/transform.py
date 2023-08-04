import pandas as pd
from tqdm import tqdm
import argparse
import re


def convert_to_camel_case(name):
    return ''.join([e.capitalize() for e in name.split('_')])


def load_data(path):
    data = pd.read_csv(path, sep='\t', dtype=str)
    data.columns = ['head', 'relation', 'tail']
    data['relation'] = data['relation'].apply(lambda x: x.strip('_'))
    data['relation'] = data['relation'].apply(lambda x: convert_to_camel_case(x))
    return data


def convert_to_predicates(data):
    result = []
    for i, row in data.iterrows():
        result.append(f'{row["relation"]}(e{row["head"]},e{row["tail"]})')
    return result


def output_bk(predicates, pred_to_learn):
    pos = []
    for line in tqdm(predicates):
        if not line.startswith(pred_to_learn):
            pos.append(f'{line}.')
    with open('bk.pl', 'w') as f:
        f.writelines([e + '\n' for e in pos])


def extract_pred(text):
    pattern = r"(\w+)\((.*?), (.*?)\)"
    return re.findall(pattern, text)[0]


def output_bias(data, pred_to_learn):
    pos = []
    pos.append('max_clauses(100).')
    pos.append('enable_recursion.')
    pos.append(f'head_pred({pred_to_learn},2).')
    predicate_list = data['relation'].unique().tolist()
    for pred in tqdm(predicate_list):
        if not pred.startswith(pred_to_learn):
            pos.append(f'body_pred({pred},2).')

    # for pred in tqdm(predicate_list):
    #     if not pred.startswith(pred_to_learn):
    #         pos.append(f':- discontiguous {pred}/2.')

    with open('bias.pl', 'w') as f:
        f.writelines([e + '\n' for e in pos])


def output_exs(predicates, pred_to_learn):
    pos = []
    for pred in tqdm(predicates):
        if pred.startswith(pred_to_learn):
            pos.append(f'pos({pred}).')
    with open('exs.pl', 'w') as f:
        f.writelines([e + '\n' for e in pos])


if __name__ == '__main__':
    pred_to_learn = 'DerivationallyRelatedForm'
    data = load_data('train.txt')
    predicates = convert_to_predicates(data)
    output_bk(predicates, pred_to_learn)
    output_bias(data, pred_to_learn)
    output_exs(predicates, pred_to_learn)


