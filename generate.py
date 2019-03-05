from argparse import ArgumentParser
import json

ap = ArgumentParser()
ap.add_argument("-S", "--sexe", required=True, help="sexe of user (m/f)")
ap.add_argument("-H", "--hotel", required=False, action="store_true", help="if you're staying somewhere where hygien products will be supplied")
ap.add_argument("-A", "--active", required=False, action="store_true", help="if you're going to be very active or not")
args = vars(ap.parse_args())

with open('conf.json') as data_file:    
    config = json.load(data_file)

print("Packing List\n")
print("---\n")
clothes = []

def addCheck(element):
    print("- [ ] %s" % element)

def clothing(sexe, days):
    assert days > 1
    if args["active"]:
        days = int(days * config["multiplier"])
    clothes.append("%d shirts" % days)
    clothes.append("%d pants" % (days // 2))
    clothes.append("%d socks" % days)
    clothes.append("%d underwear" % days)
    if sexe:
        clothes.append("%d bras" % days)

def hyg(sexe, hotel):
    if sexe:
        addCheck("tampons")
    addCheck("deodorant")
    if not hotel:
        addCheck("bodywash/soap")
        addCheck("shampoo")
    addCheck("toothbrush + toothpaste")

def main():
    sexe = args["sexe"] == 'f'
    clothing(sexe, 5)
    print("# Clothing\n")
    for c in clothes:
        addCheck(c)
    if args["hotel"]:
        print("# Hygiene\n")
        hyg(sexe, False)


assert args["sexe"] in ('m', 'f'), "Sexe must be 'm' or 'f'"
main()