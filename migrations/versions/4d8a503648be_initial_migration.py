"""Initial Migration

Revision ID: 4d8a503648be
Revises: b694033152f4
Create Date: 2021-04-26 14:56:18.395534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d8a503648be'
down_revision = 'b694033152f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pitches_category'), 'pitches', ['category'], unique=False)
    op.create_index(op.f('ix_pitches_content'), 'pitches', ['content'], unique=False)
    op.create_index(op.f('ix_pitches_title'), 'pitches', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pitches_title'), table_name='pitches')
    op.drop_index(op.f('ix_pitches_content'), table_name='pitches')
    op.drop_index(op.f('ix_pitches_category'), table_name='pitches')
    op.drop_table('pitches')
    # ### end Alembic commands ###