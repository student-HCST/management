# Veda Technology
# Business and Services Management System

customers = []
services = [
    {"id": 1, "name": "Web Development", "price": 5000},
    {"id": 2, "name": "Python Development", "price": 3000},
    {"id": 3, "name": "Digital Marketing", "price": 4000},
    {"id": 4, "name": "Software Development", "price": 8000}
]

bookings = []


def add_customer():
    print("\n--- Add New Customer ---")

    name = input("Enter Customer Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    customer = {
        "name": name,
        "phone": phone,
        "email": email
    }

    customers.append(customer)

    print("Customer Added Successfully!")


def view_customers():
    print("\n--- Customer List ---")

    if len(customers) == 0:
        print("No Customer Found")
    else:
        for customer in customers:
            print("Name:", customer["name"])
            print("Phone:", customer["phone"])
            print("Email:", customer["email"])
            print("--------------------")


def view_services():
    print("\n--- Available Services ---")

    for service in services:
        print("ID:", service["id"])
        print("Service:", service["name"])
        print("Price: Rs.", service["price"])
        print("--------------------")


def book_service():
    print("\n--- Book a Service ---")

    name = input("Enter Customer Name: ")

    found = False

    for customer in customers:
        if customer["name"].lower() == name.lower():
            found = True
            break

    if found:
        view_services()

        service_id = int(input("Enter Service ID: "))

        for service in services:
            if service["id"] == service_id:

                booking = {
                    "customer": name,
                    "service": service["name"],
                    "price": service["price"]
                }

                bookings.append(booking)

                print("Service Booked Successfully!")
                print("Total Bill: Rs.", service["price"])
                return

        print("Invalid Service ID")

    else:
        print("Customer Not Found")


def view_bookings():
    print("\n--- All Bookings ---")

    if len(bookings) == 0:
        print("No Booking Found")
    else:
        for booking in bookings:
            print("Customer:", booking["customer"])
            print("Service:", booking["service"])
            print("Price: Rs.", booking["price"])
            print("--------------------")


def search_customer():
    print("\n--- Search Customer ---")

    name = input("Enter Customer Name: ")

    found = False

    for customer in customers:
        if customer["name"].lower() == name.lower():
            print("Customer Found!")
            print("Name:", customer["name"])
            print("Phone:", customer["phone"])
            print("Email:", customer["email"])
            found = True

    if not found:
        print("Customer Not Found")


# Main Program

while True:

    print("\n================================")
    print("       VEDA TECHNOLOGY")
    print(" BUSINESS AND SERVICES MANAGEMENT")
    print("================================")

    print("1. Add Customer")
    print("2. View Customers")
    print("3. View Services")
    print("4. Book Service")
    print("5. View Bookings")
    print("6. Search Customer")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_customer()

    elif choice == "2":
        view_customers()

    elif choice == "3":
        view_services()

    elif choice == "4":
        book_service()

    elif choice == "5":
        view_bookings()

    elif choice == "6":
        search_customer()

    elif choice == "7":
        print("Thank You for Using Veda Technology!")
        break

    else:
        print("Invalid Choice! Please Try Again.")