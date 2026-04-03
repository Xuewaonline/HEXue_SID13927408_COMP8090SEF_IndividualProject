"""
utils.py - Utility functions for SmartPET Pet Shop Management System
"""

def generate_sample_data(shop):
    """Generate sample data for testing"""
    # Add sample pets
    shop.add_pet("Piggy", 1, 500, "Tabby", "Cat")
    shop.add_pet("Max", 1, 800, "Poodle", "Dog")
    shop.add_pet("Oliver", 2, 600, "Orange Tabby", "Cat")

    # Add sample customers
    shop.add_customer("Tom", "13800138000")
    shop.add_customer("Tim", "13900139000")
    print("Sample data generated!")


def print_line(char="=", length=60):
    """Print a line of characters"""
    print(char * length)


def print_header(title):
    """Print a header with title"""
    print_line()
    print("  " + title)
    print_line()


def print_menu():
    """Print the main menu"""
    print("\n")
    print_line("=", 60)
    print("         SmartPET - Pet Shop Management System")
    print_line("=", 60)
    print("  1. View Shop Information")
    print("  2. Add Pet to Inventory")
    print("  3. View All Pets")
    print("  4. View Available Pets")
    print("  5. Add Customer")
    print("  6. View All Customers")
    print("  7. Process Sale")
    print("  8. View Sales History")
    print("  9. Generate Sample Data")
    print("  0. Exit")
    print_line("-", 60)
