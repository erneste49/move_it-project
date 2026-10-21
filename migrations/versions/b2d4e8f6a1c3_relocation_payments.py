"""Track Paystack payments for relocation requests.

Revision ID: b2d4e8f6a1c3
Revises: 1f4b8c2d6a90
Create Date: 2026-10-18 13:30:00.000000
"""
from alembic import op
import sqlalchemy as sa


revision = 'b2d4e8f6a1c3'
down_revision = '1f4b8c2d6a90'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'relocation_payments',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('relocation_id', sa.Integer(), nullable=False),
        sa.Column('reference', sa.String(length=100), nullable=False),
        sa.Column('amount_kobo', sa.Integer(), nullable=False),
        sa.Column(
            'status',
            sa.Enum('pending', 'paid', 'failed'),
            nullable=False,
            server_default='pending',
        ),
        sa.Column('checkout_url', sa.String(length=512), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('paid_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['relocation_id'], ['relocation.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('reference'),
    )
    op.create_index(
        op.f('ix_relocation_payments_relocation_id'),
        'relocation_payments',
        ['relocation_id'],
        unique=False,
    )


def downgrade():
    op.drop_index(
        op.f('ix_relocation_payments_relocation_id'),
        table_name='relocation_payments',
    )
    op.drop_table('relocation_payments')
