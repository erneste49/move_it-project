"""Replace delivered relocation status with completed.

Revision ID: 1f4b8c2d6a90
Revises: e8a1d9c3f442
Create Date: 2026-10-18 12:50:00.000000
"""
from alembic import op
from sqlalchemy.dialects import mysql


revision = '1f4b8c2d6a90'
down_revision = 'e8a1d9c3f442'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'relocation',
        'status',
        existing_type=mysql.ENUM(
            'pending', 'quoted', 'confirmed', 'in_transit', 'delivered', 'cancelled'
        ),
        type_=mysql.ENUM(
            'pending', 'quoted', 'confirmed', 'in_transit', 'delivered', 'completed', 'cancelled'
        ),
        existing_nullable=False,
    )
    op.execute("UPDATE relocation SET status = 'completed' WHERE status = 'delivered'")
    op.alter_column(
        'relocation',
        'status',
        existing_type=mysql.ENUM(
            'pending', 'quoted', 'confirmed', 'in_transit', 'delivered', 'completed', 'cancelled'
        ),
        type_=mysql.ENUM(
            'pending', 'quoted', 'confirmed', 'in_transit', 'completed', 'cancelled'
        ),
        existing_nullable=False,
    )


def downgrade():
    op.alter_column(
        'relocation',
        'status',
        existing_type=mysql.ENUM(
            'pending', 'quoted', 'confirmed', 'in_transit', 'completed', 'cancelled'
        ),
        type_=mysql.ENUM(
            'pending', 'quoted', 'confirmed', 'in_transit', 'completed', 'delivered', 'cancelled'
        ),
        existing_nullable=False,
    )
    op.execute("UPDATE relocation SET status = 'delivered' WHERE status = 'completed'")
    op.alter_column(
        'relocation',
        'status',
        existing_type=mysql.ENUM(
            'pending', 'quoted', 'confirmed', 'in_transit', 'completed', 'delivered', 'cancelled'
        ),
        type_=mysql.ENUM(
            'pending', 'quoted', 'confirmed', 'in_transit', 'delivered', 'cancelled'
        ),
        existing_nullable=False,
    )
