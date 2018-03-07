import numpy as np
import nltk
from nltk.tokenize import word_tokenize

def process_data(syl_file, sonnet_file):
    # Construct a dictionary mapping from word -> [# syllables], [# syllables when at the end of the word]
    syl_data = np.loadtxt(syl_file, dtype='str', delimiter='\n')
    syl_dict = {}
    for line in syl_data:
        syl_list = line.split()
        word = syl_list[0]
        syl_dict[word] = [[],[]]
        for i in range(1, len(syl_list)):
            if syl_list[i].startswith('E'):
                syl_dict[word][1].append(int(syl_list[i].lstrip('E')))
            else:
                syl_dict[word][0].append(int(syl_list[i]))

    sonnet_data = np.loadtxt(sonnet_file, dtype='str', delimiter='\n')

    # Construct a sequence of tokens from sonnets.
    sonnets = []
    for line in sonnet_data:
        if line.lstrip().isdigit():
            sonnets.append([])
        else:
            tokens = word_tokenize(line)
            for i, token in enumerate(tokens):
                if (not token.lower() in syl_dict) and (token.lstrip("'").lower() in syl_dict):
                    sonnets[-1].append(token.lstrip("'").lower())
                elif (not token.lower() in syl_dict) and (token.lower() + "'" in syl_dict):
                    sonnets[-1].append(token.lower() + "'")
                elif i != len(tokens) - 1 and (tokens[i+1] == "'s" or tokens[i+1] == "'ll"):
                    sonnets[-1].append(token.lower() + tokens[i+1])
                elif i != len(tokens) - 1 and tokens[i+1] == "is" and tokens[i].lower() == "'t":
                    sonnets[-1].append("'tis")
                elif token in ["'s", "'", "(", ")", "'ll"]:
                    continue
                elif i != 0 and tokens[i-1].lower() == "'t" and tokens[i].lower() == "is":
                    continue
                else:
                    sonnets[-1].append(token.lower())
    syl_dict['grossly'] = [[2], []]
    syl_dict['fickle'] = [[2], []]
    syl_dict['waning'] = [[2], []]
    syl_dict["show'st"] = [[1], []]
    syl_dict['over'] = [[2], []]
    syl_dict['wrack'] = [[1], []]
    syl_dict['withering'] = [[2], []]
    syl_dict['goest'] = [[1], []]
    syl_dict['onwards'] = [[2], []]
    syl_dict['minion'] = [[2], []]
    syl_dict['detain'] = [[2], []]
    syl_dict['delayed'] = [[2], []]
    syl_dict['answered'] = [[2], []]
    syl_dict['quietus'] = [[3], []]

    for punct in ['.',',',':', '?', '!', ';']:
        syl_dict[punct] = [[0],[]]

    num_tokens = 0
    token_dict = {}
    num_dict = {}
    for j, sonnet in enumerate(sonnets):
        for token in sonnet:
            if not token in token_dict:
                token_dict[token] = num_tokens
                num_dict[num_tokens] = token
                num_tokens += 1
    return sonnets, syl_dict, num_dict, token_dict