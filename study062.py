from orm import Model,StringField ,IntegerField

class User(Model):
    __table__='users'

    id = IntegerField(primary_key=True)
    name = StringField()

user = User(id=123,name='username')
user.insert()
users = User.findAll()

