# movies-library

### 安装依赖
1. web.py(作为web服务器)
2. ImageMagick(生成缩略图)

### 使用
1. 运行 init_sqite.py 初始化数据库
2. 图片和视频放入 /static/source/ 下的相应位置
3. 运行 updateDB.py 处理图片和视频, 更新数据到数据库
4. 运行 server.py
5. 用浏览器访问(http://192.168.0.100:8080 的形式)

### 注意
1. 程序使用8080端口(web.py默认使用8080端口)
2. 这是一个被腰斩的项目 :(
