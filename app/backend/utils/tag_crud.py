from sqlalchemy.orm import Session
from app.models.tags import Tag
from app.schema._tag import TagCreate


def get_tag(db: Session, tag_id: int):
    return db.query(Tag).filter(Tag.id == tag_id).first()


def create_tag(db: Session, tag: TagCreate):
    db_tag = Tag(name=tag.name)

    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def get_tags(db: Session):
    return db.query(Tag).all()


"""  
def update_tag(db: Session, tag_id: int):
    db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag
"""
