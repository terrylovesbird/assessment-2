import unittest
from modules.interface import Interface
from modules.customer import Customer
from modules.inventory import Inventory

class CustomerTestSuite(unittest.TestCase):
    def test_create_customer_instance_info(self):
        c1 = Customer(1, 'Tianlin', 'Cai')
        self.assertEqual(c1.first_name, 'Tianlin')

class InventoryTestSuite(unittest.TestCase):
    pass
    # def test_create_check_initial_balance(self):
    #     initial_balance = 500
    #     a = Account(1, initial_balance)
        
    #     self.assertEqual(a.get_balance(), initial_balance)

    # def test_withdraw_simple(self):
    #     initial_balance = 500
    #     a = Account(1, initial_balance)

    #     withdraw_amount = 100
    #     new_balance = a.withdraw(withdraw_amount)
        
    #     self.assertEqual(new_balance, initial_balance - withdraw_amount)

class InterfaceTestSuite(unittest.TestCase):
    pass
    # def test_create_check_initial_balance(self):
    #     initial_balance = 500
    #     a = Account(1, initial_balance)
        
    #     self.assertEqual(a.get_balance(), initial_balance)

if __name__ == "__main__":
    unittest.main()