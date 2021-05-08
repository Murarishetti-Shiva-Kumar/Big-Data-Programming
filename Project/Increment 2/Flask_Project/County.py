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

df = spark.read.option("header",True).csv(r"E:\engg\Master\Big Data Programming\GitHub Repo\Big-Data-Programming\Project\Increment 2\Flask_Project\covid19vaccinesbycounty.csv")
df.createOrReplaceTempView("county")

query_1 = spark.sql("select * from county limit 5")
query_1.show()

query_2 = spark.sql("SELECT sum(pfizer_doses) as pfizer,sum(moderna_doses) as moderna,sum(jj_doses) as JJ, month(administered_date) as month from county group by month")
pd = query_2.toPandas()
pd.to_csv('Query2_2.csv', index=False)
pd.plot.pie(y="pfizer", labels=pd.month.tolist(), autopct='%1.2f%%',shadow=False, legend=False, fontsize=8)
plt.title("Pfizer distribution")
plt.axis('equal')
plt.tight_layout()
plt.show()
plt.savefig('graph1_1.png')

pd.plot.pie(y="moderna", labels=pd.month.tolist(), autopct='%1.2f%%',shadow=False, legend=False, fontsize=8)
plt.title("Moderna Distribution")
plt.axis('equal')
plt.tight_layout()
plt.show()
plt.savefig('graph1_2.png')

pd.plot.pie(y="JJ", labels=pd.month.tolist(), autopct='%1.2f%%',shadow=False, legend=False, fontsize=8)
plt.title("JJ Distribution")
plt.axis('equal')
plt.tight_layout()
plt.show()
plt.savefig('graph1_3.png')


query_3=spark.sql("SELECT max(pfizer_doses) as pfizer,max(moderna_doses) as moderna,max(jj_doses) as JJ, month(administered_date) as month from county where month(administered_date) in (1,2,3,4) group by month")
pd = query_3.toPandas()
pd.to_csv('Query2_3.csv', index=False)
fig,[ax1,ax2,ax3]=plt.subplots(nrows=3,ncols=1, figsize=(7,10))
ax1.plot(list(pd.month),pd.pfizer.tolist())

ax1.set(ylabel='PFizer')
ax2.plot(pd.month.tolist(),pd.moderna.tolist())
ax2.set(ylabel='Moderna')
ax3.plot(pd.month.tolist(),pd.JJ.tolist())
ax3.set(xlabel='Months')
ax3.set(ylabel='JJ');
fig.show()

query_4=spark.sql("select county,sum(fully_vaccinated) from county group  by county")
pd = query_4.toPandas()
pd.to_csv('Query2_4.csv', index=False)
query_4.show()

query_5=spark.sql("select county,sum(partially_vaccinated) from county group  by county")
pd = query_5.toPandas()
pd.to_csv('Query2_5.csv', index=False)
query_5.show()

query_6=spark.sql("select county,sum(partially_vaccinated), month(administered_date) from county where month(administered_date) in (1,2,3,4) group by county, month(administered_date) order by sum(partially_vaccinated) limit 5")
pd = query_6.toPandas()
pd.to_csv('Query2_6.csv', index=False)
query_6.show()
