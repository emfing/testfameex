import hmac


class JiaMi:
    def __init__(self, method, path, body):
        self.method = method
        self.path = path
        self.body = body

    def getHeader(self):  # 定义一个签名的函数
        # type: () -> object
        Access = "a6b695ab-aefc-0122-6dec-467347521dc5"
        Secret = "bc6dc9a8-9531-00e6-bb67-45509962da28"
        message = str(1231231230) + str.upper(self.method) + self.path + str(self.body)
        mac = hmac.new(bytes(Secret, encoding='utf8'), bytes(message, encoding='utf8'), digestmod='sha256').digest()
        hex_data = bytes(mac).hex()
        headers = {
            "AccessKey": Access,
            "SignatureMethod": "HmacSHA256",
            "SignatureVersion": "v1.0",
            "Timestamp": "1231231230",
            "Signature": hex_data,
            "Content-Type":"application/json"
        }
        return headers

