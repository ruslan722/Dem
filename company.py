from peewee import Model, MySQLDatabase, AutoField, CharField, \
    DateTimeField, ForeignKeyField, BooleanField, DateField,  IntegerField

db =MySQLDatabase('two', user='root', password= 'root', host ='localhost', port=3306)

class BaseModel(Model):
    ''' Базовый класс '''
    class Meta:
        ''' Класс '''
        database = db

class Partners(BaseModel):
    ''' Партнеры '''
    id = AutoField()
    type = CharField()
    name_company = CharField()
    adress = CharField()
    TIN = IntegerField()
    Full_name = CharField()
    phone = CharField()
    email = CharField()
    logo = CharField()
    rating = IntegerField()
    sales_points = CharField()
    History = CharField()

class Menegers(BaseModel):
    ''' Менеджеры '''
    id = AutoField()
    seartch = CharField()
    name = CharField()
    password = CharField()
    rating = IntegerField()
    aplication = CharField(null = True)
    offers = CharField(null = True)

class Bid(BaseModel):
    ''' Заявки '''
    id = AutoField()
    price = IntegerField()
    data = DateField()
    quantity = IntegerField()
    data_insert = DateTimeField()

class Employeers(BaseModel):
    ''' Сотрудники '''
    id = AutoField()
    full_name = CharField()
    data_birth = DateField()
    passport = CharField()
    details = CharField()
    family = CharField()
    heath = CharField()

class Personnel(BaseModel):
    ''' Кадры'''
    id = AutoField()
    full_name = CharField()
    job_title = CharField()
    department = CharField()
    admission = CharField(null=True)
    admission_date = DateField()
    contacts = CharField()
    hirring = BooleanField(default=False)
    kvalification = CharField(null=True)

class Access(BaseModel):
    ''' Доступы '''
    id = AutoField()
    employeer_id = ForeignKeyField(Employeers, backref='accesses')
    full_name = CharField()
    number_cards = CharField()
    data = DateTimeField()
    access = CharField()
    result = CharField()
    location = CharField()

class Materials(BaseModel):
    ''' Материалы '''
    id = AutoField()
    type = CharField()
    name = CharField()
    suppliers = CharField()
    quantity = IntegerField()
    unit_of_measurement = CharField()
    description = CharField()
    image = CharField()
    price = IntegerField()
    quantity_in_stock = IntegerField()
    minimum_stock = IntegerField()
    history = CharField()

class Warehouse(BaseModel):
    ''' Склад '''
    id = AutoField()
    registration = CharField()
    rezerve = CharField()
    write_off = CharField()
    receipts = CharField()
    info = CharField()

class Suppliers(BaseModel):
    ''' Поставщики '''
    id = AutoField()
    name = CharField()
    TIN = IntegerField()
    history = CharField()

class Products(BaseModel):
    ''' Продукция'''
    id = AutoField()
    Article = CharField()
    type = CharField()
    name = CharField()
    description = CharField()
    image = CharField()
    min_price = IntegerField()
    size_packaging = CharField()
    weight_packaging = IntegerField()
    weight_no_packaging = IntegerField()
    sertificate = CharField()
    number_standard = CharField()
    history = CharField()
    data_insert = DateTimeField()
    cost_price = IntegerField()
    number_workshops = IntegerField()
    number_people = IntegerField()
    materials = CharField()

db.connect()
db.create_tables([Partners, Menegers, Bid, Employeers, Personnel, Access,
                   Materials, Warehouse, Suppliers, Products], safe=True)

db.close()
# End of company.py
