import logging

from db.models import (
    database,
    AttributeType,
    Attribute,
    ObjectType,
    Object,
    RelationshipType,
    Relationship
)


def main(args):
    
    # Just testing things out at the moment.
    database.init(r'.\test.db')
    
    database.connect()
    
    # Can't run the create_db.sql script directly
    # (get an error re: one statement at a time or something like that,)
    # so this is the next best thing.
    # Creates the database tables.
    database.create_tables([
        ObjectType,
        AttributeType,
        RelationshipType,
        Object,
        Attribute,
        Relationship
    ])
    
    # This works.
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
    