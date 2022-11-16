# -*- coding: utf-8 -*-
"""Nested_JSON_flatten_by_spark.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uo8WBm3MadJ6tllKarxQR21LmBO7Pdkm
"""

# Commented out IPython magic to ensure Python compatibility.
# %fs
ls /mnt/tf-abfss/bronze/indian_railways

from pyspark.sql.functions import explode

df = spark.read.option("multiline","true").json("/mnt/tf-abfss/bronze/indian_railways/stations.json")
df.printSchema()

df0 = df.select(explode("features"))
display(df0)

df1 = df0.select("col.*")
display(df1)

df2 = df1.select("geometry.*", "properties.*")
display(df2)

