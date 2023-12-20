import sqlalchemy as _sql
import sqlalchemy.orm as _orm

DATABASE_URL = "postgresql://alicia:password@127.0.0.1:5432/website_db"

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)