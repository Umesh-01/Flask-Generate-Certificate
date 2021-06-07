"""empty message

Revision ID: 270cab5b71c1
Revises: 0d8437913e06
Create Date: 2021-06-07 09:29:43.794481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '270cab5b71c1'
down_revision = '0d8437913e06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sqlite_stat1')
    op.drop_table('sqlite_stat4')
    with op.batch_alter_table('certificate', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_email_sent', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('certificate', schema=None) as batch_op:
        batch_op.drop_column('is_email_sent')

    op.create_table('sqlite_stat4',
    sa.Column('tbl', sa.NullType(), nullable=True),
    sa.Column('idx', sa.NullType(), nullable=True),
    sa.Column('neq', sa.NullType(), nullable=True),
    sa.Column('nlt', sa.NullType(), nullable=True),
    sa.Column('ndlt', sa.NullType(), nullable=True),
    sa.Column('sample', sa.NullType(), nullable=True)
    )
    op.create_table('sqlite_stat1',
    sa.Column('tbl', sa.NullType(), nullable=True),
    sa.Column('idx', sa.NullType(), nullable=True),
    sa.Column('stat', sa.NullType(), nullable=True)
    )
    # ### end Alembic commands ###
