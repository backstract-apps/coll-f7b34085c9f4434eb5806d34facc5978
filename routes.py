from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.delete('/user1/id')
async def delete_user1_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_user1_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/user2/id')
async def delete_user2_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_user2_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user2/id')
async def get_user2_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_user2_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user2/')
async def get_user2(db: Session = Depends(get_db)):
    try:
        return await service.get_user2(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user2/id/')
async def put_user2_id(id: int, created_at: Annotated[str, Query(max_length=100)], name: Annotated[str, Query(max_length=100)], username: Annotated[str, Query(max_length=100)], password: Annotated[str, Query(max_length=100)], email: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_user2_id(db, id, created_at, name, username, password, email)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/external/api')
async def post_external_api(raw_data: schemas.PostExternalApi, db: Session = Depends(get_db)):
    try:
        return await service.post_external_api(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user2/')
async def post_user2(id: int, created_at: Annotated[str, Query(max_length=100)], name: Annotated[str, Query(max_length=100)], username: Annotated[str, Query(max_length=100)], password: Annotated[str, Query(max_length=100)], email: str, db: Session = Depends(get_db)):
    try:
        return await service.post_user2(db, id, created_at, name, username, password, email)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/test')
async def post_test(raw_data: schemas.PostTest, db: Session = Depends(get_db)):
    try:
        return await service.post_test(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user1/id/')
async def put_user1_id(id: int, uaername: Annotated[str, Query(max_length=100)], name: Annotated[str, Query(max_length=100)], email: Annotated[str, Query(max_length=100)], password: Annotated[str, Query(max_length=100)], created_at: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_user1_id(db, id, uaername, name, email, password, created_at)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user1/id')
async def get_user1_id(id: str, db: Session = Depends(get_db)):
    try:
        return await service.get_user1_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user1/')
async def post_user1(id: int, uaername: Annotated[str, Query(max_length=100)], name: Annotated[str, Query(max_length=100)], email: Annotated[str, Query(max_length=100)], password: Annotated[str, Query(max_length=100)], created_at: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.post_user1(db, id, uaername, name, email, password, created_at)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user1/')
async def get_user1(pincode: str, db: Session = Depends(get_db)):
    try:
        return await service.get_user1(db, pincode)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

