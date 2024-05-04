import requests
import json
import conf
import command

BASE_URL = "http://localhost:11434/api/"


def send_request(model, message):
    url = BASE_URL + "chat"
    data = {"model": model, "messages": [{"role": "user", "content": message}]}

    response = requests.post(url, data=json.dumps(data), stream=True)

    # 初始化一个空的字符串来存储响应的内容
    response_content = ""

    # 持续读取返回的数据流
    for line in response.iter_lines():
        if line:
            res_json = json.loads(line.decode("utf-8"))
            response_content += str(res_json["message"]["content"])
            if res_json["done"]:
                break

    # 返回响应的数据
    return response_content


def chat_basic(msg):
    return send_request("llama3", msg + "\n请用中文回答。不要用其他的语言。")


def chat_msg(msg):
    return send_request("llama3", msg)


def chat_command():
    pass


def chat_pi(msg):
    config = conf.read_config_1()
    config_range = conf.read_config_range_1()
    return chat_basic(
        "你是一个车机语音助手，你只回应以小猪同学开头的对话，如果对话信息不是以小猪同学开头，那么返回JSON为['ok':false, 'msg':null]，如果是小猪同学开头，则返回['ok':true, 'msg': xxx,'command': xxx, 'value': xxx]格式，其中xxx根据对话来生成，车机配置文件是："
        + json.dumps(config._sections)
        + "根据对话内容和配置文件，分析对话是否可以通过修改配置问价文件来满足用户需求，如果可以，则返回对应的命令和值。如用户说太热了，则返回['ok':true,'msg':'好的，调低空调温度', 'command':'air_conditioner1.temperature', 'value': xxx_1], 其中xxx_1等于config._sections中air_conditioner1.temperature的值减少3的数字值，"
        + "参考的命令有："
        + command.get_command_list()
        + "配置的范围参考:"
        + config_range + 
        "比如temperature=[16-30]，温度的最小值是16，不能再低了，最大值是30。"
        +
        "，所有的命令的value应该参考范围中的值，不能超过最大、最小值。如果超过了范围，就提示msg：已经达到最大、最小值了。"
        + "以下是对话内容："
        + msg,
    )


# def chat_pi_wash(msg):
#     return chat_msg(
#         "这是一些参考的命令:"
#         + command.get_command_list()
#         + "，根据对话信息，分析其中的命令，如果有别的信息，忽略掉，只返回其中的命令，如果就是命令，没有其他信息，那就返回命令。以下是对话信息:"
#         + msg
#     )
