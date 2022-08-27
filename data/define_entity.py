from peewee import (
    AutoField, Model, TextField,
    CharField, ForeignKeyField
)


MAX_LENGTH, MID_LENGTH, SMALL_LENGTH = 255, 150, 100

# Database Entities


class Database(Model):
    class Meta:
        database = None


class Account(Database):
    id = AutoField(null=False)
    username = CharField(max_length=MID_LENGTH, null=False)
    email = CharField(max_length=MAX_LENGTH, null=False)
    passwd = CharField(max_length=MAX_LENGTH, null=False)
    mobile = CharField(max_length=SMALL_LENGTH, null=True)


class Notes(Database):
    id = AutoField(null=False)
    note = TextField(null=True)
    account_id = ForeignKeyField(model=Account, field=Account.id, null=False)


class Login(Database):
    id = AutoField(null=False)
    username = CharField(max_length=MID_LENGTH, null=True)
    email = CharField(max_length=MAX_LENGTH, null=True)
    account_id = ForeignKeyField(model=Account, field=Account.id, null=False)


class Password(Database):
    id = AutoField(null=False)
    password_1 = CharField(max_length=MAX_LENGTH, null=True)
    login_id = ForeignKeyField(model=Login, field=Login.id, null=False)
