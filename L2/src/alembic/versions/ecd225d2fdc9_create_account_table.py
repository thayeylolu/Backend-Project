"""create account table

Revision ID: ecd225d2fdc9
Revises: 
Create Date: 2021-03-05 23:44:33.770479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecd225d2fdc9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'User',
        sa.Column('uid', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('hashed_password', sa.String(30), nullable = False),
        sa.Column('is_active', sa.Boolean, default=True)
        
    )
    pass


def downgrade():
    pass
