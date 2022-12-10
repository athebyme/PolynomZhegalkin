def Polynimus(a, names=None):
    if names is None:
        names = "x1 x2 x3 x4".split(" ")
    res = []
    out = []
    s = {'0001': [names[3]], '0010': [names[2]], '0011': [names[2], names[3]], '0100': [names[1]],\
         '0101': [names[1], names[3]], '0110': [names[1], names[2]], '0111': [names[1], names[2], names[3]],\
         '1000': [names[0]], '1001': [names[0], names[3]], '1010': [names[0], names[2]], '1011': [names[0], names[2], names[3]],\
         '1100': [names[0], names[1]], '1101': [names[0], names[1], names[3]], '1110': [names[0], names[1], names[2]],\
         '1111': [names[0], names[1], names[2], names[3]]}
    for x in range(len(a)):
        t = bin(x)[2:]
        if len(t) < 4:
            t = '0' * (4 - len(t)) + t
        res.append(t)

    print("formula = (a[0]) ^ (x1 * a[8]) ^ (x2 * a[4]) ^ (x3 * a[2]) ^ (x4 * a[1]) ^ (x1 * x2 * a[12]) ^ (x1 * x3 * a[10]) ^"
          "(x1 * x4 * a[9]) ^ (x2 * x3 * a[6]) ^ (x2 * x4 * a[5]) ^ (x3 * x4 * a[3]) ^ (x1 * x2 * x3 * a[14]) ^"
          "(x1 * x2 * x4 * a[13]) ^ (x1 * x3 * x4 * a[11]) ^ (x2 * x3 * x4 * a[7]) ^ (x1 * x2 * x3 * x4 * a[15])\n\n")

    for i in range(len(res)):
        c1, c2, c3, c4 = list(map(lambda c: int(c), res[i]))
        forprint = f"({a[0]}) ^ ({c1} * {a[8]}) ^ ({c2} * {a[4]}) ^ ({c3} * {a[2]}) ^ ({c4} * {a[1]}) ^ ({c1} * {c2} * {a[12]}) ^ ({c1} * {c3} * {a[10]}) ^"\
                  f"({c1} * {c4} * {a[9]}) ^ ({c2} * {c3} * {a[6]}) ^ ({c2} * {c4} * {a[5]}) ^ ({c3} * {c4} * {a[3]}) ^ ({c1} * {c2} * {c3} * {a[14]}) ^"\
                  f"({c1} * {c2} * {c4} * {a[13]}) ^ ({c1} * {c3} * {c4} * {a[11]}) ^ ({c2} * {c3} * {c4} * {a[7]}) ^ ({c1} * {c2} * {c3} * {c4} * {a[15]})"
        formula = (a[0]) ^ (c1 * a[8]) ^ (c2 * a[4]) ^ (c3 * a[2]) ^ (c4 * a[1]) ^ (c1 * c2 * a[12]) ^ (c1 * c3 * a[10]) ^ \
                  (c1 * c4 * a[9]) ^ (c2 * c3 * a[6]) ^ (c2 * c4 * a[5]) ^ (c3 * c4 * a[3]) ^ (c1 * c2 * c3 * a[14]) ^ \
                  (c1 * c2 * c4 * a[13]) ^ (c1 * c3 * c4 * a[11]) ^ (c2 * c3 * c4 * a[7]) ^ (c1 * c2 * c3 * c4 * a[15])
        out.append(formula)
        print(f'[{c1}, {c2}, {c3}, {c4}] :  res: {formula}  // : {forprint}')
    res_s = ""
    for i in range(len(res)):
        if out[i] != 0:
            t = s.get(res[i])
            n = ""
            for l in t:
                n += l
            res_s += f"{n} ⊕ "
    res_s = res_s[:len(res_s)-2]
    print(f'\n\nres: {res_s}')

if __name__ == '__main__':
    success = False
    func_vector = ""
    while not success:
        try:
            a = input()
            func_vector = list(map(lambda x: (int(x)), a.split()))
            if len(func_vector) == 16: success = True
            else: print("Check vector of truth. It has incorrect length")
        except ValueError:
            print('Value Error. Enter correct vector of truth')
    Polynimus(func_vector, names = ['a', 'b', 'c', 'd'])
