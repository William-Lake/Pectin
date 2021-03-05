import logging
from logging import StreamHandler,Formatter
import re

from db.models import *
import sqlparse


# Testing out the idea of formatting sql logs nicely.
class SqlFormattingLogger(StreamHandler):

    def __init__(self):

        super().__init__()

    def emit(self,record):

        msg = record.msg[0]

        args = record.msg[1]

        if args:

            # [:-1] takes off the closing paren
            query_parts = msg.split('?')[:-1]


            # Want this to look like a real sql statement,
            # so going to detect strings (non-numbers essentially)
            # and wrap them in single quotes.
            formatted_args = []

            for arg in args:

                if isinstance(arg,str):

                    formatted_args.append(f"'{arg}'")

                else:

                    formatted_args.append(str(arg))

            # Create arg string
            query_parts.append(', '.join(formatted_args))

            # Replace trailing paren
            query_parts.append(')')

            msg = ''.join(query_parts)

            args = []

        # Formatting the sql to look nice,
        # and putting space on either side of it.
        msg = sqlparse.format(msg, keyword_case='upper', reindent=True,indent_columns=True)

        record.msg = f'\n{msg}\n'

        super().emit(record)


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
    # ot = ObjectType(description='desc',name='name')
    
    # ot.save()

    # Unless the user is coming back to a previous session,
    # there should always be some initial questions.
    starting_question = 'At a high level, what does the application do?'

    content = Content(text=starting_question)

    content.save()

    question = Question(content_id = content.content_id)

    question.save()

def gather_args():
    
    pass

if __name__ == '__main__':
    
    # The next three statements make it so all sql statments executed
    # by peewee are printed to the console.
    pw_logger = logging.getLogger('peewee')
    
    # Testing out the idea of formatting sql logs nicely.
    pw_logger.addHandler(SqlFormattingLogger())

    pw_logger.setLevel(logging.DEBUG)
    
    main(gather_args())
    