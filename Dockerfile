FROM python:3
RUN git clone https://github.com/PabloHerrera99/Ult_pract.git
WORKDIR /PabloHerrera99/Ult_pract.git
RUN pip install -r requirements.txt
CMD ["python3", "-m", "my_test"]