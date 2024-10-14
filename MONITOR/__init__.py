
import os
import pyautogui
import time



import subprocess


def git_and_update_monitor():
    server = "146.148.2.80"
    username = "lupa"
    password = "A12bc28!"
    remote_path = r"C:\Users\lupa\Desktop\powergit.ps1"

    ps_command = f"""
    $username = '{username}'
    $password = ConvertTo-SecureString '{password}' -AsPlainText -Force
    $cred = New-Object System.Management.Automation.PSCredential($username, $password)

    $session = New-PSSession -ComputerName {server} -Credential $cred
    Invoke-Command -Session $session -ScriptBlock {{ Start-Process "{remote_path}" }}
    Remove-PSSession $session
    """

    # הרצת הפקודה
    process = subprocess.Popen(["powershell.exe", ps_command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # הדפסת פלט אם יש
    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())


git_and_update_monitor()
