用docker构建简单的python flask

# 构建命令
在Dockerfile文件目录下执行 
```shell script
docker build -t docker-python-flask:v1 .
```

# 查看镜像
```shell script
docker imagesds
REPOSITORY                                  TAG                                                     IMAGE ID       CREATED         SIZE
docker-python-flask                         v1                                                      43100657ee4b   5 hours ago     173MB
......
```

# 启动容器
```shell script
docker run -tid --name docker-python-flask-v1 -p 8888:8888 docker-python-flask:v1 /bin/bash
```

# 启动日志
```shell script
docker logs 52a0f83ac43f58abe9b30fedb82be28fe8c3326fa1367e5f7231e83ea592ed35
```
> 没有任何错误信息，容器正常启动了

# 访问接口
```shell script
curl http://127.0.0.1:8888/api
```

# 进入容器
```shell script
docker exec -it docker-python-flask-v1 /bin/bash
root@52a0f83ac43f:/app# ls
README.md  app.py  dockerfile  requirements.txt  run.sh  sktime-0.7.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
root@52a0f83ac43f:/app#
```

# 停止
```shell script
docker stop 52a0f83ac43f58abe9b30fedb82be28fe8c3326fa1367e5f7231e83ea592ed35
```

# 删除
> docker rm -f 删除
```shell script
docker rm -f 52a0f83ac43f58abe9b30fedb82be28fe8c3326fa1367e5f7231e83ea592ed35
```
