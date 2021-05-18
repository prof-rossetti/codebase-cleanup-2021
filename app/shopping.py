import os
from datetime import datetime
from pandas import read_csv

#Format USD function
#Did this in Prof's class

def format_usd(my_price):
    return f"${my_price:,.2f}"

#Product function 
#We did this in class! 
def find_product(product_num, product_list):
    '''
    Parameters:
    product num as a string (eg: "2")
    product_list as a list of dicts
    Returns: that product's dictionary (if it exists)
    '''
    matching_products = [p for p in product_list if str(p["id"]) == str(product_num)]
    if any(matching_products):
        return matching_products[0]
    else:
        return None

if __name__ == '__main__':

    # READ INVENTORY OF PRODUCTS

    products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
    products_df = read_csv(products_filepath)
    products = products_df.to_dict("records")

    # CAPTURE PRODUCT SELECTIONS

    selected_products = []
    while True:
        selected_id = input("Please select a product identifier: ")
        if selected_id.upper() == "DONE":
            break
        else:
            matching_product = find_product(selected_id, products)
            if matching_product:
                selected_products.append(matching_product)
            else:
                print("OOPS, Couldn't find that product. Please try again.")

    checkout_at = datetime.now()

    subtotal = sum([float(p["price"]) for p in selected_products])

    # PRINT RECEIPT

    TAXRATE = .0875

    print()
    print()
    print("----------------")
    print("YOUR RECEIPT:")
    print("----------------")
    print()
    print("CHECKOUT AT: " + str(checkout_at.strftime("%Y-%M-%d %H:%m:%S")))
    print()
    for p in selected_products:
        print("---------------------------------------------------------------")
        print("SELECTED PRODUCT: " + p["name"] + "   " + format_usd(p["price"]))

    print("___________________")
    print(f"SUBTOTAL: {format_usd(subtotal)}")
    print(f"TAX: {format_usd(subtotal * TAXRATE)}")
    print(f"TOTAL: {format_usd(subtotal * TAXRATE + subtotal)}")
    print("-----------------------------------")
    print("THANK YOU! PLEASE COME AGAIN SOON!")
    print("-----------------------------------")

    # WRITE RECEIPT TO FILE

    receipt_id = checkout_at.strftime('%Y-%M-%d-%H-%m-%S')
    receipt_filepath = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{receipt_id}.txt")

    with open(receipt_filepath, "w") as receipt_file:
        receipt_file.write("------------------------------------------")
        for p in selected_products:
            receipt_file.write("\nSELECTED PRODUCT: " + p["name"] + "   " + format_usd(p["price"]))

        receipt_file.write("\n---------")
        receipt_file.write(f"\nSUBTOTAL: {subtotal}")
        receipt_file.write(f"\nTAX: {format_usd(subtotal * TAXRATE)}")
        receipt_file.write(f"\nTOTAL: {format_usd((subtotal * TAXRATE) + subtotal)}")
        receipt_file.write("\n---------")
        receipt_file.write("\nTHANK YOU! PLEASE COME AGAIN SOON!")
        receipt_file.write("\n---------")