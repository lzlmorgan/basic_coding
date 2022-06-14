def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig')as f:  #utf-8-sig去掉文档前缀隐藏符号
        for line in f:
            lines.append(line.strip())
        return lines


def convert(lines):
    new = []
    person = None
    for line in lines:
        s = line.split(' ')
        print(s)
    return new


def write_file(filename, lines):
    with open(filename, 'w')as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    #write_file('output.txt',lines)


main()