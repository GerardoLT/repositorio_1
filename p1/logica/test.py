from logica.moldes import usuarios as u


def create_user(nick_name,full_name):
    user=u.User(nick_name=nick_name,fullname=full_name)
    try:
     u.session.add(user)
     u.session.commit()
     return f"usuario {user.nick_name} guardado con exito"
    except Exception as error:
       u.session.rollback()
       raise Exception(error)
    