# Author: Giancarlo Pernudi Segura
# GitHub: https://github.com/giancarlopernudisegura/packingList
# read the README.md for documentation
####

# import statements
from argparse import ArgumentParser
import json

# arguments
ap = ArgumentParser()
ap.add_argument("-D", "--days", required=True, type=int, help="number of days")
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

def addList(list, days=0):
    for elem in config[list]:
        if days == 0:
            addCheck(elem)
        else:
            numbered(days, elem)

# adds clothing section
def clothing(sexe):
    title("Clothing")

    days = args["days"]
    if args["active"]:
        days = int(days * config["multiplier"])
    addList("clothing", days)
    if sexe:
        addList("clothingWomen", days)

# adds the hygiene section
def hyg(sexe):
    # sexe is a boolean
    title("Hygiene")

    addList("Hygiene")
    # all the optional items
    if sexe:
        addList("hygieneWomen")
    if not args["hotel"]:
        addList("hygieneHotel")

# adds all the custom section defined in the config
def custom():
    if args["custom"] != None:
        lists = args["custom"].split(',')
        for list in lists:
            title(list)
            for element in config[list]:
                addCheck(element)
# runs all the section printing functions
def main():
    print("Packing List\n")
    print("---\n")
    sexe = args["sexe"] == 'f'
    clothing(sexe)
    hyg(sexe)
    custom()

if __name__ == "__main__":
     # Why would you need a packing list generator for one day? lmao
    assert args["days"] > 1
    assert args["sexe"] in ('m', 'f'), "Sexe must be 'm' or 'f'"
    main()

