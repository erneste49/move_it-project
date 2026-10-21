"""Allow pending relocation requests and save pickup/drop-off addresses.

Revision ID: e8a1d9c3f442
Revises: 49a98ed7f6ef
Create Date: 2026-10-18 12:15:00.000000
"""
from alembic import op
import sqlalchemy as sa


revision = 'e8a1d9c3f442'
down_revision = '49a98ed7f6ef'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('relocation', sa.Column('current_address', sa.String(length=255), nullable=True))
    op.add_column('relocation', sa.Column('new_address', sa.String(length=255), nullable=True))
    op.alter_column(
        'relocation',
        'driver_id',
        existing_type=sa.Integer(),
        existing_nullable=False,
        nullable=True,
    )


def downgrade():
    op.alter_column(
        'relocation',
        'driver_id',
        existing_type=sa.Integer(),
        existing_nullable=True,
        nullable=False,
    )
    op.drop_column('relocation', 'new_address')
    op.drop_column('relocation', 'current_address')
