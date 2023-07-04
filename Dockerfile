FROM python:3
RUN git clone https://github.com/PabloHerrera99/Ult_pract.git
WORKDIR /Ult_pract
RUN pip install -r requirements.txt
CMD ["python3", "-m", "unittest"]