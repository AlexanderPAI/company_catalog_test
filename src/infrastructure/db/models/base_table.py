from sqlalchemy.ext.declarative import declarative_base


class PreBase:
    """PreBase"""


Base = declarative_base(cls=PreBase)
