def read_file(data):
    openlist = []
    with open("input.txt") as file:
        while (line:= file.readline().rstrip()):
            openlist.append(line)
    return openlist

def prepare(data):
    spisok = []
    first_step = read_file(data)
    for i in range(len(first_step)):
        one = first_step[i].index(' ')
        two = first_step[i][6:one]
        spisok.append([])
        spisok[i].append(float(two))
        spisok[i].append(first_step[i])
    return spisok
    
def sort_and_out(data):
    spisok = prepare(data)
    def sortre(spisok):
        return spisok[0]
    spisok.sort(key=sortre)
    sortre(spisok)
    with open("output.txt", "w") as file:
        for elem in spisok:
            file.write(elem[1] + '\n')
    return file
    
if __name__ == '__main__':
    rfile = open("input.txt")
    sort = sort_and_out(rfile)
    
