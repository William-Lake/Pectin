import logging

from db.models import *


def main(args):
    
    # Just testing things out at the moment.
    
    # With this method you can pass in a database name from args so that previous progress can be continued.
    database.init(r'.\test.db')
    database.connect()
    
    # Can't run the create_db.sql script directly
    # (get an error re: one statement at a time or something like that,)
    # so this is the next best thing.
    # Creates the database tables.
    database.create_tables([
        Content,
        Question,
        Answer,
        AnswerContent,
        ObjectType,
        AttributeType,
        RelationshipType,
        Object,
        Attribute,
        Relationship
    ])
    
    # Testing out creating a record and saving it. It works.
    ot = ObjectType(description='desc',name='name')
    
    ot.save()
    
def gather_args():
    
    pass

if __name__ == '__main__':
    
    # The next three statements make it so all sql statments executed
    # by peewee are printed to the console.
    pw_logger = logging.getLogger('peewee')
    
    pw_logger.addHandler(logging.StreamHandler())
    
    pw_logger.setLevel(logging.DEBUG)
    
    main(gather_args())
    