ARG tag=3.7-alpine
FROM registry.docker-cn.com/library/python:$tag

LABEL maintainer="Jintao Zhang <zhangjintao9020@gmail.com>"

WORKDIR /app
ARG requirements=requirements.txt

ADD . /app

RUN pip install --no-cache-dir -r $requirements -i https://mirrors.ustc.edu.cn/pypi/web/simple
CMD python -m httputil
