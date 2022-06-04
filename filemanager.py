import awswrangler as wr
import pandas as pd

#define bucket name
bucket = 'wran-bucket'

#define bucket path which is in your aws s3
basePath = f"s3://{bucket}/csv/"

class filemanager:
    def readFile(self,fileName):
        path = basePath + fileName
        return wr.s3.read_csv([path])
    def writeFile(self,dataFrame,fileName):
        path = basePath + fileName
        wr.s3.to_csv(dataFrame, path, index=False)
    def deleteFile(self):
        wr.s3.delete_objects(f"s3://{bucket}/")
