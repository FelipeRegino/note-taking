import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BASEDIR = os.path.abspath(os.path.dirname(__file__))

ENGINE = create_engine('sqlite:///' + os.path.join(BASEDIR, 'app.db'),
                       convert_unicode=True)
DB_SESSION = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=ENGINE))
Base = declarative_base()
Base.query = DB_SESSION.query_property()


def init_db():
    """Inicia banco de dados."""
    import app.models
    Base.metadata.create_all(bind=ENGINE)
