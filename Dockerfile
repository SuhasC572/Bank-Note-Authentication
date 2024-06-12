FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
# RUN apt-get update && apt-get install -y ca-certificates
COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# RUN apt-get update && apt-get install -y ca-certificates
# RUN pip install -r requirements.txt
CMD python main_copy.py