# source
# https://github.com/absent1706/sqlalchemy-mixins/blob/master/sqlalchemy_mixins/timestamp.py
import datetime

import sqlalchemy as sa


class TimestampsMixin:
    """Mixin that define timestamp columns."""

    __abstract__ = True

    __created_at_name__ = "created_at"
    __updated_at_name__ = "updated_at"
    __datetime_func__ = datetime.datetime.utcnow

    created_at = sa.Column(
        __created_at_name__,
        sa.TIMESTAMP(timezone=False),
        default=__datetime_func__,
        nullable=False,
    )

    updated_at = sa.Column(
        __updated_at_name__,
        sa.TIMESTAMP(timezone=False),
        default=__datetime_func__,
        onupdate=__datetime_func__,
        nullable=False,
    )

    __all__ = ["TimestampsMixin"]
