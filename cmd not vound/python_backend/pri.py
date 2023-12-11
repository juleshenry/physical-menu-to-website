from datetime import datetime as dt


def nt(*a, **t):
    print(f"[{str(dt.utcnow())}]:", *a, **t)
