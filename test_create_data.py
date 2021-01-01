from sys import exit
from argparse import ArgumentParser
from configs import configurations
from utils.filehandler import FilePreprocess
from CRD.functions import DataStoreCRD

parser = ArgumentParser()
parser.add_argument('--datastore', help='Enter The Absolute Path Of The Datastore.')
args = parser.parse_args()

if args.datastore:
    db_path = args.datastore
else:
    db_path = configurations.DEFAULT_DB_PATH

# Create a datastore directory.
directory_created = FilePreprocess(db_path).create_folder()
if not directory_created:
    print(f"Permission denied: Cannot Enter The Directory `{db_path}`.\n")
    exit(0)


json_data = {
    "abc": {
        "data1": "value1",
        "data2": "value2",
        "data3": "value3",
        "Time-To-Live": 5000,
    },
    "def": {
        "data1": "value1",
        "data2": "value2",
        "data3": "value3",
        "Time-To-Live": 50,
    },
    "ghi": {
        "data1": "value1",
        "data2": "value2",
        "data3": "value3",
        "data4": "value4",
    },
    "jkl": {
        "data1": "value1",
        "data2": "value2",
        "data3": "value3",
        "Time-To-Live": 250,
    }
}


################################
''' CREATING DATA IN DATASTORE '''
_valid_data, message = DataStoreCRD().check_create_data(json_data, db_path)
print(message)
################################
