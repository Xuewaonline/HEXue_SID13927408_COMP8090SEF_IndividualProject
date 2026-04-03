# Task 1: Course Project (OOP): SmartPET 🐱🐶

**COMP8090SEF Data Structures and Algorithms**

**NAME:** **HE Xue (SID: 13927408)**

---

## 🎤 Topics
SmartPET 🐱🐶 - Pet Shop Management System
![img.png](img.png)

## 📹 Video Link
https://www.youtube.com/watch?v=SWd6C8hPUxs

## 🔗 GitHub Repository
https://github.com/Xuewaonline/HEXue_SID13927408_COMP8090SEF_IndividualProject/tree/main

## 📄 Files

| File | Description                                                           |
|------|-----------------------------------------------------------------------|
| `[Task1]_HEXue_13927408_Course_Project_Report`    | Course Project Report of Task 1                                       |
| `[Task1]_HEXue_13927408_CourseProject_OOP_SmartPET_Video_PPT` | PPT of Course Project                                                 
| `main.py` | Entrance of the application. Contains the user interface and menu system |
| `models.py` | Core data models. Contains `Pet` and `Customer` classes               |
| `petshop.py` | Main controller class. Manages pet inventory, customers, and sales    |
| `utils.py` | Utility functions                                                     |
| `README.md` | User guide                                                            |

---

## 🧑‍🏫 Introduction

**SmartPET** is a console-based Python application designed for managing a pet store.

### 🔧 Core Functions

1. **Managing Pet Inventory**: 
- Add, view, and manage pets with details including name, age, price, breed, and type
2. **Tracking Customers**: 
- Maintain customer records with contact information and purchase history
3. **Processing Sales**: 
- Sell pets to customers with automatic inventory updates and revenue tracking

### 💻 OOP Concepts Demonstrated

| Concept | Implementation |
|---------|---------------|
| **Class & Object** | Three classes: Pet, Customer, PetShop |
| **Encapsulation** | Private attributes with getter/setter methods |
| **Class Attributes** | Shared counters for ID generation |
| **Static Methods** | Price formatting and phone validation |
| **Magic Methods** | __str__, __eq__, __len__ for object operations |
| **Modular Programming** | Code organized into four separate files |

---

## 😼 How to Run  (User Guide)

### Prerequisites
Python

### Running the Application

```bash
python main.py
```

### Main Menu

```
============================================================
         SmartPET - Pet Shop Management System
============================================================
  1. View Shop Information
  2. Add Pet to Inventory
  3. View All Pets
  4. View Available Pets
  5. Add Customer
  6. View All Customers
  7. Process Sale
  8. View Sales History
  9. Generate Sample Data
  0. Exit
```


## 📖 References
- Course Lecture Notes: Object-Oriented Programming_lec_note_2_OOP(2026)
- Python 3 - Episode 33 - Pet Shop Application https://www.youtube.com/watch?v=UQslB5ElFE4
- Object-Oriented Programming https://kblog.ink/?p=302