"""create todos table

Revision ID: d9b3c6cc203a
Revises: 
Create Date: 2023-09-28 19:35:37.159139

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9b3c6cc203a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
        create table todos (
            id bigserial primary key,
            name text,
            completed boolean not null default false
        );
    """)


def downgrade():
    op.execute("drop table todos;")
