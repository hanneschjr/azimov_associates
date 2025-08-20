# DOCKERFILE MULTISTAGE BUILD:
# satage 1: baixa a imagem e instala as dependências necessárias para a aplicação
FROM python:slim-trixie AS build
# WORKDIR no build: boa prática. Não seria necessário neste projeto.
WORKDIR /app

COPY  requirements.txt .
# --no-cache-dir: o pip não armazena cache (~/.cache/pip). O pip baixa e instala diretamente os pacotes sem guardá-los
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do projeto, incluindo setup.py e pacote
COPY . /app

# # Instala o pacote NewDashboard em modo editável
# RUN pip install --no-cache-dir -e .


# state 2: cria um container enxuto sem a ferramenta pip e inicia a aplicação
FROM python:slim-trixie AS runtime
WORKDIR /app

# copia somente os pacotes instalados para dentro do container da imagem anterior
COPY --from=build /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
# copia somente a instalação dos pacotes streamlit que outros que são guradados em /usr/local/bin
COPY --from=build /usr/local/bin /usr/local/bin

# copia toda a pasta do projeto para dentro da imagem runtime
COPY --from=build /app /app

ENTRYPOINT [ "python", "index.py" ]
