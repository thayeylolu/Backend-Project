"""create movie table

Revision ID: 6cee24ac1a59
Revises: ecd225d2fdc9
Create Date: 2021-03-07 21:16:45.425037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cee24ac1a59'
down_revision = 'ecd225d2fdc9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    'Movie',
    sa.Column('mid', sa.Integer, primary_key=True),
    sa.Column('title', sa.String(50), nullable=False),
    sa.Column('description', sa.Unicode(200)),
    sa.Column('rating', sa.Integer(5), nullable=False),
    sa.Column('cost', sa.Integer(5), nullable=False),
    sa.Column('replacement_cost', sa.Integer(5), default=True),
    sa.Column('past_return_charge', sa.Integer(5), default=True),
    sa.Column('is_rented',  sa.Boolean, default=True)
    )

def downgrade():
    pass
