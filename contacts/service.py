from contacts.model import Contact

class Service:
    def __init__(self):
        pass
    @staticmethod
    def set_contact(name, phone, email, addr):
        return Contact(name, phone, email, addr)
    @staticmethod
    def get_contacts(params):
        contacts = []
        for i in params:
            contacts.append(i.to_string())
        return ' '.join(contacts)
    @staticmethod
    def del_contact(params, name):
        for i, t in enumerate(params):
            if t.name == name:
                del params[i]

