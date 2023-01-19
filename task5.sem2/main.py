def formatted_to_anagrams(data):
    dict_f_a = {}
    list_f_a = []
    for word in data:
        s_word = ''.join(sorted(word))
        if s_word in dict_f_a:
	        dict_f_a[s_word].append(word)
        else:
	        dict_f_a[s_word] = [word]
    for w in list(dict_f_a.values()):
        list_f_a.append(sorted(w))
    return list_f_a

words = ["eat","tea","tan","ate","nat","bat"]
print(formatted_to_anagrams(words))

