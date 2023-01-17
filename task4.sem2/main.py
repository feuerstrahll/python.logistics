import string
from collections import Counter

def read_file(data):
    file = open(data)
    content = file.read()
    return content

def write_data(file_name, data):
    f = open(file_name, "w")
    f.write(data)
    f.close()

def prepare(data):
    data = ''.join(c for c in data if c not in string.punctuation)
    words = data.lower()
    words_new = words.split()
    base = {}
    for i in words_new:
        if i not in base:
            base.update({i: 1})
        else:
            last_word = base.get(i)
            base.update({i: last_word+1})
    sorted_base = {}
    sorted_keys = sorted(base, key=base.get)
    for w in sorted_keys:
        sorted_base[w] = base[w]
    rev = reversed(sorted_base)
    final = ""
    cnt = Counter(words_new)
    cnt.most_common()
    for key in cnt.most_common(10):
        template = '{} \n'
        final += template.format(key, base.get(key))
    return final
    
    
if __name__ == '__main__':
    g = prepare(read_file('input.txt'))
    write_data('output.txt', g)
    
