FROM python:3.7.2
ENV IS_DOCKER 1
COPY . /home/app
WORKDIR /home/app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "run.py"]
EXPOSE 8000
