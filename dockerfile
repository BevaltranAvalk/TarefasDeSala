# Define a imagem base
FROM python:3.8
docker build -t Imagem_API

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do diretório atual para o diretório de trabalho
COPY . /app
COPY requirements.txt

# Instala as dependências
RUN pip install -r requirements.txt
RUN pip install flask
RUN pip freeze > requirements.txt

# Define o comando a ser executado quando o contêiner for iniciado
CMD ["python", "main.py"]
