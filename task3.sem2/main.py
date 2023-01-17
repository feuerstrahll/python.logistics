def read_file(data):
    with open('input.txt') as file:
        line = file.readline()
        l = line.split()
    return l

def formatted_file(data):
    spisok = ''
    file2 = open('output.txt', 'w')
    l = read_file(data)
    for i in l:
        if (len(spisok)+len(i)) <= 20:
            spisok += i+' '
        else:
            file2.write(spisok+'\n')
            spisok = i+' '
    return file2.write(spisok)
    
if __name__ == '__main__':
    rfile = read_file("input.txt")
    formatted_file(rfile)
    
