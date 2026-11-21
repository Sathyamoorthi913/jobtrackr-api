from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models import Application, Status
from .schemas import ApplicationCreate, ApplicationUpdate, ApplicationOut

Base.metadata.create_all(bind=engine)
app = FastAPI(title="JobTrackr API")


def get_or_404(db: Session, app_id: int) -> Application:
    obj = db.get(Application, app_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Application not found")
    return obj


@app.get("/")
def home():
    return {"message": "JobTrackr API is running"}


@app.post("/applications", response_model=ApplicationOut, status_code=201)
def create_app(data: ApplicationCreate, db: Session = Depends(get_db)):
    obj = Application(**data.model_dump(exclude_none=True))
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@app.get("/applications", response_model=list[ApplicationOut])
def list_apps(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    status: Status | None = None,
    company: str | None = None,
    db: Session = Depends(get_db),
):
    q = select(Application)
    if status:
        q = q.where(Application.status == status)
    if company:
        q = q.where(Application.company.ilike(f"%{company}%"))
    return db.scalars(q.offset(skip).limit(limit)).all()


@app.get("/applications/{app_id}", response_model=ApplicationOut)
def get_app(app_id: int, db: Session = Depends(get_db)):
    return get_or_404(db, app_id)


@app.patch("/applications/{app_id}", response_model=ApplicationOut)
def update_app(app_id: int, data: ApplicationUpdate, db: Session = Depends(get_db)):
    obj = get_or_404(db, app_id)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj


@app.delete("/applications/{app_id}", status_code=204)
def delete_app(app_id: int, db: Session = Depends(get_db)):
    db.delete(get_or_404(db, app_id))
    db.commit()