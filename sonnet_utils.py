import numpy as np
import nltk
from nltk.tokenize import word_tokenize

def process_data_lines(syl_file, sonnet_file):
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
    sonnets = []
    sonnet_lines = []
    for line in sonnet_data:
        if line.lstrip().isdigit():
            sonnets.append([])
            sonnet_lines.append([])
        else:
            tokens = word_tokenize(line)
            sonnet_lines[-1].append([])
            for i, token in enumerate(tokens):
                if (not token.lower() in syl_dict) and (token.lstrip("'").lower() in syl_dict):
                    t = token.lstrip("'").lower()
                    sonnets[-1].append(t)
                    sonnet_lines[-1][-1].append(t)
                elif (not token.lower() in syl_dict) and (token.lower() + "'" in syl_dict):
                    t = token.lower() + "'"
                    sonnets[-1].append(t)
                    sonnet_lines[-1][-1].append(t)
                elif i != len(tokens) - 1 and (tokens[i+1] == "'s" or tokens[i+1] == "'ll"):
                    t = token.lower() + tokens[i+1]
                    sonnets[-1].append(t)
                    sonnet_lines[-1][-1].append(t)
                elif i != len(tokens) - 1 and tokens[i+1] == "is" and tokens[i].lower() == "'t":
                    sonnets[-1].append("'tis")
                    sonnet_lines[-1][-1].append("'tis")
                elif token in ["'s", "'", "(", ")", "'ll"]:
                    continue
                elif i != 0 and tokens[i-1].lower() == "'t" and tokens[i].lower() == "is":
                    continue
                else:
                    t = token.lower()
                    sonnets[-1].append(t)
                    sonnet_lines[-1][-1].append(t)
    
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
    return sonnets, sonnet_lines, syl_dict, num_dict, token_dict

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

# Return a token with the first alphanumeric character capitalized.
def capitalize(token):
    for i, c in enumerate(token):
        if c.isalnum():
            break
    return token[0:i] + c.upper() + token[i+1:(len(token))]           

# Turns the sonnet lines into a sonnet.
def process_lines(sonnet_lines, punct):
    for line in sonnet_lines:
        line.reverse()
    
    processed_lines = [[] for i in range(len(sonnet_lines))]
    for i, line in enumerate(sonnet_lines):
        first_word_idx = i-1 if line[0] in punct else i
        if first_word_idx != -1:
            processed_lines[first_word_idx].append(line[0])
        for j in range(1, len(line)):
            processed_lines[i].append(line[j])
    
    for line in processed_lines:
        line[0] = capitalize(line[0])
        for i, token in enumerate(line):
            if token in ['.', '!', '?'] and i != len(line) - 1:
                line[i+1] = capitalize(line[i+1])
            elif token in ['i', "i'll"]:
                line[i] = capitalize(line[i])
    
    if processed_lines[-1][-1] != '.':
        processed_lines[-1].append('.')
    
    joined_lines = [' '.join(tokens) for tokens in processed_lines]
    return '\n'.join(joined_lines)

def generate_states(hmm, seq_len, word_num):
    emission_probs = [out[word_num] for out in hmm.O]
    sum_probs = sum(emission_probs)
    emission_probs = [prob/float(sum_probs) for prob in emission_probs]
    
    rand = random.random()
    sum_probs = 0
    state = hmm.L - 1
    for i, prob in enumerate(emission_probs):
        sum_probs += prob
        if rand < sum_probs:
            state = i
            break
    states = []
    
    for i in range(0, seq_len):
        rand = random.random()
        sum_probs = 0
        next_state = hmm.L - 1
        for j, prob in enumerate(hmm.A[state]):
            sum_probs += prob
            if rand < sum_probs:
                next_state = j
                break
        states.append(next_state)
        state = next_state
    return states

def generate_emission(hmm, state):
    rand = random.random()
    sum_probs = 0
    for i, prob in enumerate(hmm.O[state]):
        sum_probs += prob
        if rand < sum_probs:
            return i
    
    return hmm.D - 1

def generate_rhyming_sonnet(hmm, syl_dict, num_dict, token_dict, rhyming_dict):
    '''
    Input:
        hmm: HMM
        syl_dict: Maps token -> # syllables
        num_dict: Maps token -> token #
        token_dict: Maps token # -> token
        rhyming_dict: Maps word -> rhyming words
    '''
    sonnet_lines = [[] for i in range(14)]
    rhyming_list = list(rhyming_dict.keys())
    words_to_rhyme = []
    rhyming_words = []
    for pair in [(0,2), (1,3), (4, 6), (5, 7), (8, 10), (9, 11), (12, 13)]:
        word = random.choice(rhyming_list)
        rhyming_word = random.choice(rhyming_dict[word])
        sonnet_lines[pair[0]].append(word)
        sonnet_lines[pair[1]].append(rhyming_word)  
            
    punctuation = ['.',',',':', '?', '!', ';']
        
    prev_token_is_punct = False
    for i, line in enumerate(sonnet_lines):
        states = generate_states(hmm, 20, token_dict[line[0]])
        state = 0

        # List of possible number of syllables in the line so far
        possible_syls = syl_dict[line[0]][0]
        while True:
            token_num = generate_emission(hmm, states[state])
            token = num_dict[token_num]
            token_syls = syl_dict[token]
            next_possible_syls = []
            for num_syls in possible_syls:
                for syls in token_syls[0] + token_syls[1]:
                    next_possible_syls.append(syls + num_syls)

            # Generate another token and try again with the same state. 
            if min(next_possible_syls) > 10:
                continue
            
            cur_token_is_punct = token in punctuation
            if prev_token_is_punct and cur_token_is_punct:
                continue
            
            prev_token_is_punct = cur_token_is_punct
                  
            # Line is complete, go to next line.
            if 10 in next_possible_syls:
                line.append(token)
                break           
            
            # In this case, the line is not complete. Add the token to the sonnet,
            # update possible_syls, and increment state.
            line.append(token)
            state += 1
            possible_syls = [a + b for a in possible_syls for b in token_syls[0]]
    return process_lines(sonnet_lines, punctuation)


def add_rhymes(t1, t2, rhymer):
    if t1 in rhymer:
        if t2 not in rhymer[t1]:
            rhymer[t1].append(t2)
    else:
        rhymer[t1] = [t2]
    if t2 in rhymer:
        if t1 not in rhymer[t2]:
            rhymer[t2].append(t1)
    else: 
        rhymer[t2] = [t1]

def create_rhyming_dict(sonnet_lines):
    # Form a rhyming dictionary, mapping each word to its rhymes.
    rhyming_dict = {}
    for sonnet in sonnet_lines:
        if (len(sonnet) != 14):
            continue
    
        last_tokens = []
        for line in sonnet:
            for i in range(len(line) - 1, -1, -1):
                last_token = line[i]
                if not last_token in ['.',',',':', '?', '!', ';']:
                    break
            last_tokens.append(last_token)
    
        add_rhymes(last_tokens[0], last_tokens[2], rhyming_dict)
        add_rhymes(last_tokens[1], last_tokens[3], rhyming_dict)
        add_rhymes(last_tokens[4], last_tokens[6], rhyming_dict)
        add_rhymes(last_tokens[5], last_tokens[7], rhyming_dict)
        add_rhymes(last_tokens[8], last_tokens[10], rhyming_dict)
        add_rhymes(last_tokens[9], last_tokens[11], rhyming_dict)
        add_rhymes(last_tokens[12], last_tokens[13], rhyming_dict)