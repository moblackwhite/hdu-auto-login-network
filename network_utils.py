import subprocess


def is_connected_to_internet(host="www.baidu.com", count=2):
    """
    通过 ping 指定主机来判断是否联网

    参数:
        host (str): 要 ping 的主机，默认为百度
        count (int): ping 的次数

    返回:
        bool: True 表示有网络，False 表示无网络
    """
    # 根据操作系统选择 ping 命令参数
    param = (
        "-n" if subprocess.os.name == "nt" else "-c"
    )  # Windows 用 -n，Linux/Mac 用 -c
    command = ["ping", param, str(count), host]

    try:
        # 执行 ping 命令，设置超时防止卡住
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10
        )
        # 如果返回码为 0，说明 ping 成功
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print("Ping 超时")
        return False
    except Exception as e:
        print(f"发生异常: {e}")
        return False
