from itsdangerous import URLSafeTimedSerializer
from key import salt
def encode(data):
    serializer=URLSafeTimedSerializer('Mani124@')#screte code
    return serializer.dumps(data,salt=salt)
def decode(data):
    serializer=URLSafeTimedSerializer('Mani124@')#screte code
    return serializer.loads(data,salt=salt)
