# Define a imagem base
FROM python:3

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do diretório atual para o diretório de trabalho
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define o comando a ser executado quando o contêiner for iniciado
CMD ["python", "ArvoreBinaria.ipynb"]
CMD ["python", "BubbleSort.py"]
CMD ["python", "BuscaBinaria.py"]
CMD ["python", "MergeSort.py"]
CMD ["python", "quicksort.py"]