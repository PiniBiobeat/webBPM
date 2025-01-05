import subprocess
import os


current_dir = os.path.dirname(os.path.realpath(__file__))
allure_report_dir = os.path.join(current_dir, "Allure_reports")
subprocess.run(f"allure serve {allure_report_dir}", check=True, shell=True, cwd=current_dir)



if os.path.exists("trace_.zip"): subprocess.run("playwright show-trace trace_.zip")
if os.path.exists("trace_mobile.zip"): subprocess.run("playwright show-trace trace_mobile.zip")