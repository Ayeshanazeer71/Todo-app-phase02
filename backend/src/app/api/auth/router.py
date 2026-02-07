from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from app.api.deps import get_db
from app.models.user import User, UserCreate, Token
from app.services.auth import authenticate_user, create_access_token, get_password_hash
from datetime import timedelta
from app.core.config import settings

router = APIRouter()

@router.post("/signup", response_model=Token)
def signup(user_in: UserCreate, db: Session = Depends(get_db)):
    user = db.exec(select(User).where(User.username == user_in.username)).first()
    if user:
        raise HTTPException(status_code=400, detail="Username already registered")

    db_user = User(
        username=user_in.username,
        hashed_password=get_password_hash(user_in.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    access_token = create_access_token(data={"sub": str(db_user.username)})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.exec(select(User).where(User.username == form_data.username)).first()
    from app.services.auth import verify_password
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": str(user.username)})
    return {"access_token": access_token, "token_type": "bearer"}
