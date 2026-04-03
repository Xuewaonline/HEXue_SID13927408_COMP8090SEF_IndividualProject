
from petshop import PetShop
from utils import generate_sample_data, print_line, print_header, print_menu

def show_shop_info(shop):
    print_header("Shop Information")
    print("  Shop Name: {}".format(PetShop.shop_name))
    print("  Owner: {}".format(shop.get_owner()))
    print("  Total Pets: {}".format(shop.get_pet_count()))
    print("  Available Pets: {}".format(len(shop.get_available_pets())))
    print("  Sold Pets: {}".format(len(shop.get_sold_pets())))
    print("  Customers: {}".format(shop.get_customer_count()))
    print("  Total Revenue: ${}".format(shop.get_total_revenue()))
    print("  Inventory Value: ${}".format(shop.get_inventory_value()))


def add_pet_ui(shop):
    """Adding a pet to inventory"""
    print_header("Add Pet to Inventory")
    
    name = input("  Pet name: ").strip()
    
    try:
        age = int(input("  Pet age (years): "))
        price = int(input("  Pet price ($): "))
    except ValueError:
        print("  Error: Age and price must be numbers!")
        return
    
    breed = input("  Breed: ").strip()
    pet_type = input("  Type (Dog/Cat/Bird): ").strip()
    
    pet = shop.add_pet(name, age, price, breed, pet_type)
    print("\n  Pet added successfully! ID: {}".format(pet.get_id()))


def view_all_pets(shop):
    """View all pets in inventory"""
    print_header("All Pets")
    
    pets = shop.get_all_pets()
    if not pets:
        print("  No pets in inventory")
        return
    
    print("  {:<6} {:<12} {:<10} {:<8} {:<10} {:<10}".format(
        "ID", "Name", "Type", "Age", "Price", "Status"
    ))
    print_line("-", 70)
    
    for pet in pets:
        status = "Sold" if pet.is_sold() else "Available"
        print("  {:<6} {:<12} {:<10} {:<8} {:<10} {:<10}".format(
            pet.get_id(), pet.get_name(), pet.get_type(),
            pet.get_age(), pet.get_price(), status
        ))


def view_available_pets(shop):
    """View available pets"""
    print_header("Available Pets")
    
    pets = shop.get_available_pets()
    if not pets:
        print("  No available pets")
        return
    
    for pet in pets:
        print("  " + str(pet))


def add_customer_ui(shop):
    """UI for adding a customer"""
    print_header("Add Customer")
    
    name = input("  Customer name: ").strip()
    phone = input("  Phone number: ").strip()
    
    if not PetShop.validate_phone(phone):
        print("  Error: Invalid phone number! Must be 11 digits.")
        return
    
    customer = shop.add_customer(name, phone)
    print("\n  Customer added successfully!")
    print("  " + str(customer))


def view_all_customers(shop):
    """View all customers"""
    print_header("Customer List")
    
    customers = shop.get_all_customers()
    if not customers:
        print("  No customers")
        return
    
    for customer in customers:
        print("  " + str(customer))
        pets = customer.get_purchased_pets()
        if pets:
            print("    Purchase history:")
            for pet in pets:
                print("      - {} ({})".format(pet.get_name(), pet.get_type()))


def process_sale_ui(shop):
    """UI for processing a sale"""
    print_header("Process Sale")
    
    # Show available pets
    print("  Available pets:")
    available_pets = shop.get_available_pets()
    if not available_pets:
        print("  No available pets!")
        return
    
    for pet in available_pets:
        print("    ID:{} {} {} ${}".format(
            pet.get_id(), pet.get_name(), 
            pet.get_type(), pet.get_price()
        ))
    
    try:
        pet_id = int(input("\n  Enter pet ID: "))
    except ValueError:
        print("  Error: ID must be a number!")
        return
    
    # Show customers
    print("\n  Customer list:")
    customers = shop.get_all_customers()
    if not customers:
        print("  No customers. Please add a customer first!")
        return
    
    for customer in customers:
        print("    - {}".format(customer.get_name()))
    
    customer_name = input("\n  Enter customer name: ").strip()
    
    # Process sale
    shop.sell_pet(pet_id, customer_name)


def view_sales_history(shop):
    """View sales history"""
    print_header("Sales History")
    
    history = shop.get_sales_history()
    if not history:
        print("  No sales history")
        return
    
    print("  {:<6} {:<12} {:<12} {:<10}".format(
        "No.", "Pet", "Customer", "Price"
    ))
    print_line("-", 50)
    
    for i, record in enumerate(history, 1):
        print("  {:<6} {:<12} {:<12} {:<10}".format(
            i,
            record["pet"].get_name(),
            record["customer"].get_name(),
            record["price"]
        ))
    
    print_line("-", 50)
    print("  Total Revenue: ${}".format(shop.get_total_revenue()))


def main():
    """Main function - Program starts here"""
    print_line("=", 70)
    print("     Welcome to SmartPET - Pet Shop Management System")
    print_line("=", 70)
    
    # Create shop
    owner = input("\nEnter owner name: ").strip()
    if not owner:
        owner = "Owner"
    
    shop = PetShop(owner)
    
    print("\nWelcome, {}!".format(shop.get_owner()))
    print("Your pet shop is now open!")
    
    # Main loop
    while True:
        print_menu()
        choice = input("Enter option: ").strip()
        
        if choice == "1":
            show_shop_info(shop)
        elif choice == "2":
            add_pet_ui(shop)
        elif choice == "3":
            view_all_pets(shop)
        elif choice == "4":
            view_available_pets(shop)
        elif choice == "5":
            add_customer_ui(shop)
        elif choice == "6":
            view_all_customers(shop)
        elif choice == "7":
            process_sale_ui(shop)
        elif choice == "8":
            view_sales_history(shop)
        elif choice == "9":
            generate_sample_data(shop)
        elif choice == "0":
            print("\nThank you for using SmartPET!")
            print("Goodbye!")
            break
        else:
            print("\n  Invalid option. Please try again.")
        
        input("\nPress Enter to continue...")


# Program entry point
if __name__ == "__main__":
    main()
