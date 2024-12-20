FROM public.ecr.aws/lambda/python:3.11

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}
# COPY snf_utils.py ${LAMBDA_TASK_ROOT}
# COPY logger.py ${LAMBDA_TASK_ROOT}
# COPY config_utils.py ${LAMBDA_TASK_ROOT}
# COPY utils.py ${LAMBDA_TASK_ROOT}
# COPY config.ini ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.handler" ]