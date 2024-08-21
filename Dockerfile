FROM python:3-alpine
RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-Camila-Choque
WORKDIR /ajedrez-2024-Camila-Choque
RUN pip install -r requirements.txt
CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python main.py"]