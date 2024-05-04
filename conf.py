import configparser
import shutil



def read_config(file):
    config = configparser.ConfigParser()
    config.read(file)
    return config

def read_config_range(file):
    config = configparser.ConfigParser()
    config.read(file)
    return {section: dict(config.items(section)) for section in config.sections()}

def write_config(file, config_data):
    config = configparser.ConfigParser()
    config.read_dict(config_data)
    with open(file, 'w') as configfile:
        config.write(configfile)

def write_config_opt(option, value):
    # 分割选项为部分和键
    section, key = option.split('.')
    # 读取当前配置
    config_data = read_config('config.ini')
    # 更新指定的选项
    config_data[section][key] = str(value)
    # 写回配置
    write_config('config.ini', config_data)


def copy_config():
    # 复制config_primary.ini到config.ini
    shutil.copyfile('config_primary.ini', 'config.ini')

# 使用新函数
# copy_config()


# 使用新函数
# write_config_opt('air_conditioner1.temperature', 27)


def read_config_1():
    return read_config('config.ini')    


def read_config_range_1():
    with open('config_range.ini', 'r') as file:
        return file.read()

def read_config_range_2():
    return read_config_range('config_range.ini')  

