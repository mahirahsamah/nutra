FROM python:3.11.2
WORKDIR /backend
COPY ./requirements.txt /backend/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt
COPY . /backend
CMD [ "python", "-m", "flask", "run" ]