import os
import socket
import uuid

import httpx

HOST = os.getenv('TEST_HOST', '127.0.0.1')
PORT = int(os.getenv('TEST_PORT', '8000'))
BASE_URL = f'http://{HOST}:{PORT}'


def test_tcp_port_accepts_connections():
    with socket.create_connection((HOST, PORT), timeout=3):
        pass


def test_health_endpoint():
    response = httpx.get(f'{BASE_URL}/health', timeout=5)
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}


def test_write_and_read_round_trip():
    key = uuid.uuid4().hex
    value = 'qa-network-lab'
    with httpx.Client(timeout=5) as client:
        created = client.put(f'{BASE_URL}/items/{key}', json={'value': value})
        assert created.status_code == 200
        fetched = client.get(f'{BASE_URL}/items/{key}')
        assert fetched.status_code == 200
        assert fetched.json()['value'] == value


def test_missing_item_returns_404():
    response = httpx.get(f'{BASE_URL}/items/{uuid.uuid4().hex}', timeout=5)
    assert response.status_code == 404
