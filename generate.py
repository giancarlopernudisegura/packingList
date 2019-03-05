# Author: Giancarlo Pernudi Segura
# GitHub: https://github.com/giancarlopernudisegura/packingList
# read the README.md for documentation
# ---

# import statements
from argparse import ArgumentParser
import json

# arguments
ap = ArgumentParser()
ap.add_argument("-S", "--sexe", required=True, help="sexe of user (m/f)")
ap.add_argument("-H", "--hotel", required=False, action="store_true", help="if you're staying somewhere where hygien products will be supplied")
ap.add_argument("-A", "--active", required=False, action="store_true", help="if you're going to be very active or not")
ap.add_argument("-C", "--custom", required=False, help="list custom arrays in config file, separate multiple lists by a comma")
args = vars(ap.parse_args())

# opens the config
with open('conf.json') as data_file:    
    config = json.load(data_file)

# global variables
# None

# prints markdown header1
def title(label):
    print("# %s" % label)

# prints markdown checkbox
def addCheck(element):
    print("- [ ] %s" % element)

def numbered(num, label):
    addCheck("%d %s" % (num, label))

# adds clothing section
def clothing(sexe, days):
    title("Clothing")

    # Why would you need a packing list generator for one day? lmao
    assert days > 1
    if args["active"]:
        days = int(days * config["multiplier"])
    numbered(days, "shirts")
    numbered(days // 2, "pants")
    numbered(days, "socks")
    numbered(days, "underwear")
    if sexe:
        numbered(days, "bras")

def hyg(sexe, hotel):
    title("Hygiene")

    if sexe:
        addCheck("tampons")
    addCheck("deodorant")
    if not hotel:
        addCheck("bodywash/soap")
        addCheck("shampoo")
    addCheck("toothbrush + toothpaste")
    if args["custom"] != None:
        lists = args["custom"].split(',')
        for list in lists:
            title(list)
            for element in config[list]:
                addCheck(element)

def main():
    print("Packing List\n")
    print("---\n")
    sexe = args["sexe"] == 'f'
    clothing(sexe, 5)
    if args["hotel"]:
        hyg(sexe, False)



assert args["sexe"] in ('m', 'f'), "Sexe must be 'm' or 'f'"
main()