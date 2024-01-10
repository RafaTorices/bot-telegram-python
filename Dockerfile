# Image docker python base for flask app
FROM python:3.10
# Workdir default for aplication
WORKDIR /src
RUN python -m pip install --upgrade pip
COPY src .
COPY requirements.txt .
RUN pip install -r requirements.txt
# Expose port for flask app
EXPOSE 80
# Set environment variables
ENV FLASK_APP=app.py
# Run flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
