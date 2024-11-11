@echo off
call C:\Users\lupa\Desktop\Repositories\pytest-lupa\venv\Scripts\activate.bat
python -m pytest C:\Users\lupa\Desktop\Repositories\pytest-lupa\Test_run_every_day\test_check_url_payment_v4_is_prod.py
call deactivate
