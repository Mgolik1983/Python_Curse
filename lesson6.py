from sqlalchemy import Column, INT, VARCHAR, DECIMAL, ForeignKey
from sqlalchemy.orm import DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    pk = Column('id', INT, primary_key=True)
    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i fro i in cls.__name__).strip('_')

class Category(Base):
    __tablename__ = 'category'
    name = Column(VARCHAR(64), nullable=False, unique=True)
class Product(Base):
    __tablename__ = 'product'
    name = Column(VARCHAR(128), nullable=False, unique=True)
    price = Column(DECIMAL(8, 2), nullable=False)
    category_id = Column(INT, ForeignKey('Category.id', ondelete='CASCADE'), nullable=False)