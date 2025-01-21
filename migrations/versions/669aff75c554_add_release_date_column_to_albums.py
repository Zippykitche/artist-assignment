"""Add release_date column to albums

Revision ID: 669aff75c554
Revises: d1e618bd6325
Create Date: 2025-01-21 01:53:37.899930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '669aff75c554'
down_revision = 'd1e618bd6325'
branch_labels = None
depends_on = None

def upgrade():
    # This is the code to add the `release_date` column to the `albums` table
    op.add_column('albums', sa.Column('release_date', sa.Date(), nullable=True))


def downgrade():
    # This is the code to remove the `release_date` column from the `albums` table
    op.drop_column('albums', 'release_date')