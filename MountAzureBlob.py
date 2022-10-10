# Databricks notebook source
container_name = "databricks-administration"
storage_name = "adlsstoragecourse"
mount_point = "/mnt/custom_mount"

# COMMAND ----------

try:
    dbutils.fs.mount( source = "wasbs://" + container_name + "@" + storage_name + ".blob.core.windows.net",
                     mount_point = mount_point,
                     extra_configs = {"fs.azure.account.key." + storage_name + '.blob.core.windows.net': dbutils.secrets.get(scope="dbstoragescope", key="secredbadministrationcourse")}
                    )
    
except Exception as e:
    print("already mounted, please unmount using dbutils.fs.unmount")

# COMMAND ----------

# MAGIC %fs ls dbfs:/mnt/

# COMMAND ----------

if any([mount.mountPoint == mount_point for mount in dbutils.fs.mounts()]):
    dbutils.fs.unmount(mount_point)