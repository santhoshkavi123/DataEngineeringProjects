from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.window import Window
from pyspark.sql.types import (StructType, 
                                StructField, 
                                FloatType, 
                                IntegerType, 
                                StringType)


# S3 Location details
BUCKET = ""




# Load the required files from the s3 location
songs = spark.read.csv("../data/songs.csv", inferSchema = True, header = True)
users = spark.read.csv("../data/users.csv", inferSchema = True, header = True)
streams = spark.read.csv("../data/streams/", inferSchema = True, header = True)


print(f"Shape of the songs dataframe : {songs.count(), len(songs.columns)}")
print(f"Shape of the users dataframe : {users.count(), len(users.columns)}")
print(f"Shape of the streams dataframe : {streams.count(), len(streams.columns)}")



