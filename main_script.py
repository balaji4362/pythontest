import unittest
import pdb
from lib import Controller
from testbed import controller

class TestUM(unittest.TestCase):

    def setUp(self):
        print('Connecting the controller')
        self.ctrl = Controller(browser="firefox",username = "admin" ,password = "Admin123")

    def test_create_a_wlan(self):
        print('Deleting the existing wlan')
        self.ctrl.delete_wlan()

        print('Create a open wlan')
        self.ctrl.create_open_wlan()

    def tearDown(self):
        print('Delete the configured wlan')
        self.ctrl.delete_wlan()

        print('disconnect to the wlan')
        self.ctrl.disconnect()


if __name__ == '__main__':
    unittest.main()
