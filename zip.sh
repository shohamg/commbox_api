deactivate
cd venv/lib/site-packages
zip -r ../../../../survey.zip .
cd ../../../..
zip -g survey.zip lambda_function.py
zip -g survey.zip upload_file.py
zip -g survey.zip config_utils.py
zip -g survey.zip config.ini
zip -g survey.zip logger.py
source venv/bin/activate
