from fastapi import APIRouter, HTTPException

import app.core.data_store as data_store  # 🔥 IMPORTANT

from app.kpi_engine import compute_all_kpis
from app.scoring import compute_race_readiness

router = APIRouter(prefix="/readiness", tags=["Readiness"])


@router.get("/")
def get_race_readiness():
    """
    Return final race readiness score and coach-friendly insight
    """

    # 🔥 1️⃣ Shared state check
    if data_store.latest_activity_df is None:
        raise HTTPException(
            status_code=400,
            detail="No activity data found. Please upload a file first."
        )

    # 2️⃣ Compute KPIs
    kpis = compute_all_kpis(data_store.latest_activity_df)

    # 3️⃣ Compute readiness score
    readiness = compute_race_readiness(kpis)

    # 4️⃣ Final response
    return {
        "status": "success",
        "readiness": readiness
    }
