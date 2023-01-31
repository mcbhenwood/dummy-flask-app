FROM python:3.9
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY web.sh ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY dummy ./dummy
CMD ["/usr/src/app/web.sh"]

EXPOSE 80
