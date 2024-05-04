from flask import Flask, request
import chat
import conf
import pprint
from log import write_to_log
import command
from say import saying
import os

app = Flask(__name__)
pp = pprint.PrettyPrinter(indent=4)

def init():
    # 判断如果config.ini文件不存在，就执行copy_config
    if not os.path.exists('config.ini'):
        conf.copy_config()

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    result = chat.chat_pi(data["message"])
    print(result)
    write_to_log(result)
    config = conf.read_config_1()
    write_to_log(config._sections)

    command_1 = command.extract_first_brackets_content(result)

    write_to_log(command_1, n="111")

    command_1_n2 = "{" + command_1[0:].replace("'", '"') + "}"

    write_to_log(command_1_n2, n="222")
    command_2_dict = command.parse_to_dict(command_1_n2)
    # command_2 = command.parse_to_dict(command_1)

    write_to_log(command_2_dict, n="333")

    if command_2_dict["ok"]:
        saying(command_2_dict["msg"])
        if command_2_dict["command"]:
            command.exec(cmd=command_2_dict["command"], val=command_2_dict["value"])
            return {"status": "success", "ok": True,}
            

    return {"status": "success"}

if __name__ == "__main__":
    app.run(debug=True)
