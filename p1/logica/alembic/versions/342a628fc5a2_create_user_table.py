"""create user table

Revision ID: 342a628fc5a2
Revises: 
Create Date: 2023-03-02 18:01:03.045860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '342a628fc5a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'User',
        sa.Column('id',sa.Integer,primary_key=True, autoincrement=True),
        sa.Column('nick_name',sa.String(50),nullable=False),
        sa.Column('fullname',sa.Unicode(200)),
    )
   


def downgrade() -> None:
    op.drop_table('account')
