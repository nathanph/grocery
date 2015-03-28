__author__ = 'Nathan Hernandez'

import sys

def main():

    infile, outfile = sys.argv[1], sys.argv[2]
    user_data = {}

    with open(infile) as file:
        for line in file:
            fields = line.split("|")
            customer = get_customer(fields)
            upc = get_upc(fields)
            quantity = get_quantity(fields)
            if customer not in user_data:
                user_data[customer] = {}
            if upc in user_data[customer]:
                total_quantity = int(user_data[customer][upc]) + int(quantity)
                user_data[customer][upc] = total_quantity
            else:
                user_data[customer][upc] = quantity

    file = open(outfile, "w")
    for customer in user_data:
        file.write(customer+"\n")
        for upc in user_data[customer]:
            file.write("\t"+upc+"\t"+str(user_data[customer][upc])+"\n")
        file.write("\n")


def print_user_data(user_data):
    for user in user_data:
        print(user)

def get_upc(fields):
    return fields[12]

def get_quantity(fields):
    return fields[23][0]

def get_customer(fields):
    return fields[0]

if __name__ == "__main__":
    main()
