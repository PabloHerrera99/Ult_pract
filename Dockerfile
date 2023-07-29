FROM python:3
RUN git clone https://github.com/PabloHerrera99/Ult_pract.git
WORKDIR /Ult_pract
CMD ["python3", "my_test.py"]