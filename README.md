# HDU 网络自动登录

## 1. 安装环境

```SHELL
uv sync
playwright install
```

## 2. 输入账号和密码

1. 账号和密码输入到`.env.example`文件中。
2. 将`.env.example`文件改名为`.env`

## 3. 运行自动登录脚本

```SHELL
uv run main.py
```

运行成功后可以将`.env`文件删除，防止密码泄露。