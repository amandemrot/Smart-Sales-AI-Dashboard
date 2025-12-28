from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as _sum, month
from datetime import datetime
import os

class DataProcessor:
    def __init__(self):
        self.spark = SparkSession.builder.appName("DashboardData").getOrCreate()

        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        data_dir = os.path.join(base_dir, "data")

        self.sales = self.spark.read.csv(os.path.join(data_dir, "sales_dataset.csv"), header=True, inferSchema=True)

    def calculate_key_metrics(self):
        total = self.sales.agg(_sum("Weekly_Sales").alias("t")).collect()[0]["t"] or 0

        return {
            "totalRevenue": {"value": round(total, 2), "changeDescription": "+20.1% from last month"},
            "activeUsers": {"value": 1, "changeDescription": "+180.1% from last month"},
            "salesGrowth": {"value": 0, "changeDescription": "Compared to last quarter"}
        }

    def get_sales_history(self):
        rows = self.sales.groupBy(month("Date").alias("m")).agg(_sum("Weekly_Sales").alias("s")).collect()
        names = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}

        return [{"month": names[r["m"]], "sales": r["s"]} for r in rows]

    def calculate_sales_forecast(self):
        total = self.sales.agg(_sum("Weekly_Sales").alias("t")).collect()[0]["t"] or 0
        monthly_avg = total / 12

        today = datetime.today()
        data = []

        for i in range(1,7):
            val = monthly_avg * (1 + 0.08 * i)
            data.append({
                "date": today.strftime("%Y-%m-01"),
                "product": "Total Sales",
                "forecast": round(val,2),
                "lowerBound": round(val*0.95,2),
                "upperBound": round(val*1.05,2)
            })

        return data
