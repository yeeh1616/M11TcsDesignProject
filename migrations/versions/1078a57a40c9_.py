"""empty message

Revision ID: 1078a57a40c9
Revises: 44c87365175f
Create Date: 2020-03-16 22:02:35.691563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1078a57a40c9'
down_revision = '44c87365175f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('module_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('star', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('owner_id')
    )
    op.create_table('course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('module', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('house',
    sa.Column('house_id', sa.Integer(), nullable=False),
    sa.Column('house_keeper', sa.Integer(), nullable=True),
    sa.Column('module', sa.Integer(), nullable=True),
    sa.Column('color', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('house_id')
    )
    op.create_table('house_keeper',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('module_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('manager',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('module',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('img', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('student',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('house_id', sa.Integer(), nullable=True),
    sa.Column('module_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uname', sa.String(length=80), nullable=True),
    sa.Column('password_hash', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('img', sa.String(length=80), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=False),
    sa.Column('confirmed_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('uname')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('student')
    op.drop_table('module')
    op.drop_table('manager')
    op.drop_table('house_keeper')
    op.drop_table('house')
    op.drop_table('course')
    op.drop_table('comment')
    # ### end Alembic commands ###
