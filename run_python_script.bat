@echo off
call C:\Users\lupa\Desktop\Repositories\pytest-lupa\venv\Scripts\activate.bat
python -m pytest C:\Users\lupa\Desktop\Repositories\pytest-lupa\Test_run_every_day\check_if_tiles_add_to_basket.py
call deactivate
