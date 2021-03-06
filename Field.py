class Field(object):

    def __init__(self,name,colum_type,primary_key,default):
        self.name=name
        self.column_type = colum_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s,%s:%s>' % (self.__class__.__name__,self.column_type,self.name)

class StringField(Field):

    def __init__(self,name =None,primary_key =False , default =None,ddl='varchar(100))'):
        super().__init__(name,ddl,primary,default)

