
from logica.Models import usuarios as u

def create_user(nick_name, full_name):
    user = u.User(nick_name=nick_name, fullname=full_name)
    try:
        u.session.add(user)
        u.session.commit()
        return "sucessfull create user{user.nick_name}"
    except Exception as error:
        u.session.rollback()
        raise Exception(error)
    