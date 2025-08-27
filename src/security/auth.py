# security / auth file
from datetime import datetime, timedelta , timezone
from jose import JWTError, jwt
from passlib.context import CryptContext

# Secret & settings
SECRET_KEY = "424rwfsvfer3t267y8u91iokjndbcvcfet36y72u89iokwndbvgfrtge3y2u8iqoksmnbvfgetg3y72uiokqmsndcbfvgrte3yuwioqksmncbvgfrte3yu8w9iqoksmncbvfgrt4378u29i0oqlksmndbfvgrt3y2uiokwmdnbhfvgrt3y28u9iwksmdnbhfrvgt3y8u2i9oqksmndbfvgrt3y72u8i"   # put in .env later
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict):
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str) -> dict:
    """
    Decode a JWT access token and return the payload.
    Raises JWTError if token is invalid or expired.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        raise JWTError(f"Token is invalid or expired: {str(e)}")

