# for _ in range(4): page.go_back()




























####################################################################
#page.py (page object model)
# from playwright.sync_api import Page
# import pytest
# import configparser
# config = configparser.ConfigParser()
# config.read('config.ini')
#
#
# class SearchPage:
#     search_term_input_selector = '#sb_form_q'
#     selector = "#finish"
#
#     def __init__(self, page: Page):
#         self.page = page
#
#     def navigate(self, site):
#         self.page.goto(config['GLOBAL'][site])
#         self.page.goto("http://the-internet.herokuapp.com/dynamic_loading/1")
#
#     def search(self):
#         self.page.get_by_role("button", name="Start").click()
#         self.page.get_by_role("heading", name="Hello World!").is_enabled()
#         self.page.wait_for_selector(self.selector, state="visible")


    # def test_new_tab(self, page):
    #     general_function = Generalfunction(page=page, context=page.context)
    #     general_function.navigate("google")
    #     general_function.open_new_tab_and_navigate("gmail")










#########################################################################

#test_page.py desktop
# @pytest.mark.usefixtures("payment_url_tiles_prod")
# def test_play(page):
#     searchclass = SearchPage(page)
#     searchclass.navigate('payment_url_books_prod')
#     searchclass.search()
#
#
#
# #test_page.py mobile
# @pytest.mark.usefixtures("payment_url_tiles_prod")
# def test_play_mobile(page_mobile):
#     searchclass = SearchPage(page_mobile)
#     searchclass.navigate('payment_url_books_prod')
#     searchclass.search()



# def test_new_tab(page):
#     general_function = Generalfunction(page=page, context=page.context)
#     general_function.navigate("google")
#     general_function.open_new_tab_and_navigate("gmail")






#############################################################
# import os
# import pyautogui
# import time
# import subprocess
#
# def git_and_update_monitor():
#     server = "146.148.2.80"
#     username = "lupa"
#     password = "A12bc28!"
#     remote_path = r"C:\Users\lupa\Desktop\powergit.ps1"
#
#     ps_command = f"""
#     $username = '{username}'
#     $password = ConvertTo-SecureString '{password}' -AsPlainText -Force
#     $cred = New-Object System.Management.Automation.PSCredential($username, $password)
#
#     $session = New-PSSession -ComputerName {server} -Credential $cred
#     Invoke-Command -Session $session -ScriptBlock {{ Start-Process "{remote_path}" }}
#     Remove-PSSession $session
#     """
#
#     # הרצת הפקודה
#     process = subprocess.Popen(["powershell.exe", ps_command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     stdout, stderr = process.communicate()
#
#     # הדפסת פלט אם יש
#     if stdout:
#         print(stdout.decode())
#     if stderr:
#         print(stderr.decode())
#
#
# git_and_update_monitor()






#URLS IN FIXTURES
# import configparser
# config = configparser.ConfigParser()
# config.read('config.ini')
# @pytest.fixture(scope="module")
# def payment_url_books_prod(request):
#     page = request.getfixturevalue('page' if 'page' in request.fixturenames else 'page_mobile')
#     page.goto(config['GLOBAL']['payment_url_books_prod'])
#
# @pytest.fixture(scope="module")
# def payment_url_books_test(request):
#     page = request.getfixturevalue('page' if 'page' in request.fixturenames else 'page_mobile')
#     page.goto(config['GLOBAL']['payment_url_books_test'])
#
# @pytest.fixture(scope="module")
# def payment_url_tiles_prod(request):
#     page = request.getfixturevalue('page' if 'page' in request.fixturenames else 'page_mobile')
#     page.goto(config['GLOBAL']['payment_url_tiles_prod'])
#
# @pytest.fixture(scope="module")
# def payment_url_tiles_test(request):
#     page = request.getfixturevalue('page' if 'page' in request.fixturenames else 'page_mobile')
#     page.goto(config['GLOBAL']['payment_url_tiles_test'])


#  run cmd from file
# import subprocess
# import os
#
# #run trace
# if os.path.exists("trace_.zip"):
#     subprocess.Popen("playwright show-trace trace_.zip", shell=True)
# if os.path.exists("trace_mobile.zip"):
#     subprocess.Popen("playwright show-trace trace_mobile.zip", shell=True)
#
#
# #run allure
# current_dir = os.path.dirname(os.path.realpath(__file__))
# allure_report_dir = os.path.join(current_dir, "allure-results")
# subprocess.run(f"allure serve {allure_report_dir}", check=True, shell=True, cwd=current_dir)
