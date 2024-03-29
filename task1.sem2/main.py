def pre(data):
    with open(data, 'r+') as fp:
        qwer = fp.readlines()
        for line in range(len(qwer)):
            l = qwer[line]
            q = l[(l.index(' ')+1):]
            qwer[line] = q.replace('\n', '')
    return qwer


def sor(data):
    qwer = pre(data)
    def sortre(qwer):
        return qwer[0]
    qwer.sort(key=sortre)
    sortre(qwer)
    output = []
    for i in range(len(qwer)):
        qw = qwer[i].split(': ')
        output.append([])
        for q in qw:
            output[i].append(q)
    return output


def out(data):
    import csv 
    data = sor(data)
    file = open('output.csv', 'w+', newline ='') 
    with file:     
        write = csv.writer(file) 
        write.writerow(['name', 'grade'])
        write.writerows(data)
        
if __name__ == '__main__':
    out("data.txt")
