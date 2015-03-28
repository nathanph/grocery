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

- customer = unique identifier for a customer household (masked)
- tier = value segment of customer
- homeStore = store closest to the customer's address
- homeStoreLat = latitude of home store
- homeStoreLon = longitude of home store
- distance = distance from customer's address to homeStore in miles
- receipt = unique identifier for a basket checkout (masked)
- elFlag = Boolean flag indicating if the transaction was completed online ("1") or in-store ("0")
- datetime = date and time of the transaction
- store = store number where the customer checked out
- storeLat = latitude of store where the customer checked out
- storeLon = longitude of the store where the customer checked out
- upc = unique product identifier (industry standard) and base product segmentation
- description = description of upc
- mupc = ID number for level 2 of product hierarchy
- subcategory = description for level 3 of product hierarchy
- subcat_num = ID number for level 3 of product hierarchy
- category = level 4 of product hierarchy
- cat_num = ID number for level 4 of product hierarchy
- department = level 5 of product hierarchy
- dept_num = ID number for level 5 of product hierarchy
- quantity = number of units purchased
- sales = summed dollar value of UPC-level purchase (= unit price * quantity)
- discounts = summed dollar value of discounts

