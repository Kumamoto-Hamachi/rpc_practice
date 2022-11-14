# 参考: https://docs.docker.jp/engine/reference/builder.html
# 参考2:https://guldra-cranch.hatenablog.com/entry/2020/11/07/172749
# ベースイメージの指定
FROM python:3.10.8-bullseye

# コンテナの実行時に指定したネットワーク・ポートnetwork portをコンテナがリッスンするように
EXPOSE 1234

# RUN命令はDockerfileからImageを作成するときに実行される
RUN set -ex && \
    apt update && \
    apt upgrade -y && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    rm -rf /var/lib/apt/lists/*

# 環境変数 <キー> に対し、値を <値> として設定します。この値は、以降に続く構築ステージ中で、環境変数として保持されます(引用符はエスケープしなければ削除されます)
ENV PATH="/root/.local/bin":$PATH

# Dockerfile 内で以降に続く RUN 、 CMD 、 ENTRYPOINT 、 COPY 、 ADD 命令の処理時に（コマンドを実行する場所として）使う 作業ディレクトリworking directory を指定
WORKDIR /app

# COPY 追加元 追加先
COPY pyproject.toml /app/
COPY poetry.lock /app/

RUN poetry install

COPY . /app/

# CMD命令はDockerイメージからDockerコンテナを作成するときに実行される
WORKDIR /app/grpc
CMD poetry run python grpc_manager.py
