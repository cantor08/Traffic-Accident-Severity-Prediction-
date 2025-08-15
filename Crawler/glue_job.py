mport sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, to_timestamp, hour, dayofweek

# 🚀 Glue job setup
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# STEP 1: Load raw data from your S3 bucket
df = spark.read.option("header", "true").csv("s3://raw-data-714/Raw Data/US_Accidents_March23.csv")

# STEP 2: Drop unnecessary columns (customized for accident data)
columns_to_drop = [
    "ID", "Source", "TMC", "End_Time", "Number", "Street", "Description",
    "Country", "Timezone", "Airport_Code", "Wind_Chill(F)", "Turning_Loop",
    "Nautical_Miles", "Precipitation(in)", "Civil_Twilight", "Sunrise_Sunset",
    "Nautical_Twilight", "Astronomical_Twilight", "Weather_Timestamp",
    "Zipcode", "County", "State"
]
df = df.drop(*columns_to_drop)

# STEP 3: Data type conversion and missing value handling
df = df.withColumn("Severity", col("Severity").cast("int"))
df = df.dropna(subset=["Severity", "Start_Time"])  # Ensure required fields exist

# Fill missing values with defaults
df = df.fillna({
    "Visibility(mi)": 10.0,
    "Wind_Speed(mph)": 0.0,
    "Weather_Condition": "Unknown",
    "City": "Unknown"
})

# STEP 4: Feature Engineering - add Hour and Day of Week
df = df.withColumn("Start_Time", to_timestamp("Start_Time"))
df = df.withColumn("Hour", hour("Start_Time"))
df = df.withColumn("DayOfWeek", dayofweek("Start_Time"))

# STEP 5: Save the cleaned dataset to a new S3 location in Parquet format
df.write.mode("overwrite").parquet("s3://raw-data-714/processed/accidents_cleaned/")

# inalize the job
job.commit()
