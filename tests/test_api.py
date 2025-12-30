from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_csv_upload():
    file_path = "data/sample.csv"
    assert os.path.exists(file_path)

    with open(file_path, "rb") as f:
        response = client.post(
            "/upload/",
            files={"file": ("sample.csv", f, "text/csv")}
        )

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "success"
    assert body["rows"] > 0
    assert "columns" in body


def test_chat_endpoint():
    payload = {
        "metrics": {
            "avg_speed": 6.0,
            "max_speed": 6.5,
            "lap_consistency": 0.08,
            "avg_hr": 150,
            "hr_drift": 6,
            "efficiency": 0.03,
            "training_load": 120,
            "acwr": 1.1,
            "endurance_index": 0.03,
            "readiness_score": 78
        }
    }

    response = client.post("/chat/", json=payload)
    assert response.status_code == 200
    assert "answer" in response.json()
