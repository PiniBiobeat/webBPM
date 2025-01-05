import subprocess
import os

#run trace
if os.path.exists("trace_.zip"):
    subprocess.Popen("playwright show-trace trace_.zip", shell=True)
if os.path.exists("trace_mobile.zip"):
    subprocess.Popen("playwright show-trace trace_mobile.zip", shell=True)


#run allure
current_dir = os.path.dirname(os.path.realpath(__file__))
allure_report_dir = os.path.join(current_dir, "Allure_reports")
subprocess.run(f"allure serve {allure_report_dir}", check=True, shell=True, cwd=current_dir)



