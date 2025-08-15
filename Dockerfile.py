FROM debian:stable-slim
RUN <<EOF
apt-get update
apt-get install -y python3
EOF
COPY main.py main.py
COPY books/ books/
CMD ["python3", "main.py"]