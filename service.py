from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def delete_user1_id(db: Session, id: int):

    query = db.query(models.User1)
    query = query.filter(and_(models.User1.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        user1_deleted = record_to_delete.to_dict()
    else:
        user1_deleted = record_to_delete
    res = {
        "user1_deleted": user1_deleted,
    }
    return res


async def delete_user2_id(db: Session, id: int):

    query = db.query(models.User2)
    query = query.filter(and_(models.User2.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        user2_deleted = record_to_delete.to_dict()
    else:
        user2_deleted = record_to_delete
    res = {
        "user2_deleted": user2_deleted,
    }
    return res


async def get_user2_id(db: Session, id: int):

    query = db.query(models.User2)
    query = query.filter(and_(models.User2.id == id))

    user2_one = query.first()

    user2_one = (
        (user2_one.to_dict() if hasattr(user2_one, "to_dict") else vars(user2_one))
        if user2_one
        else user2_one
    )

    test = aliased(models.User2)
    query = db.query(models.User2, test)

    query = query.join(test, and_(models.User2.id == models.User2.id))

    dsgfhg = query.first()
    dsgfhg = (
        [
            {
                "dsgfhg_1": s1.to_dict() if hasattr(s1, "to_dict") else vars(s1),
                "dsgfhg_2": s2.to_dict() if hasattr(s2, "to_dict") else vars(s2),
            }
            for s1, s2 in dsgfhg
        ]
        if dsgfhg
        else dsgfhg
    )

    res = {
        "user2_one": user2_one,
        "dfsd": dsgfhg,
    }
    return res


async def get_user2(db: Session):

    query = db.query(models.User2)

    user2_all = query.all()
    user2_all = (
        [new_data.to_dict() for new_data in user2_all] if user2_all else user2_all
    )

    safdgdg = aliased(models.User1)
    query = db.query(models.User1, safdgdg)

    query = query.join(safdgdg, and_(models.User1.uaername != models.User1.uaername))

    fdsdg = query.first()
    fdsdg = (
        [
            {
                "fdsdg_1": s1.to_dict() if hasattr(s1, "to_dict") else vars(s1),
                "fdsdg_2": s2.to_dict() if hasattr(s2, "to_dict") else vars(s2),
            }
            for s1, s2 in fdsdg
        ]
        if fdsdg
        else fdsdg
    )

    res = {
        "user2_all": user2_all,
        "fsdgs": fdsdg,
    }
    return res


async def put_user2_id(
    db: Session,
    id: int,
    created_at: str,
    name: str,
    username: str,
    password: str,
    email: str,
):

    query = db.query(models.User2)
    query = query.filter(and_(models.User2.id == id))
    user2_edited_record = query.first()

    if user2_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "email": email,
            "password": password,
            "username": username,
            "created_at": created_at,
        }.items():
            setattr(user2_edited_record, key, value)

        db.commit()
        db.refresh(user2_edited_record)

        user2_edited_record = (
            user2_edited_record.to_dict()
            if hasattr(user2_edited_record, "to_dict")
            else vars(user2_edited_record)
        )

    mhghjgjgk = aliased(models.User1)
    query = db.query(models.User1, mhghjgjgk)

    query = query.join(mhghjgjgk, and_(models.User1.email == mhghjgjgk.email))

    jghfhghkjgjh = query.all()
    jghfhghkjgjh = (
        [
            {
                "jghfhghkjgjh_1": (
                    s1.to_dict() if hasattr(s1, "to_dict") else s1.__dict__
                ),
                "jghfhghkjgjh_2": (
                    s2.to_dict() if hasattr(s2, "to_dict") else s2.__dict__
                ),
            }
            for s1, s2 in jghfhghkjgjh
        ]
        if jghfhghkjgjh
        else jghfhghkjgjh
    )
    res = {
        "user2_edited_record": user2_edited_record,
        "fgdxhgh": jghfhghkjgjh,
    }
    return res


async def post_external_api(db: Session, raw_data: schemas.PostExternalApi):
    name: str = raw_data.name
    address: str = raw_data.address

    res = {}
    return res


async def post_user2(
    db: Session,
    id: int,
    created_at: str,
    name: str,
    username: str,
    password: str,
    email: str,
):

    record_to_be_added = {
        "id": id,
        "name": name,
        "email": email,
        "password": password,
        "username": username,
        "created_at": created_at,
    }
    new_user2 = models.User2(**record_to_be_added)
    db.add(new_user2)
    db.commit()
    db.refresh(new_user2)
    user2_inserted_record = new_user2.to_dict()

    res = {
        "user2_inserted_record": user2_inserted_record,
    }
    return res


async def post_test(db: Session, raw_data: schemas.PostTest):
    id: Any = raw_data.id
    name: Any = raw_data.name

    res = {}
    return res


async def put_user1_id(
    db: Session,
    id: int,
    uaername: str,
    name: str,
    email: str,
    password: str,
    created_at: str,
):

    query = db.query(models.User1)
    query = query.filter(and_(models.User1.id == id))
    user1_edited_record = query.first()

    if user1_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "email": email,
            "password": password,
            "uaername": uaername,
            "created_at": created_at,
        }.items():
            setattr(user1_edited_record, key, value)

        db.commit()
        db.refresh(user1_edited_record)

        user1_edited_record = (
            user1_edited_record.to_dict()
            if hasattr(user1_edited_record, "to_dict")
            else vars(user1_edited_record)
        )
    res = {
        "user1_edited_record": user1_edited_record,
    }
    return res


async def get_user1_id(db: Session, id: str):

    query = db.query(models.User1)
    query = query.filter(and_(models.User1.id == id))

    user1_one = query.first()

    user1_one = (
        (user1_one.to_dict() if hasattr(user1_one, "to_dict") else vars(user1_one))
        if user1_one
        else user1_one
    )

    userlist = aliased(models.User2)
    query = db.query(models.User1, userlist)

    query = query.join(userlist, and_(models.User1.id == userlist.id))

    record = query.all()
    record = (
        [
            {
                "record_1": s1.to_dict() if hasattr(s1, "to_dict") else s1.__dict__,
                "record_2": s2.to_dict() if hasattr(s2, "to_dict") else s2.__dict__,
            }
            for s1, s2 in record
        ]
        if record
        else record
    )
    res = {
        "user1_one": user1_one,
        "record": record,
    }
    return res


async def post_user1(
    db: Session,
    id: int,
    uaername: str,
    name: str,
    email: str,
    password: str,
    created_at: str,
):

    record_to_be_added = {
        "id": id,
        "name": name,
        "email": email,
        "password": password,
        "uaername": uaername,
        "created_at": created_at,
    }
    new_user1 = models.User1(**record_to_be_added)
    db.add(new_user1)
    db.commit()
    db.refresh(new_user1)
    user1_inserted_record = new_user1.to_dict()

    userlist = aliased(models.User2)
    query = db.query(models.User1, userlist)

    query = query.join(userlist, and_(models.User1.id == models.User2.id))

    records = query.first()
    records = (
        [
            {
                "records_1": s1.to_dict() if hasattr(s1, "to_dict") else vars(s1),
                "records_2": s2.to_dict() if hasattr(s2, "to_dict") else vars(s2),
            }
            for s1, s2 in records
        ]
        if records
        else records
    )

    headers = {}

    payload = {}
    apiResponse = requests.get(
        "https://api.postalpincode.in/pincode/201301",
        headers=headers,
        json=payload if "params" == "raw" else None,
    )
    dsgfhf = apiResponse.json() if "list" in ["dict", "list"] else apiResponse.text
    res = {
        "user1_inserted_record": user1_inserted_record,
        "records": records,
    }
    return res


async def get_user1(db: Session, pincode: str):

    query = db.query(models.User1)

    user1_all = query.all()
    user1_all = (
        [new_data.to_dict() for new_data in user1_all] if user1_all else user1_all
    )

    headers = {}

    payload = {}
    apiResponse = requests.get(
        "https://api.postalpincode.in/pincode/201301",
        headers=headers,
        json=payload if "params" == "raw" else None,
    )
    test123 = apiResponse.json() if "list" in ["dict", "list"] else apiResponse.text
    res = {
        "user1_all": test123,
    }
    return res
