"""First attempt

Revision ID: 5de90618e21b
Revises: 
Create Date: 2023-08-02 15:19:51.314677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5de90618e21b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('swimmers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], name=op.f('fk_swimmers_team_id_teams')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('times',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('swimmer_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('time', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], name=op.f('fk_times_event_id_events')),
    sa.ForeignKeyConstraint(['swimmer_id'], ['swimmers.id'], name=op.f('fk_times_swimmer_id_swimmers')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('times')
    op.drop_table('swimmers')
    op.drop_table('teams')
    op.drop_table('events')
    # ### end Alembic commands ###