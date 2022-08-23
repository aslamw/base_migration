"""primeira

Revision ID: db71548199cc
Revises: 
Create Date: 2022-08-22 22:22:03.641643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db71548199cc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'pessoa',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=50), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('pessoa')
