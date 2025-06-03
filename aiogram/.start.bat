@echo off
setlocal

set VENV_DIR=venv

if not exist %VENV_DIR% (
	echo Virtual environment not found. Creating...
	python -m venv %VENV_DIR%
)

if exist requirements.txt (
	echo Checking if all dependencies from requirements.txt are installed...
	
	REM Get the list of installed packages
	venv\Scripts\pip freeze > installed_packages.txt

	REM Install missing packages
	for /f "tokens=*" %%i in (requirements.txt) do (
		findstr /i "%%i" installed_packages.txt >nul
		if errorlevel 1 (
			echo Installing %%i...
			venv\Scripts\pip install %%i
		) else (
			echo %%i is already installed.
		)
	)

	del installed_packages.txt
) else (
	echo requirements.txt not found.
)

cls
echo Running app\main.py...
venv\Scripts\python.exe app\main.py

endlocal
pause
.start.bat
