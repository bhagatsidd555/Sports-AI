from fastapi import APIRouter, HTTPException

from app.core.data_store import latest_activity_df
from app.kpi_engine import compute_all_kpis
from app.scoring import compute_race_readiness

router = APIRouter(prefix="/readiness", tags=["Readiness"])


@router.get("/")
def get_race_readiness():
    """
    Return final race readiness score and coach-friendly insight
    """

    # 1️⃣ Check if data is uploaded
    if latest_activity_df is None:
        raise HTTPException(
            status_code=400,
            detail="No activity data found. Please upload a file first."
        )

    # 2️⃣ Compute KPIs
    kpis = compute_all_kpis(latest_activity_df)

    # 3️⃣ Compute readiness score
    readiness = compute_race_readiness(kpis)

    # 4️⃣ Final response
    return {
        "status": "success",
        "readiness": readiness
    }
