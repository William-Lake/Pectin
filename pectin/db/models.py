from peewee import *

database = SqliteDatabase('test.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Content(BaseModel):
    content_id = AutoField()
    text = TextField()

    class Meta:
        table_name = 'content'

class Question(BaseModel):
    question_id = AutoField()
    content = ForeignKeyField(column_name='content_id', field='content_id', model=Content)
    target_table = TextField(null=True)
    target_id = IntegerField(null=True)
    asked = IntegerField(constraints=[SQL("DEFAULT 0")])
    created = UnknownField(constraints=[SQL("DEFAULT current_timestamp")])  # timestamp

    class Meta:
        table_name = 'question'

class Answer(BaseModel):
    answer_id = AutoField()
    question = ForeignKeyField(column_name='question_id', field='question_id', model=Question)

    class Meta:
        table_name = 'answer'

class AnswerContent(BaseModel):
    answer_content_id = AutoField()
    answer = ForeignKeyField(column_name='answer_id', field='answer_id', model=Answer)
    content = ForeignKeyField(column_name='content_id', field='content_id', model=Content)

    class Meta:
        table_name = 'answer_content'

class AttributeType(BaseModel):
    attribute_type_id = AutoField()
    name = TextField()
    description = TextField()

    class Meta:
        table_name = 'attribute_type'

class Attribute(BaseModel):
    attribute_id = AutoField()
    attribute_type = ForeignKeyField(column_name='attribute_type_id', field='attribute_type_id', model=AttributeType)
    name = TextField()

    class Meta:
        table_name = 'attribute'

class ObjectType(BaseModel):
    object_type_id = AutoField()
    name = TextField()
    description = TextField()

    class Meta:
        table_name = 'object_type'

class Object(BaseModel):
    object_id = AutoField()
    object_type = ForeignKeyField(column_name='object_type_id', field='object_type_id', model=ObjectType)
    name = TextField()

    class Meta:
        table_name = 'object'

class RelationshipType(BaseModel):
    relationship_type_id = AutoField()
    object_type_id_1 = ForeignKeyField(column_name='object_type_id_1', field='object_type_id', model=ObjectType)
    object_type_id_2 = ForeignKeyField(backref='object_type_object_type_id_2_set', column_name='object_type_id_2', field='object_type_id', model=ObjectType)
    name = TextField()
    description = TextField()

    class Meta:
        table_name = 'relationship_type'

class Relationship(BaseModel):
    relationship_id = AutoField()
    relationship_type = ForeignKeyField(column_name='relationship_type_id', field='relationship_type_id', model=RelationshipType)
    object_id_1 = ForeignKeyField(column_name='object_id_1', field='object_id', model=Object)
    object_id_2 = ForeignKeyField(backref='object_object_id_2_set', column_name='object_id_2', field='object_id', model=Object)
    name = TextField()

    class Meta:
        table_name = 'relationship'

class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = 'sqlite_sequence'
        primary_key = False

