# Environment Setup

1) Operating system: Ubuntu 18.04
2) Python: Python3.6 or higher
3) Install Python dependency packages: python3 -m pip install -r requirements.txt
4) Run app.py to run the backend server.
   i) To start datastore from default file location, run python3 app.py
   ii) To start datastore from user defined file location, run python3 app.py --datastore=<absolute_path_of_your_datastore>
   
 # Test Environment Setup
1) To test the Create operation of data in datastore, run python3 test_create_data.py for default datastore or run python3 test_create_data.py --datastore=<absolute_path_of_your_datastore> for custom datastore location.
2) To test the Read operation of data in datastore, run python3 test_read_data.py for default datastore or run python3 test_read_data.py --datastore=<absolute_path_of_your_datastore> for custom datastore location.
3) To test the Delete operation of data in datastore, run python3 test_delete_data.py for default datastore or run python3 test_delete_data.py --datastore=<absolute_path_of_your_datastore> for custom datastore location.
