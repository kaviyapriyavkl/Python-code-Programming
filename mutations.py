def mutate_string(string, position, character):
    string=string[0:5]+"k"+string[6:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)