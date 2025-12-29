from fastapi.testclient import TestClient
from app.main import app
import io

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200


def test_upload_csv():
    csv_content = b"""timestamp,distance,speed,heart_rate
    0,0,6.0,100
    1,6,5.8,102
    """

    file = io.BytesIO(csv_content)
    response = client.post(
        "/upload",
        files={"file": ("test.csv", file, "text/csv")}
    )

    assert response.status_code == 200
    assert response.json()["status"] == "success"
