FROM ubuntu:20.04
RUN apt-get update && apt-get install -y rclone curl

# https://rclone.org/faq/#rclone-gives-x509-failed-to-load-system-roots-and-no-roots-provided-error
RUN mkdir -p /etc/ssl/certs/
RUN curl -o /etc/ssl/certs/ca-certificates.crt https://raw.githubusercontent.com/bagder/ca-bundle/master/ca-bundle.crt
