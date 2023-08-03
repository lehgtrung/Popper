
from tqdm import tqdm


def output_exs(data):
    pos = []
    for line in tqdm(data):
        pos.append(f'pos({line}).')
    with open('exs.pl', 'w') as f:
        f.writelines([e + '\n' for e in pos])


def output_bk(data):
    pos = []
    for line in tqdm(data):
        pos.append(f'{line}.')
    with open('bk.pl', 'w') as f:
        f.writelines([e + '\n' for e in pos])


def read_data():
    with open('kinship.data', 'r') as f:
        data = f.readlines()
    data = [e.strip().lower() for e in data if e != '\n']
    return data


if __name__ == '__main__':
    data = read_data()
    output_exs(data)
    output_bk(data)


