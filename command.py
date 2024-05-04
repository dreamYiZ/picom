import re
import json
import conf


def extract_brackets_content(text):
    pattern = r"\[(.*?)\]"
    matches = re.findall(pattern, text)
    return matches


def extract_first_brackets_content(text):
    pattern = r"\[(.*?)\]"
    match = re.search(pattern, text)
    return match.group(1) if match else None


# text = "['ok':true, msg:'好的，调低空调温度', command:'air_conditioner1.temperature', value:21]"
# print(extract_brackets_content(text))


def parse_to_dict(text):
    # 使用json.loads函数将字符串解析为字典
    dictionary = json.loads(text)
    return dictionary


# def parse_to_dict(text):
#     # 使用eval函数将字符串解析为字典
#     dictionary = eval(text)
#     return dictionary

# text = "{'ok':true, 'msg':'好的，调低空调温度', 'command':'air_conditioner1.temperature', 'value':21}"
# print(parse_to_dict(text))


def get_command_list():
    return """
    ['ok':true,'msg':'好的，调低空调温度', 'command':'air_conditioner1.temperature', 'value': 23],
    ['ok':true,'msg':'温度已经是最低了', 'command':'air_conditioner1.temperature', 'value': 16],
    ['ok':true,'msg':'温度已经是最低了', 'command':'', 'value': ''],
    ['ok':true,'msg':'好的，调高空调温度', 'command':'air_conditioner1.temperature', 'value': 27],
    ['ok':true,'msg':'提高音量', 'command':'music1.volume', 'value': 38],
    ['ok':true,'msg':'灯光已调暗', 'command':'brightness.brightness', 'value': 38],
    ['ok':true,'msg':'初始化配置', 'command':'recreate', 'value': ''],
"""


def exec(cmd, val):
    if cmd == 'recreate':
        conf.copy_config()
    
    else:
        conf.write_config_opt(cmd, val)
    pass
