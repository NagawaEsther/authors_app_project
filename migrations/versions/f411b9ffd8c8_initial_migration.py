"""initial migration

Revision ID: f411b9ffd8c8
Revises: 32434691a333
Create Date: 2024-03-01 10:17:53.365160

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f411b9ffd8c8'
down_revision = '32434691a333'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('origin', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('companies')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('origin', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('description', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='companies_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('Companies')
    # ### end Alembic commands ###
