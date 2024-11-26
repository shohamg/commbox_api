REM Deactivate the virtual environment
 powershell deactivate


REM cd venv\lib\site-packages
cd venv\lib\site-packages

REM Zip the site-packages
powershell Compress-Archive -Path * -DestinationPath ..\..\..\commbox.zip

cd ..\..\..

REM Add files to the zip
powershell Compress-Archive -Path lambda_function.py -Update -DestinationPath commbox.zip

REM Activate the virtual environment
powershell venv\Scripts\activate
