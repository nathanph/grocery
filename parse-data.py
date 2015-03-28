__author__ = 'Nathan Hernandez'

import sys
import itertools

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

    products = {}
    with open("products") as file:
        for line in file:
            fields = line.split("|")
            upc = fields[0]
            description = fields[1]
            products[upc] = description[0:-1]


#    for customer_one in user_data:
#       for customer_two in user_data:
#           if customer_one is not customer_two:
#               print("Customer "+str(customer_one)+" & "+str(customer_two))
#               print(manhattan(user_data[customer_one], user_data[customer_two]))

    file = open("recommendations", "w")

    for customer in user_data:
        file.write(str(customer)+"\n")
        # print(nearest_neighbor(customer, user_data))
        show_top = 5
        for recommendation in recommend(customer, user_data):
            if show_top>0:
                file.write("\t"+str(recommendation[0])+" "+str(recommendation[1])+" "+str(products[recommendation[0]])+"\n")
                show_top-=1
            else:
                break
        file.write("\n")

def recommend(customer, user_data):
    # first find nearest neighbor
    nearest = nearest_neighbor(customer, user_data)[0][1]
    recommendations = []
    # now find bands neighbor rated that user didn't
    neighbor_purchases = user_data[nearest]
    user_purchases = user_data[customer]
    for upc in neighbor_purchases:
        if not upc in user_purchases:
            recommendations.append((upc, neighbor_purchases[upc]))
    # using the fn sorted for variety - sort is more efficient
    return sorted(recommendations, key=lambda product_tuple: int(product_tuple[1]), reverse = True)

def manhattan(user_one, user_two):
    distance = 0
    for key in user_one:
        if key in user_two:
            distance += abs(int(user_one[key]) - int(user_two[key]))
    return distance

def nearest_neighbor(customer, user_data):
    distances = []
    for user in user_data:
        if user != customer:
            distance = manhattan(user_data[user], user_data[customer])
            distances.append((distance, user))
    # sort based on distance -- closest first
    distances.sort()
    return distances

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
