import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import spark as spark
from datetime import datetime
from io import BytesIO
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import *


spark = SparkSession.builder.appName("COVID Vaccination Data Analysis").getOrCreate()

df = spark.read.json(r"E:\engg\Master\Big Data Programming\GitHub Repo\Big-Data-Programming\Project\Increment 2\Flask_Project\tweetsdata.txt")
df.createOrReplaceTempView("tweets")
users = df.select("user.*").dropDuplicates(subset=['id'])
users.createOrReplaceTempView("user")
entities = df.select("entities.*")
entities.createOrReplaceTempView("entity")
retweeted = df.select("retweeted_status.*")
retweeted.createOrReplaceTempView("user_retweeted")


# Query1
# Query to fetch top 20 highest followers count of verified users
def get_query1():
    plt.clf()
    # os.remove("Query2.csv")
    # os.remove("graph2.png")
    query_1 = spark.sql(
        "select name, followers_count from user where name is not null and verified=='true' order by followers_count DESC LIMIT 5")
    pd = query_1.toPandas()
    pd.to_csv('Query1.csv', index=False)
    pd.plot.pie(y="followers_count", labels=pd.name.tolist(), autopct='%1.2f%%',shadow=False, legend=False, fontsize=8)
    plt.title("Followers Count of verified Users")
    plt.axis('equal')
    plt.tight_layout()
    # plt.show()
    plt.savefig('graph1.png')
    graph1 = BytesIO()
    plt.savefig(graph1)
    graph1.seek(0)
    return graph1

# Query3
# Query to fetch 20 most influential person based on retweeted count
def get_query3():
    plt.clf()
    # os.remove("Query3.csv")
    # os.remove("graph3.png")
    query_3 = spark.sql(
        "select  t.Name,t.Retweeted_Count from(select user.screen_name as Name,SUM(retweet_count) as Retweeted_Count, count(*) from user_retweeted where user.screen_name is not null group by Name ) t order by Retweeted_Count DESC LIMIT 20")
    pd = query_3.toPandas()
    pd.to_csv('Query3.csv', index=False)
    x = pd.Name.tolist()
    y = pd.Retweeted_Count.tolist()
    plt.stackplot(x, y)
    plt.title("Most Influential Person Based on Retweet")
    plt.xlabel('User Name')
    plt.ylabel('Retweeted count')
    plt.xticks(rotation=45, ha="right")
    # plt.axis('equal')
    plt.tight_layout()
    # plt.show()
    plt.savefig('graph3.png')
    graph3 = BytesIO()
    plt.savefig(graph3)
    graph3.seek(0)
    return graph3

# Query4
# Query to fetch top 20 trending hashtags
def get_query4():
    plt.clf()
    # os.remove("Query4.csv")
    # os.remove("graph4.png")
    query4 = spark.sql(
        "SELECT LOWER(hashtags.text) As Hashtags, COUNT(*) AS total_count FROM tweets LATERAL VIEW EXPLODE(entities.hashtags) AS hashtags GROUP BY LOWER(hashtags.text) ORDER BY total_count DESC LIMIT 20")
    pd = query4.toPandas()
    pd.to_csv('Query4.csv', index=False)
    plt.plot(pd.Hashtags.tolist(), pd.total_count.tolist())
    plt.xticks(rotation=45, ha="right")
    plt.title("Trending Hashtags")
    plt.xlabel('Hashtags')
    plt.ylabel('Count')
    # plt.axis('equal')
    plt.tight_layout()
    # plt.show()
    plt.savefig("graph4.png")
    graph4 = BytesIO()
    plt.savefig(graph4)
    graph4.seek(0)
    return graph4