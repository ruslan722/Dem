from peewee import Model, MySQLDatabase, AutoField, IntegerField, \
                    CharField, DateField, DateTimeField, FloatField, \
                    ForeignKeyField, BooleanField

db = MySQLDatabase('test', user='root', password="root", host='localhost', port=3306)

class BaseModel(Model):
    class Meta:
        database = db

# Человек как биологическое существо
class Human(BaseModel):
    id = AutoField()
    name = CharField()
    age = IntegerField()
    gender = CharField()
    birth_date = DateField()
    height = FloatField()
    weight = FloatField()

# Человек как социальное существо
class SocialHuman(BaseModel):
    id = AutoField()
    human = ForeignKeyField(Human, backref='social_humans') 
    social_status = CharField()
    occupation = CharField()
    education = CharField()
    marital_status = CharField()
    income = FloatField()
    address = CharField()
    phone_number = CharField()
    email = CharField()

# Социальные связи человека
class SocialConnection(BaseModel):
    id = AutoField() 
    social_human = ForeignKeyField(SocialHuman, backref='connections') 
    connection_type = CharField() 
    connected_human = ForeignKeyField(SocialHuman, backref='connected_to') 
    connection_date = DateTimeField()
    connection_strength = FloatField()
    notes = CharField(null=True)
    venom = FloatField(null=True)
    is_active = BooleanField(default=True)
    is_conflict = BooleanField(default=False)
    is_important = BooleanField(default=False)
    is_mentoring = BooleanField(default=False)
    is_family = BooleanField(default=False)
    is_friend = BooleanField(default=False)
    is_professional = BooleanField(default=False)
    is_romantic = BooleanField(default=False)
    is_acquaintance = BooleanField(default=False)
    is_colleague = BooleanField(default=False)

# Состояние здоровья человека
class HealthStatus(BaseModel):
    id = AutoField()
    social_human = ForeignKeyField(SocialHuman, backref='health_status')
    health_condition = CharField()
    chronic_conditions = CharField(null=True)
    allergies = CharField(null=True)
    medications = CharField(null=True)
    last_checkup_date = DateTimeField(null=True)
    notes = CharField(null=True)
    is_smoker = BooleanField(default=False)
    is_drinker = BooleanField(default=False)
    is_physically_active = BooleanField(default=False)
    is_mentally_active = BooleanField(default=False)
    is_under_stress = BooleanField(default=False)
    is_sleep_deprived = BooleanField(default=False)
    is_happy = BooleanField(default=False)
    is_anxious = BooleanField(default=False)
    is_depressed = BooleanField(default=False)
    is_burned_out = BooleanField(default=False)


db.connect()
db.create_tables([Human, SocialHuman, SocialConnection, HealthStatus], safe=True)
db.close()
