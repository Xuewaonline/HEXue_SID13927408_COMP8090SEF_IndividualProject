"""
models.py - Core data models for SmartPET Pet Shop Management System
"""


class Pet:
    # Class attributes - shared by all Pet objects
    total_pets = 0
    pet_id_counter = 100
    
    def __init__(self, name, age, price, breed, pet_type):

        self.__id = Pet.pet_id_counter
        Pet.pet_id_counter += 1
        Pet.total_pets += 1
        self.__name = name
        self.__age = age
        self.__price = price
        self.__breed = breed
        self.__type = pet_type
        self.__is_sold = False
    
    # Getter methods
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_price(self):
        return self.__price
    def get_breed(self):
        return self.__breed
    def get_type(self):
        return self.__type
    def is_sold(self):
        return self.__is_sold
    
    # Setter methods
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        if age > 0:
            self.__age = age
    def set_price(self, price):
        if price >= 0:
            self.__price = price
    def mark_as_sold(self):
        self.__is_sold = True
    
    # Magic method - string representation
    def __str__(self):
        status = "Sold" if self.__is_sold else "Available"
        return "[{}] {} | {} | {} years | ${} | [{}]".format(
            self.__id, self.__name, self.__type, 
            self.__age, self.__price, status
        )
    
    # Magic method - equality comparison
    def __eq__(self, other):
        if isinstance(other, Pet):
            return self.__id == other.get_id()
        return False


class Customer:
    """
    Customer class - represents a shop customer.
    """
    
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone
        self.__purchased_pets = []
    
    def get_name(self):
        return self.__name
    
    def get_phone(self):
        return self.__phone
    
    def buy_pet(self, pet):
        """Purchase a pet"""
        if not pet.is_sold():
            pet.mark_as_sold()
            self.__purchased_pets.append(pet)
            return True
        return False
    
    def get_purchased_pets(self):
        return self.__purchased_pets
    
    def get_total_spent(self):
        total = 0
        for pet in self.__purchased_pets:
            total += pet.get_price()
        return total
    
    def __str__(self):
        return "{} | {} | Purchased {} pets".format(
            self.__name, self.__phone, len(self.__purchased_pets)
        )
