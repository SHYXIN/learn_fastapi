import base64

# 用户名和密码
username = 'wangxin'
password = 'wangxin'

# 构建 "username:password"
credentials = f"{username}:{password}"

# 进行base64编码
credentials_base64 = base64.b64encode(credentials.encode()).decode()

# 构建 Authorization 头部
authorization_header = f"Basic {credentials_base64}"

print(authorization_header)
# Basic bWVzZWNyZXQ=

#
import base64

# 原始数据
original_data = b"Hello, this is a secret message."

# Base64 编码
encoded_data = base64.b64encode(original_data)
print("Encoded:", encoded_data)

# Base64 解码
decoded_data = base64.b64decode(encoded_data)
print("Decoded:", decoded_data.decode())


original_data = b"Hello, this is a secret message."


# f-string  填充 对齐 宽度 格式
for byte in original_data:
    print(f"byte:{byte:^8d}\tchr:{chr(byte):^10s}\tbin:{byte:0>16b}")
for byte in credentials.encode():
    print(f"byte:{byte:^8d}\tchr:{chr(byte):^10s}\tbin:{byte:0>16b}")

s = f"{byte:0>16b}"
print(s)