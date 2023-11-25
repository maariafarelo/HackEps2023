FROM postgres:11.22-alpine3.18

USER postgres
ADD cfm.sql /docker-entrypoint-initdb.d/
ENTRYPOINT ["docker-entrypoint.sh"]
EXPOSE 5432
CMD ["postgres"]
