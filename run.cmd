@echo off

:: this line is used to navigate the current working directory (important to setup relative import)
set SCRIPTDIR=%~dp0
set LIBDIR = %E:/ProgramData/Anaconda3/
set PYTHONPATH=%LIBDIR%

(
echo "Set script dir to %SCRIPTDIR% and python path to %LIBDIR%"
:: this line is used to set up environment from anaconda
call E:\ProgramData\Anaconda3\Scripts\activate.bat 
echo "Activate environment: "
echo "Running: python - m main.py"
python main.py %*
)

cmd /k