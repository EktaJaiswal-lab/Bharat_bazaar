from fastapi import APIRouter, Depends
from typing import Dict, Any, List
from database import get_database

router = APIRouter()

@router.get("/dashboard", response_model=Dict[str, Any])
async def get_dashboard_stats(db = Depends(get_database)):
    # In a real scenario, this would aggregate data from the interactions and orders collections.
    # We provide mock data here for the UI dashboard to render charts.
    
    sales_data = [
        {"name": "Mon", "sales": 4000, "views": 2400},
        {"name": "Tue", "sales": 3000, "views": 1398},
        {"name": "Wed", "sales": 2000, "views": 9800},
        {"name": "Thu", "sales": 2780, "views": 3908},
        {"name": "Fri", "sales": 1890, "views": 4800},
        {"name": "Sat", "sales": 2390, "views": 3800},
        {"name": "Sun", "sales": 3490, "views": 4300},
    ]
    
    category_data = [
        {"name": "Electronics", "value": 400},
        {"name": "Footwear", "value": 300},
        {"name": "Clothing", "value": 300},
        {"name": "Gaming", "value": 200},
    ]
    
    return {
        "total_revenue": "$12,450.00",
        "total_users": "1,240",
        "conversion_rate": "3.2%",
        "sales_trend": sales_data,
        "category_distribution": category_data
    }
