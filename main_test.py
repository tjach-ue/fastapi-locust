import ast

import pytest
from fastapi.testclient import TestClient
import json
from main import app


@pytest.fixture
def client():
    client = TestClient(app)
    return client


@pytest.fixture
def test_data():
    test_data = {
        1: {1},
        120: {1, 2, 3, 4, 5, 6, 40, 8, 10, 12, 15, 20, 120, 24, 60, 30},
        324758962386: {1, 2, 3, 22277, 6, 89989, 2429703, 9, 44554, 179978, 601479, 4859406, 66831, 269967, 1202958, 18,
                       7289109, 12028109718, 1804437, 2004684953, 27, 133662, 539934, 162, 54126493731, 14578218,
                       3608874, 200493, 809901, 4009369906, 54, 36084329154, 108252987462, 6014054859, 81, 324758962386,
                       1619802, 400986, 18042164577, 162379481193}
    }
    return test_data


def test_root_endpoint_with_get(client):
    resp = client.get("/")
    assert resp.status_code == 200
    msg = "Hello World"
    expected = {"message": msg}
    assert resp.json() == expected


def test_root_endpoint_only_get(client):
    resp = client.post("/")
    assert resp.status_code == 405
    assert resp.json() == {"detail": "Method Not Allowed"}


def test_factor1_endpoint_with_get(client, test_data):
    for test, expected in test_data.items():
        resp = client.get(f"/factor1/{test}")
        assert resp.status_code == 200
        assert ast.literal_eval(resp.json()['message']) == expected


def test_factor2_endpoint_with_get(client, test_data):
    for test, expected in test_data.items():
        resp = client.get(f"/factor2/{test}")
        assert resp.status_code == 200
        assert ast.literal_eval(resp.json()['message']) == expected


def test_factor3_endpoint_with_get(client, test_data):
    for test, expected in test_data.items():
        resp = client.get(f"/factor3/{test}")
        assert resp.status_code == 200
        assert ast.literal_eval(resp.json()['message']) == expected
