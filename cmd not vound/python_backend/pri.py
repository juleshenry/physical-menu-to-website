from datetime import datetime as dt


def nt(*a, **t):
    pre = ">>>" or f"[{str(dt.utcnow())}]:"
    print(pre, *a, **t)
