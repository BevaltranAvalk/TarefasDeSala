# Define a imagem base
FROM python:3

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do diretório atual para o diretório de trabalho
COPY . /app

# Instala as dependências
RUN pip install -r requirements.txt
RUN pip freeze > requirements.txt

# Define o comando a ser executado quando o contêiner for iniciado
CMD ["python", "main.py"]
