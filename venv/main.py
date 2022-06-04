import awswrangler as wr
import pandas as pd
import boto3
from filemanager import filemanager
from datahandler import datahandler

# create a dataframe
print("Create Data Frame")
df1 = pd.DataFrame({
    "id": [1, 2,3,4],
    "email":["a@gmail.com","b@gmail.com","c@gmail.com","d@gmail.com"],
    "firstname": ["Kenath", "Tim","Kate","Berry"],
    "lastname":["Perera","Andrew","Smith","Allan"]

})

df2 = pd.DataFrame({
    "id": [5,6,7],
    "email":["e@gmail.com","f@gmail.com","a@gmail.com"],
    "firstname": ["Robin","Kate","Kenath"],
    "lastname":["Griggs","Lewis","Perera"]

})

frames = [df1, df2]
concatResult = pd.concat(frames)

# create file manager object
file_manager = filemanager()
# delete exist csv files
file_manager.deleteFile()
print("Delete exist CSV Files")

# write to csv
try:
    file_manager.writeFile(concatResult, 'file3.csv')
    print("Write to CSV")
except ValueError:
    print("check dataframe array size")
except:
    print("An exception occurred")


#read from CSV
try:
    result = file_manager.readFile('file3.csv')
    print("Read From CSV")
except:
    print("An exception occurred")


# Configure boto session to find dynamodb session
# boto3 used aws configure details from AWS CLI Configuration
boto3.setup_default_session(region_name="us-east-1")

# add= key is new
# update = key is exist
# write to a dynamo db using data frame
dynamodb_client = boto3.client('dynamodb')
try:
    wr.dynamodb.put_df(df=result, table_name="pandaTable")
    print("Write to DynamoDB")
except dynamodb_client.exceptions.ResourceNotFoundException:
    print("No database found")
except:
    print("An exception occurred")


#################
# print("DynamoDB put_items called")
#     with table.batch_writer() as batch:
#     for i, row in df.iterrows():
#         batch.put_item(Item=row.to_dict())
#     print("DynamoDB put_items completed")
################

#Read from Dynamo DB

# create dynamodb resource object and here dynamodb is resource name
client = boto3.resource('dynamodb')

# this will search for dynamoDB table
table = client.Table("pandaTable")
resp = table.scan()
print("Read From DynamoDB")

decode_data_frame = pd.json_normalize(resp['Items'])
sort_data_frame = decode_data_frame.sort_values(by=['id'])
print("Sort by using id")
dh = datahandler()

#remove Dulicates
final_result = dh.removeDuplicates(sort_data_frame,'email')
print("Remove Duplicates by using email")
print(final_result)


#write to csv
file_manager.writeFile(final_result,'file4.csv')
print("Write to 2nd CSV File")

#read from CSV
csv4_data = file_manager.readFile('file4.csv')
print("Read from 2nd File")

print('*************************************')
print(csv4_data)
print('*************************************')



