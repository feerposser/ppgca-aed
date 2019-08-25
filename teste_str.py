f = 137.285714285714286
g = 9.0
print("%.2f" % f)
print('--%.2f' % round(137.285714285714286 * 1000 / 1000,3))
print(f)
print(str(f).find("."))
print(str(f)[:str(f).find(".")+3])

print("----------")

w = 137.285714285714286

x = float (str (w)[:str(w).find(".")+1])
y = float (str (w)[:str(w).find(".")+2])
z = float(str(w)[:str(w).find(".")+3])

print(x, y, z)

print("=====", str(g)[str(g).find(".")+1:])
print(len(str(g)[str(g).find(".")+1:]))

if len(str(g)[str(g).find(".")+1:]) > 1:
    g = str(g)[:str(g).find(".") + 3]
else:
    g = str(g)+"0"

print("G:", g)

h = 137.285714285714286
h = list(str(int(h*100)))
h.insert(-2, ".")
print(str().join(h))

print('========')

ss = "123 456789"

print(ss[:ss.find(' ')])
print(ss[ss.find(' ')+1:])

print('............')

print(ss[0:])

print(ss[:-1])

print("123".find("2"))