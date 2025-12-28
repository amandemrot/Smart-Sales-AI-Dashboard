import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import dashboard
from pyspark.sql import SparkSession

# --- Spark bootstrap (Railway safe) ---
os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"
os.environ["SPARK_LOCAL_IP"] = "127.0.0.1"

spark = SparkSession.builder \
    .master("local[*]") \
    .config("spark.driver.memory", "512m") \
    .config("spark.executor.memory", "512m") \
    .config("spark.sql.shuffle.partitions", "4") \
    .config("spark.ui.enabled", "false") \
    .getOrCreate()

# --- FastAPI ---
app = FastAPI(title="Dashboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend + production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard.router)
