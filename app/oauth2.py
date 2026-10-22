from base64 import encode
import jwt
from datetime import datetime, timedelta, timezone


SECRET_KEY ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES =30


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire =datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)
    return encode_jwt
