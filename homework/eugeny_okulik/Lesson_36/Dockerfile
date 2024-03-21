FROM python
ENV COOL_PORT 8080
ENV COOL_IP 0.0.0.0
ENV COOL_LOG logs
RUN mkdir logs
RUN mkdir /usr/share/cool-app/
RUN echo "Hello group ST4!" > /usr/share/cool-app/cool-text.txt
RUN git clone https://github.com/eugene-okulik/cool_web_app.git
CMD ["python3", "cool_web_app/run.py"]
#docker build -t eokulik/first-st4 .
#docker run --rm --name first-st4 -p 8080:8080 eokulik/first-st4