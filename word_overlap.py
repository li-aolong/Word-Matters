import json
import random
import sys
import re
import multiprocessing
def remove_special_characters(strings):
    pattern = r"[^a-zA-Z0-9\s]"
    return [re.sub(pattern, '', string) for
    string in strings]

def remove_special_words(strings):
    with open('your_words_path.txt', 'r') as f:
        lines = f.read().splitlines()
    for i, word1 in enumerate(lines):
        for j, word2 in enumerate(strings):
            if word1 == word2:
                strings[j] = ''

    return strings
def remove_blank(string):
    for i in range(string.count('')):
            string.remove('')
    return string
def count_overlap(string1, string2):
    count = 0
    string1 = set(string1)
    for i, word1 in enumerate(string1):
        for j, word2 in enumerate(string2):
            if word1 == word2:
                count = count + 1
    return count

def make_words(location1, location2, test ,train):
    count = 0
    length = 0
    with open(location1, 'r') as f:
        file1 = json.load(f)['instances']
        random.shuffle(file1)
    with open(location2, 'r') as f:
        file2 = json.load(f)['instances']
        random.shuffle(file2)
    for i, obj1 in enumerate(file1):
            text = obj1['text']
            word = text.split()
            filtered_strings1 = remove_blank(remove_special_characters(remove_special_words(word)))
            for j, obj2 in enumerate(file2):
                if j == 'your_train_dataset_length':
                    break
                text = obj2['text']
                word = text.split()
                filtered_strings2 = remove_blank(remove_special_characters(remove_special_words(word)))
                count = count_overlap(filtered_strings1, filtered_strings2) + count
                length = len(filtered_strings2) + length
            if i == 'your_test_dataset_length':
                break
    overlap = count / length
    print(f'{test} {train} overlap is %s' % overlap)
    return

location1 = ['yout_test_dataset_path.json']
location2 = ['your_train_dataset_path.json']
tests = ['yout_test_dataset_name']
trains = ['your_train_dataset_name']
for i, test in enumerate(zip(location1, tests)):
    for j, train in enumerate(zip(location2, trains)):
        p = multiprocessing.Process(target=make_words, args=(test[0], train[0], test[1], train[1]))
        p.start()