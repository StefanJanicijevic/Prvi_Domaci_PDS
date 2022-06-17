FROM python

WORKDIR /Client

COPY . /Client

RUN pip install requests

EXPOSE 8079

CMD ["python" , "client.py"]