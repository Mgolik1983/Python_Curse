from sqlalchemy import Column, INT, VARCHAR, DECIMAL, ForeignKey, BOOLEAN, \
    create_engine, select, update, delete, or_, and_
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker

class Base(DeclarativeBase):
    pk = Column('id', INT, primary_key=True)
    engine = create_engine('postgressql://belbank@localhost:5432/bank')
    session = sessionmaker(bind=engine)
   # @staticmethodACA
   # def create_session(func):
   #    def wrapper(*args, **kwargs):
   #       with Base.session() as


    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')

class Category(Base):
    __tablename__ = 'category'
    name = Column(VARCHAR(64), nullable=False, unique=True)
class Product(Base):
    __tablename__ = 'product'
    name = Column(VARCHAR(128), nullable=False, unique=True)
    price = Column(DECIMAL(8, 2), nullable=False)
    category_id = Column(INT, ForeignKey('Category.id', ondelete='CASCADE'), nullable=False)
    is_published = Column(BOOLEAN, default=False)



# with session() as s:
#    cat = Category(name='Coffee')
#    s.add(cat)
#    s.commit()
#    s.refresh(cat)
#    print(cat.pk, cat.name)
with session() as s:
    # cat = s.get(Category, 1)
    # print(cat.name, cat.pk)
    objs = s.scalars(
        select(Category)
        .order_by(Category.name.desc())
        .filter(Category.name.like('%ff%') > 0)
    )
    print(objs.all())

