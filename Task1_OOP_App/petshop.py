"""
petshop.py - Main controller for SmartPET Pet Shop Management System
"""

from models import Pet, Customer


class PetShop:

    shop_name = "SmartPET"
    
    def __init__(self, owner_name):
        """Create a new pet shop"""
        self.__owner = owner_name
        self.__pets = []
        self.__customers = []
        self.__sales_history = []
        self.__total_revenue = 0
    
    # Getter methods
    def get_owner(self):
        return self.__owner
    
    def get_total_revenue(self):
        return self.__total_revenue
    
    def get_pet_count(self):
        return len(self.__pets)
    
    def get_customer_count(self):
        return len(self.__customers)
    
    # ==================== Pet Inventory Management ====================
    
    def add_pet(self, name, age, price, breed, pet_type):
        """Add a new pet to inventory"""
        pet = Pet(name, age, price, breed, pet_type)
        self.__pets.append(pet)
        return pet
    
    def get_all_pets(self):
        """Get all pets in inventory"""
        return self.__pets
    
    def get_available_pets(self):
        """Get all available (not sold) pets"""
        result = []
        for pet in self.__pets:
            if not pet.is_sold():
                result.append(pet)
        return result
    
    def get_sold_pets(self):
        """Get all sold pets"""
        result = []
        for pet in self.__pets:
            if pet.is_sold():
                result.append(pet)
        return result
    
    def find_pet_by_id(self, pet_id):
        """Find a pet by ID"""
        for pet in self.__pets:
            if pet.get_id() == pet_id:
                return pet
        return None
    
    def remove_pet(self, pet_id):
        """Remove a pet from inventory"""
        for i, pet in enumerate(self.__pets):
            if pet.get_id() == pet_id:
                self.__pets.pop(i)
                return True
        return False
    
    # ==================== Customer Tracking ====================
    
    def add_customer(self, name, phone):
        """Add a new customer"""
        customer = Customer(name, phone)
        self.__customers.append(customer)
        return customer
    
    def get_all_customers(self):
        """Get all customers"""
        return self.__customers
    
    def find_customer_by_name(self, name):
        """Find a customer by name"""
        for customer in self.__customers:
            if customer.get_name() == name:
                return customer
        return None
    
    # ==================== Sales Processing ====================
    
    def sell_pet(self, pet_id, customer_name):
        pet = self.find_pet_by_id(pet_id)
        if not pet:
            print("Error: Pet not found!")
            return False
        
        if pet.is_sold():
            print("Error: Pet already sold!")
            return False
        
        customer = self.find_customer_by_name(customer_name)
        if not customer:
            print("Error: Customer not found!")
            return False
        
        if customer.buy_pet(pet):
            self.__total_revenue += pet.get_price()
            self.__sales_history.append({
                "pet": pet,
                "customer": customer,
                "price": pet.get_price()
            })
            print("Sale successful! {} purchased {}".format(customer_name, pet.get_name()))
            return True
        return False
    
    def get_sales_history(self):
        """Get all sales history"""
        return self.__sales_history
    
    # ==================== Business Statistics ====================
    
    def get_inventory_value(self):
        """Calculate total value of available pets"""
        total = 0
        for pet in self.__pets:
            if not pet.is_sold():
                total += pet.get_price()
        return total
    
    # ==================== Static Methods ====================
    
    @staticmethod
    def format_price(price):
        """Static method - Format price for display"""
        return "${}".format(price)
    
    @staticmethod
    def validate_phone(phone):
        """Static method - Validate phone number"""
        if len(phone) != 11:
            return False
        if not phone.isdigit():
            return False
        return True
    
    # ==================== Magic Methods ====================
    
    def __str__(self):
        """String representation of the shop"""
        available = len(self.get_available_pets())
        sold = len(self.get_sold_pets())
        return "{} | Owner:{} | Available:{} | Sold:{} | Revenue:${}".format(
            PetShop.shop_name, self.__owner, available, sold, self.__total_revenue
        )
    
    def __len__(self):
        """Return total number of pets"""
        return self.get_pet_count()
