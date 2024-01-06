
FROM mongo:latest

COPY mongo-init/mongod.conf /etc/mongod.conf

COPY mongo-init/start.sh /scripts/start.sh

RUN chmod +x /scripts/start.sh

CMD ["/scripts/start.sh"]