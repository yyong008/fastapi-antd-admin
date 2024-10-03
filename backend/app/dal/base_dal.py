def get_total(db, model):
  return db.query(model).count()

def get_list_by_offset_limit(db, model, offset, limit):
  return db.query(model).offset(offset).limit(limit).all()

def get_by_id(db, model, id):
  return db.query(model).filter(model.id == id).first()

def create(db, model, data):
  db_obj = model(**data)
  db.add(db_obj)
  db.commit()
  db.refresh(db_obj)
  return db_obj

def update_by_id(db, model, id, data):
  db.query(model).filter(model.id == id).update(data)
  db.commit()

def delete_by_id(db, model, id):
  db.query(model).filter(model.id == id).delete()
  db.commit()

def delete_by_ids(db, model, ids):
  db.query(model).filter(model.id.in_(ids)).delete()
  db.commit()
