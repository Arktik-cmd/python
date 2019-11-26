s = ["один", "два", "три", "два"]


item = "два"
col = s.count(item)

for i in range(col):
    if item in s:
        s.remove(item)


print(s)