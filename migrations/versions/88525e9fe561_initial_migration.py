"""Initial Migration

Revision ID: 88525e9fe561
Revises: 58b0a0496c41
Create Date: 2019-07-08 09:29:12.295920

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '88525e9fe561'
down_revision = '58b0a0496c41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bloggy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('upvotes', sa.Integer(), nullable=True),
    sa.Column('downvotes', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('blogs')
    op.drop_constraint('comments_blog_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'bloggy', ['blog_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_blog_id_fkey', 'comments', 'blogs', ['blog_id'], ['id'])
    op.create_table('blogs',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('upvotes', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('downvotes', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='blogs_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='blogs_pkey')
    )
    op.drop_table('bloggy')
    # ### end Alembic commands ###
