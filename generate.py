# Author: Giancarlo Pernudi Segura
# GitHub: https://github.com/giancarlopernudisegura/packingList
# read the README.md for documentation
####

# import statements
from argparse import ArgumentParser
import json
from datetime import date

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

# print title header
def title():
    print("---")
    print("title: %s" % config["title"])
    print("author: %s" % config["author"])
    print("date: %s" % date.today())
    print("...\n")

# prints markdown header1
def section(label):
    print("\n# %s" % label)

# prints markdown checkbox
def addCheck(element):
    print("- [ ] %s" % element)

# prints markdown checkbox with a number infront
def numbered(num, label):
    addCheck("%d %s" % (num, label))

# adds checkboxes from a list in a config
def addList(list, days=0):
    for elem in config[list]:
        if days == 0:
            addCheck(elem)
        else:
            numbered(days, elem)

# adds clothing section
def clothing(sexe):
    section("Clothing")

    days = args["days"]
    if args["active"]:
        days = int(days * config["multiplier"])
    addList("clothing", days)
    if sexe:
        addList("clothingWomen", days)

# adds the hygiene section
def hyg(sexe):
    # sexe is a boolean
    section("Hygiene")

    addList("Hygiene")
    # all the optional items
    if sexe:
        addList("hygieneWomen")
    if not args["hotel"]:
        addList("hygiene!Hotel")

# adds all the custom section defined in the config
def custom():
    if args["custom"] != None:
        lists = args["custom"].split(',')
        for l in lists:
            list = l.strip()
            section(list)
            for element in config[list]:
                addCheck(element)
# runs all the section printing functions
def main():
    title()
    sexe = args["sexe"] == 'f'
    clothing(sexe)
    hyg(sexe)
    custom()

if __name__ == "__main__":
     # Why would you need a packing list generator for one day? lmao
    assert args["days"] > 1, "lmao why do you need a list for one day? It needs to be a minimum of 2"
    assert args["sexe"] in ('m', 'f'), "Sexe must be 'm' or 'f'"
    main()

