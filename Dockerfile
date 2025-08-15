FROM debian:stable-slim

COPY go-srv /bin/go-srv

ENV PORT=8991

CMD ["/bin/go-srv"]