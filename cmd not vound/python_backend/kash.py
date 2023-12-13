import functools
import json
import os


def cereal(*a, **k):
    a = list(filter(lambda x: type(x) == int or type(x) == str or type(x) == float, a))
    return str({"a": json.dumps(a), "k": json.dumps(k)})


def kash(file_path):
    file_path = file_path + ".kash"

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*a, **k):
            try:
                with open(file_path, "r") as file:
                    cow = json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                cow = {}
            milk = cow.get(cere := cereal(*a, **k))
            if milk is None:
                result = func(*a, **k)
                cow[cere] = result
            with open(file_path, "w+") as file:
                json.dump(cow, file)
            return milk if milk is not None else result

        return wrapper

    return decorator


@kash("good")
def fib(*a, **k):
    for _ in range(1000):
        pass
    print("~~~!!!!!@@@@@((((*****))))````````" * 2)
    return f"F({cereal(*a,**k)})"


class A:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __serialize__(self):
        # Convert the object to a dictionary that can be serialized
        return {"image_paths": self.image_paths}

    @classmethod
    def __deserialize__(cls, data):
        # Create an instance of the class using the deserialized data
        return cls(**data)

    @kash("A-class")
    def fib(*a, **k):
        for _ in range(1000):
            pass
        print("~~~~~@@@@@@$$$$$(((()))))" * 8)
        return f"F({cereal(*a,**k)})"


# Basic ( Run these 1 @ a time, then notice...)
"""
@kash("good")
def fib(*a, **k):
    for _ in range(1000):
        pass
    print("~~~!!!!!@@@@@((((*****))))````````" * 2)
    return f"F({cereal(*a,**k)})"
print(f'>>{(etap:="step one")}<<', fib(1, 2, 3, "arg", key="key", kwarg=etap))
print(f'>>{(etap:="step one")}<<', fib(1, 2, 3, "arg", key="key", kwarg=etap))
print(f'>>{(etap:="step two")}<<', fib(1, 2, 3, "arg", key="key", kwarg=etap))
print(f'>>{(etap:="step two")}<<', fib(1, 2, 3, "arg", key="key", kwarg=etap))
print(f'>>{(etap:="step one")}<<', fib(1, 2, 3, "arg", key="key", kwarg=etap))
"""
if __name__ == "__main__":

    @kash("good")
    def fib(*a, **k):
        for _ in range(1000):
            pass
        print("~~~!!!!!@@@@@((((*****))))````````" * 2)
        return f"F({cereal(*a,**k)})"

    print(f'>>{(etap:="step one")}<<', fib(1, 2, 3, "arg", key="key", kwarg=etap))
    print(f'>>{(etap:="step one")}<<', fib(1, 2, 3, "arg", key="key", kwarg=etap))
    print(f'>>{(etap:="step two")}<<', fib(1, 2, 3, "arg", key="key", kwarg=etap))
    print(f'>>{(etap:="step two")}<<', fib(1, 2, 3, "arg", key="key", kwarg=etap))
    print(f'>>{(etap:="step one")}<<', fib(1, 2, 3, "arg", key="key", kwarg=etap))
    print("expected")
    print(
        """
~~~!!!!!@@@@@((((*****))))````````~~~!!!!!@@@@@((((*****))))````````
>>step one<< F({'a': '[1, 2, 3, "arg"]', 'k': '{"key": "key", "kwarg": "step one"}'})
>>step one<< F({'a': '[1, 2, 3, "arg"]', 'k': '{"key": "key", "kwarg": "step one"}'})
~~~!!!!!@@@@@((((*****))))````````~~~!!!!!@@@@@((((*****))))````````
>>step two<< F({'a': '[1, 2, 3, "arg"]', 'k': '{"key": "key", "kwarg": "step two"}'})
>>step two<< F({'a': '[1, 2, 3, "arg"]', 'k': '{"key": "key", "kwarg": "step two"}'})
>>step one<< F({'a': '[1, 2, 3, "arg"]', 'k': '{"key": "key", "kwarg": "step one"}'})
"""
    )
