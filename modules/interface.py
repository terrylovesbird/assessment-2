from .customer import Customer
from .inventory import Inventory
import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
c_path = os.path.join(my_path, "../data/customers.csv")
i_path = os.path.join(my_path, "../data/inventory.csv")

class Interface:
    
    menu_options = [
        "1. View video inventory",
        "2. View customer's rented videos",
        "3. Rent video",
        "4. Return video",
        "5. Add new customer",
        "6. Exit"
    ]

    def __init__(self):
        self.customers = Customer.all_customers()
        self.inventory = Inventory.all_videos()
    
    def run(self):
        while True:
            self.print_menu()
            choice = self.get_user_menu_choice()
            print("")

            if choice == 1:
                self.view_video_inventory()

            elif choice == 2:
                self.view_customer_rented_videos()

            elif choice == 3:
                self.rent_video()
                    
            elif choice == 4:
                self.return_video()

            elif choice == 5:
                self.add_new_customer()

            elif choice == 6: #or choice == 0:
                break # quit

            print("")
            
    def print_menu(self):
        print("Welcome to Code Platoon Video!")
        for option in self.menu_options:
            print(option)
        print('\n')

    def get_user_menu_choice(self):
        num_choices = len(self.menu_options)
        # if no menu options, return 0 (force quit)
        if num_choices == 0:
            return 0
        
        # prompt user to enter a valid choice (1-num_choices)
        choice = 0
        while choice == 0 or choice > num_choices: 
            choice = int(input(f"...Select choice (1-{num_choices}): "))

        return choice

    def view_video_inventory(self):
        for i, v in enumerate(self.inventory):
            print(f'{v.id} {v.title} {v.rating} {v.copies_available}')

    def view_customer_rented_videos(self):
        id = input("Enter the customer's ID: ")
        for i, c in enumerate(self.customers):
            if c.id == id:
                print(f'ID:{c.id}, name:{c.first_name} {c.last_name}, rents:{c.current_video_rentals}')

    def rent_video(self):
        title = input("The title of the video for rent: ")
        id = input("Enter the customer's ID: ")
        for c in self.customers:
            nums_videos = len(list(c.current_video_rentals.split('/')))
            if c.id == id and nums_videos >= 3: 
                print('You reach the rent limit')
                return
            elif c.id == id and nums_videos < 3:
                #print('temp_c got')
                temp_c = c

        for v in self.inventory:
            if v.title == title and int(v.copies_available) > 0:
                #print('title got')
                v.copies_available = int(v.copies_available) - 1

                c_list = list(temp_c.current_video_rentals.split('/'))
                c_list.append(title) #append
                c_string = '/'.join(c_list)

                for c in self.customers:
                    if c.id == temp_c.id:
                        c.current_video_rentals = c_string

            elif v.title == title and int(v.copies_available) == 0:
                
                print('Copies not enough')
                return
        self.save_to_inventory()
        self.save_to_customer()
        print("Your rent finished")

    def return_video(self):
        title = input("The title of the video for return: ")
        id = input("Enter the customer's ID: ")
        for c in self.customers:
            
            if c.id == id:
                #print('temp_c got')
                temp_c = c

        for v in self.inventory:
            if v.title == title:
                #print('title got')
                v.copies_available = int(v.copies_available) + 1

                c_list = list(temp_c.current_video_rentals.split('/'))
                c_list.remove(title) #remove
                c_string = '/'.join(c_list)

                for c in self.customers:
                    if c.id == temp_c.id:
                        c.current_video_rentals = c_string

        self.save_to_inventory()
        self.save_to_customer()
        print("Your return finished")



    def save_to_customer(self):
        with open(c_path, 'w') as c_csvfile:
            c_csv = csv.writer(c_csvfile)
            #c_csv.writerow(['id','first_name','last_name','current_video_rentals'])
            for x in self.customers:
                c_csv.writerow([x.id, x.first_name, x.last_name, x.current_video_rentals])


    def save_to_inventory(self):
        with open(i_path, 'w') as i_csvfile:
            i_csv = csv.writer(i_csvfile)
            #i_csv.writerow(['id','title','rating','copies_available'])
            for i in self.inventory:
                i_csv.writerow([i.id, i.title, i.rating, i.copies_available])

    def add_new_customer(self):
        id = input("Create the new customer ID: ")
        first_name = input("The First Name of the customer: ")
        last_name = input("The Last Name of the customer: ")

        for x in self.customers:
            if x.id == id:
                print("Please try another ID")
                return

        new_customer = Customer(id, first_name, last_name)
        self.customers.append(new_customer)
        self.save_to_customer()
        print("New customer created")


        
        
        
