from peewee import *

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
db = PostgresqlDatabase('palko', user='palko')


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class City(BaseModel):

    name = CharField()
    nearest_city = CharField()


class School(BaseModel):

    name = CharField()
    city = CharField()


class Applicant(BaseModel):

    applicant_code = CharField(default=None)
    first_name = CharField()
    last_name = CharField()
    year_of_birth = DateField()
    gender = CharField()
    adress = CharField()
    is_valued = BooleanField(default=None)
    accepted = BooleanField(default=None)


class Mentor(BaseModel):

    first_name = CharField()
    last_name = CharField()
    school_id = ForeignKeyField(School)







# class InterviewSlot(BaseModel):
