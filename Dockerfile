# DOCKERFILE MULTISTAGE BUILD:
# satage 1: baixa a imagem e instala as dependências necessárias para a aplicação
FROM python:slim-trixie AS build
# WORKDIR no build: boa prática. Não seria necessário neste projeto.
WORKDIR /app

COPY  requirements.txt .

# Atualiza pip/setuptools/wheel e instala dependências temporárias do sistema
RUN pip install --upgrade pip setuptools wheel \
 && apt-get update && apt-get install -y \
      build-essential \
      gcc \
      gfortran \
      libffi-dev \
      libpq-dev \
      pkg-config \
 && pip install --no-cache-dir -r requirements.txt \
 && apt-get purge -y --auto-remove \
      build-essential gcc gfortran libffi-dev libpq-dev pkg-config \
 && rm -rf /var/lib/apt/lists/*

# Copia o resto do projeto, incluindo setup.py e pacote
COPY . /app

# # Instala o pacote NewDashboard em modo editável
# RUN pip install --no-cache-dir -e .


# state 2: cria um container enxuto sem a ferramenta pip e inicia a aplicação
FROM python:slim-trixie AS runtime
WORKDIR /app

# instala a lib libpq necessária para psycopg2
RUN apt-get update && apt-get install -y libpq5 \
    && rm -rf /var/lib/apt/lists/*
    
# copia somente os pacotes instalados para dentro do container da imagem anterior
COPY --from=build /usr/local/lib/python3.14/site-packages /usr/local/lib/python3.14/site-packages
# copia somente a instalação dos pacotes streamlit que outros que são guradados em /usr/local/bin
COPY --from=build /usr/local/bin /usr/local/bin

# copia toda a pasta do projeto para dentro da imagem runtime
COPY --from=build /app /app

EXPOSE 8050

ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:8050", "app:server"]
