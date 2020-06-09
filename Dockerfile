FROM python:3

WORKDIR /usr/src/app

# This installs our requirements from requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]