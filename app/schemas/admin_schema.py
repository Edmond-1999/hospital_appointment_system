from app.schemas.user_schema import UserCreate, UserRead, UserUpdate


class AdminCreate(UserCreate):
    pass


class AdminUpdate(UserUpdate):
    pass


class AdminRead(UserRead):
    pass
