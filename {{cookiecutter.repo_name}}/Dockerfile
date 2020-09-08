# Dockerfile for {{ cookiecutter.project_name }}. Build it using:
#
#     $ docker build -t {{ cookiecutter.repo_name }} .
#
# You can then run it as a container:
#
#     $ docker run --rm {{ cookiecutter.repo_name }}

FROM python:3.8.5-slim

# Install Python dependencies with pip
COPY requirements.txt .
RUN python -m pip install -r requirements.txt --no-cache-dir --disable-pip-version-check

# Create working directory
WORKDIR /{{ cookiecutter.repo_name }}

# Install {{ cookiecutter.repo_name }}
COPY MANIFEST.in setup.cfg setup.py ./
COPY {{ cookiecutter.repo_name }} ./{{ cookiecutter.repo_name }}
RUN python -m pip install -e . --no-cache-dir --disable-pip-version-check

# The container runs this commands, options can be set as environment variables
ENV {{ cookiecutter.exe_name|upper }}_PIPELINE={{cookiecutter.default_pipeline}}
ENV {{ cookiecutter.exe_name|upper }}_OPTIONS=
CMD {{ cookiecutter.exe_name }} ${{ cookiecutter.exe_name|upper }}_PIPELINE ${{ cookiecutter.exe_name|upper }}_OPTIONS
