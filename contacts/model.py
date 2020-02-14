class Contact:
    def __init__(self, name, phone, email, addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr

    def to_string(self):
        return '이름 : {} \n 전화번호 : {} \n 주소 : {} \n 이메일 : {}'\
            .format(self.name, self.phone, self.email, self.addr)