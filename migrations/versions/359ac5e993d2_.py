"""empty message

Revision ID: 359ac5e993d2
Revises: 1c3e46b756c8
Create Date: 2020-01-09 16:08:08.211592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '359ac5e993d2'
down_revision = '1c3e46b756c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('book_ibfk_1', 'book', type_='foreignkey')
    op.create_foreign_key(None, 'book', 'publisher', ['publisher_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'book', type_='foreignkey')
    op.create_foreign_key('book_ibfk_1', 'book', 'publisher', ['publisher_id'], ['id'])
    # ### end Alembic commands ###
