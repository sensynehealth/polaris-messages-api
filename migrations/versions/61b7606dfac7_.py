"""empty message

Revision ID: 61b7606dfac7
Revises: be834046f941
Create Date: 2018-03-07 11:49:39.969617

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '61b7606dfac7'
down_revision = 'be834046f941'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    connection = op.get_bind()
    connection.execute("""
        insert into message_type (uuid, created, modified, value) 
        values ('Urgent_Callback', NOW(), NOW(), 5)
    """)
    connection.execute("""
        UPDATE message SET message_type_id = 5 WHERE message_type_id = 4
    """)
    connection.execute("""
        UPDATE message SET message_type_id = 4 WHERE message_type_id = 3
    """)
    connection.execute("""
        UPDATE message SET message_type_id = 3 WHERE message_type_id = 5
    """)
    connection.execute("""
        UPDATE message_type SET uuid = 'Feedback1' WHERE value = 3
    """)
    connection.execute("""
        UPDATE message_type SET uuid = 'Callback' WHERE value = 4
    """)
    connection.execute("""
        UPDATE message_type SET uuid = 'Feedback' WHERE value = 3
    """)
    # ### end Alembic commands ###


def downgrade():
    pass
