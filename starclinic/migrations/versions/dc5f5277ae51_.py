"""empty message

Revision ID: dc5f5277ae51
Revises: 85b82026d5ae
Create Date: 2026-10-06 16:39:18.333813

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dc5f5277ae51'
down_revision = '85b82026d5ae'
branch_labels = None
depends_on = None


def upgrade():

    # Remove the old foreign key from users.role_id
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(
            'users_ibfk_1',
            type_='foreignkey'
        )

        batch_op.drop_column('role_id')

        # Add the new role column
        batch_op.add_column(
            sa.Column(
                'role',
                sa.String(length=20),
                nullable=False,
                server_default='patient'
            )
        )

    # Connect doctors to their login account
    with op.batch_alter_table('doctor', schema=None) as batch_op:

        batch_op.add_column(
            sa.Column(
                'user_id',
                sa.Integer(),
                nullable=True
            )
        )

        batch_op.create_foreign_key(
            'fk_doctor_user',
            'users',
            ['user_id'],
            ['user_id']
        )

        batch_op.create_unique_constraint(
            'uq_doctor_user_id',
            ['user_id']
        )

    # Connect patients to their login account
    with op.batch_alter_table('patient', schema=None) as batch_op:

        batch_op.add_column(
            sa.Column(
                'user_id',
                sa.Integer(),
                nullable=True
            )
        )

        batch_op.create_foreign_key(
            'fk_patient_user',
            'users',
            ['user_id'],
            ['user_id']
        )

        batch_op.create_unique_constraint(
            'uq_patient_user_id',
            ['user_id']
        )

def downgrade():

    # Remove patient -> users relationship
    with op.batch_alter_table('patient', schema=None) as batch_op:
        batch_op.drop_constraint(
            'fk_patient_user',
            type_='foreignkey'
        )

        batch_op.drop_constraint(
            'uq_patient_user_id',
            type_='unique'
        )

        batch_op.drop_column('user_id')

    # Remove doctor -> users relationship
    with op.batch_alter_table('doctor', schema=None) as batch_op:
        batch_op.drop_constraint(
            'fk_doctor_user',
            type_='foreignkey'
        )

        batch_op.drop_constraint(
            'uq_doctor_user_id',
            type_='unique'
        )

        batch_op.drop_column('user_id')

    # Remove the new role column
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('role')

        batch_op.add_column(
            sa.Column(
                'role_id',
                sa.Integer(),
                nullable=True
            )
        )

        batch_op.create_foreign_key(
            'users_ibfk_1',
            'roles',
            ['role_id'],
            ['role_id']
        )