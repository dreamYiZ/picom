import os
from datetime import datetime
import json

def write_to_log(data, file='run.log',n=""):
    # 检查文件是否存在
    if not os.path.exists(file):
        print(f"文件{file}不存在，将被创建。")

    with open(file, 'a', encoding='utf-8') as f:
        # 获取当前时间并格式化为字符串
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 在数据中添加时间戳
        data_with_time = {'time': now, 'data': data}
        # 将数据写入文件
        f.write(n+">>>" +json.dumps(data_with_time, indent=4, ensure_ascii=False))
        f.write('\n')
