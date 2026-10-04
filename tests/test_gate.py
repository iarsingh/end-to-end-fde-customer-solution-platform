from fastapi.testclient import TestClient
from fdeall.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'constraint': 'no egress', 'metric': 'two minutes', 'shadow_week': True, 'readout': True}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'constraint': 'no egress', 'metric': 'two minutes', 'shadow_week': True}).json()
    assert bad["passed"] is False
    assert "readout" in bad["failed"]
