"""create user table

Revision ID: 8a9d928fc069
Revises: 
Create Date: 2023-02-28 18:32:38.688753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a9d928fc069'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None: #crear todo
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nick_name', sa.String(50), nullable=False),
        sa.Column('fullname', sa.Unicode(200)),
    )


def downgrade() -> None: #Aqui se quita todo lo que no sea nesesario
    op.drop_table('account')
