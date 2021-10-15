基于centos7构建python3运行环境

# 构建命令

在Dockerfile文件目录下执行 
```shell script
docker build -t docker-python-flask:v1 .
docker images
docker run -d --name docker-python-flask-v1 -p 8888:8888 docker-python-flask:v1
docker exec -it docker-python-flask-v1 /bin/bash
```
```shell script
docker run -it --name docker-python-flask-v1 -p 8888:8888 docker-python-flask:v1 /bin/bash
```

# 查看镜像
```shell script
docker images
REPOSITORY                                  TAG                                                     IMAGE ID       CREATED              SIZE
python-centos                               3.8                                                     bcf41da40b30   About a minute ago   1.26GB
```

# 容器启动命令: 
```shell script
docker run -itd --name python --restart always --privileged=true -v /root/dockers/python:/root/python -v /root/dockers/python/cron:/var/spool/cron python-centos:3.8 /usr/sbin/init
```
```shell script
docker run -itd --name python --restart always --privileged=true python-centos:3.8 /usr/sbin/init

```
# 进入容器
```shell script
docker exec -it python /bin/bash
```

