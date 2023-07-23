import unittest

from unittest.loader import makeSuite

from test_cases.failure_login_to_the_system import TestLoginPageFailure
from test_cases.framework import Test
from test_cases.language_change_on_main_page import  TestLanguageChangeOnMainPage
from test_cases.login_to_the_system import TestLoginPage
from test_cases.logout_from_the_system import TestLogoutPage
from test_cases.remind_password import TestRemindPassword
from test_cases.test_add_player import TestAddPlayer
def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginPageFailure))
   test_suite.addTest(makeSuite(Test))
   test_suite.addTest(makeSuite(TestLanguageChangeOnMainPage))
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestLogoutPage))
   test_suite.addTest(makeSuite(TestRemindPassword))
   test_suite.addTest(makeSuite(TestAddPlayer))

   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())