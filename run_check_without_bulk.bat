@echo off
call C:\Users\lupa\Desktop\Repositories\pytest-lupa\venv\Scripts\activate.bat
python -m pytest C:\Users\lupa\Desktop\Repositories\pytest-lupa\Test_run_every_day\test_check_orders_without_bulk_id.py
call deactivate


