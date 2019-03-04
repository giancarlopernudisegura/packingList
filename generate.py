print("Packing List\n")
print("---\n")
clothes = []

def addCheck(element):
    print("- [ ] %s\n" % element)

def clothing(days):
    assert days > 1
    clothes.append("%d shirts" % days)
    clothes.append("%d pants" % (days // 2))
    clothes.append("%d socks" % days)
    clothes.append("%d undergarments" % days)

def hyg(sexe, hotel):
    if sexe:
        addCheck("tampons")
    addCheck("deodorant")
    if not hotel:
        addCheck("bodywash/soap")
        addCheck("shampoo")
    addCheck("toothbrush + toothpaste")


clothing(5)
print("# Clothing\n")
for c in clothes:
    addCheck(c)
print("# Hygiene\n")
hyg(True, False)