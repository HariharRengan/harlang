from sys import argv

l = [0] * int(argv[2])

def main(code):
    cur = ''
    mode = 1
    for j in range(len(code)):
        if mode == 2:
            if j < x:
                continue
            mode = 1
            cur = ''
            continue
        i = code[j]
        if i == ';':
            if mode:
                compile_arg(cur)
                cur = ''
                continue
            else:
                cur += ';'
        elif i == '[':
            a = cur.split(' ')
            x = locate(code[j:])
            if a[0] == "IF":
                if a[2] == '=':
                    if l[int(a[1])] == l[int(a[3])]:
                        main(code[j+1:j+x])
                elif a[2] == '>':
                    if l[int(a[1])] > l[int(a[3])]:
                        main(code[j+1:j+x])
                elif a[2] == '<':
                    if l[int(a[1])] < l[int(a[3])]:
                        main(code[j+1:j+x])
                elif a[2] == '!':
                    if l[int(a[1])] != l[int(a[3])]:
                        main(code[j+1:j+x])
            elif a[0] == "DO":
                if a[2] == '=':
                    while l[int(a[1])] == l[int(a[3])]:
                        main(code[j+1:j+x])
                elif a[2] == '>':
                    while l[int(a[1])] > l[int(a[3])]:
                        main(code[j+1:j+x])
                elif a[2] == '<':
                    while l[int(a[1])] < l[int(a[3])]:
                        main(code[j+1:j+x])
                elif a[2] == '!':
                    while l[int(a[1])] != l[int(a[3])]:
                        main(code[j+1:j+x])
            x += j
            cur = ''
            mode = 2
            continue
        cur += i
        
def compile_arg(i):
    arr = i.split(' ')
    if arr[0] == "SET":
        l[int(arr[1])] = int(arr[2])
    elif arr[0] == "OUT":
        print(l[int(arr[1])])
    elif arr[0] == "ADD":
        l[int(arr[1])] += l[int(arr[2])]
    elif arr[0] == "SUB":
        l[int(arr[1])] -= l[int(arr[2])]

def locate(code):
    c = 0
    for i in range(len(code)):
        if code[i] == '[':
            c += 1
        elif code[i] == ']':
            c -= 1
        if c == 0:
            return i
    return -1

if __name__ == "__main__":
    code = open(argv[1] + ".hrl", "r").read().replace('\n', '')
    main(code)
