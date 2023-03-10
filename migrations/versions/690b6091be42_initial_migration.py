"""initial migration.

Revision ID: 690b6091be42
Revises: 
Create Date: 2023-01-08 20:31:14.959477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '690b6091be42'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Customer',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=50), nullable=False),
    sa.Column('City', sa.String(length=40), nullable=False),
    sa.Column('TelephoneCountryCode', sa.Integer(), nullable=False),
    sa.Column('Telephone', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Customer')
    # ### end Alembic commands ###
