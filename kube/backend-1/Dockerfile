FROM alpine:3.9

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache
WORKDIR /app
COPY . /app
RUN pip3 install virtualenv
RUN virtualenv venv 
RUN source venv/bin/activate
RUN pip install flask flask-jsonpify flask-sqlalchemy flask-restful 
RUN pip install requests
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "app-1.py" ]
