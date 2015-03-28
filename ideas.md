# Grocery Hackathon
Predict, model, plan and present the best, most attractive and creative ways to deliver groceries to customers.

## IPs
204.15.96.216  
204.15.96.217  
204.15.96.218  
204.15.96.219  

## Objectives
- Predict
- Model
- Plan

## Data field

1. customer = unique identifier for a customer household (masked)
1. tier = value segment of customer
1. homeStore = store closest to the customer's address
1. homeStoreLat = latitude of home store
1. homeStoreLon = longitude of home store
1. distance = distance from customer's address to homeStore in miles
1. receipt = unique identifier for a basket checkout (masked)
1. elFlag = Boolean flag indicating if the transaction was completed online ("1") or in-store ("0")
1. datetime = date and time of the transaction
1. store = store number where the customer checked out
1. storeLat = latitude of store where the customer checked out
1. storeLon = longitude of the store where the customer checked out
1. upc = unique product identifier (industry standard) and base product segmentation
1. description = description of upc
1. mupc = ID number for level 2 of product hierarchy
1. subcategory = description for level 3 of product hierarchy
1. subcat_num = ID number for level 3 of product hierarchy
1. category = level 4 of product hierarchy
1. cat_num = ID number for level 4 of product hierarchy
1. department = level 5 of product hierarchy
1. dept_num = ID number for level 5 of product hierarchy
1. quantity = number of units purchased
1. sales = summed dollar value of UPC-level purchase (= unit price * quantity)
1. discounts = summed dollar value of discounts

