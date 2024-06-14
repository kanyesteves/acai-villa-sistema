from werkzeug.security import generate_password_hash, check_password_hash

class Libs:
    def set_password(self, senha):
        return generate_password_hash(senha)

    def check_password(self, old_senha, senha):
        return check_password_hash(old_senha, senha)