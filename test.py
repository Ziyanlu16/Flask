from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer

s = Serializer('your-secret-key')  # 使用安全的秘钥

# 生成加密令牌并解码，设置过期时间为 30 分钟
token = s.dumps({'user_id': 1}, expires_in=1800).decode('utf-8')

# 打印令牌
print(token)
