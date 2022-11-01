from fastapi import FastAPI
from functools import reduce

app = FastAPI()


def factors_1(n: int) -> set:
    retset = set()
    for i in range(1, n + 1):
        if (n % i) == 0:
            print(i)
            retset.add(i)
    return retset


def factors_2(n: int) -> set:
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def factors_3(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1, step) if n % i == 0)))


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/factor1/{number}")
async def factor_1(number: int):
    return {"message": f"{factors_1(number)}"}


@app.get("/factor2/{number}")
async def factor_2(number: int):
    return {"message": f"{factors_2(number)}"}


@app.get("/factor3/{number}")
async def factor_3(number: int):
    return {"message": f"{factors_3(number)}"}
