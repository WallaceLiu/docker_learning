用docker构建简单的python flask

# 构建命令
在Dockerfile文件目录下执行 
```shell script
docker build -t docker-python-flask:v1 .
```

# 查看镜像
```shell script
docker images
REPOSITORY                                  TAG                                                     IMAGE ID       CREATED         SIZE
docker-python-flask                         v1                                                      43100657ee4b   5 hours ago     173MB
......
```

# 启动容器，并进入shell模式
```shell script
docker run -it --name docker-python-flask-v1 -p 8888:8888 docker-python-flask:v1 /bin/bash
root@25d69dbf1d85:/app# ls
README.md  app.py  dockerfile  requirements.txt  run.sh  sktime-0.7.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
root@25d69dbf1d85:/app# chmod u+x run.sh
root@25d69dbf1d85:/app# ./run.sh
...
```
> -it 参数会进入shell模式
> 先不要用-d参数，进入docker，确定没有再用

在另一个终端：
```shell script
curl http://127.0.0.1:8888/api
```

# 进入容器
```shell script
docker exec -it docker-python-flask-v1 /bin/bash
root@25d69dbf1d85:/app#
```

# 后台运行
> docker rm -f 删除
```shell script
docker run -itd --name docker-python-flask-v1 -p 8888:8888 docker-python-flask:v1 /bin/bash
```

```shell script
docker run -itd --name python --restart always --privileged=true python-centos:3.8 /usr/sbin/init

```