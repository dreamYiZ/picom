# 调用
curl -X POST -H "Content-Type: application/json" -d '{"message": "你好"}' http://127.0.0.1:5000/api

curl -X POST -H "Content-Type: application/json" -d '{"message": "小猪同学,音量调整到63"}' http://127.0.0.1:5000/api


# 安装

## 需要预装ollama


# 项目说明

    根据输入prompt，调用ollama中的模型，然后返回指令，
    根据指令，修改config_primary.ini文件
    利用了本地模型响应对话来执行指令
