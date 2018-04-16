
 Memory API Version 0.27

 This module plays as a mid-way communicator between the database and users
 To easily Read, Modify or Insert data.

 Written By: Ahmed Abdeldaim

  Depandacies:
 - Postgresql-v10.2
 - Python >= 3.5
 ```shell
 # Instal postgres
 $ sudo apt-get install postgres

 # Add the installed Folder to linux search PATH
 $ export PATH="/usr/lib/postgresql/9.5/bin:$PATH"

 # Create DBs in "/usr/local/var/postgres" .. This path is not essinitial, you can choose yours.
 $ initdb /home/omarovee/Documents/postgress

 # To start the server .. "/usr/local/var/postgres" replace it with your path
 $ pg_ctl -D /home/omarovee/Documents/postgress -l logfile start


 # Change Password of the postgres user
 $ sudo nano /etc/postgresql/9.5/main/pg_hba.conf

 1- Replace `local   all             postgres                                peer` to 'local   all             postgres                                trust'
 2- Save the file
 3- close the file
 4- restart server `sudo service postgresql restart`

 # In another terminal type
 $ sudo -su postgres
 $ psql
 # ALTER USER postgres with password 'your-password';

 # Press CTRL+D to return to th postgres user

 # create a DB
 $ createdb wattary

 # create a user(must be the same name of the DB)
 $ createuser --interactive

 # Return to the first terminal where the file `pg_hba.conf` is opened
 1- Replace `local   all             postgres                                trust` to 'local   all             postgres                                md5'
 2- Save the file
 3- close the file
 4- restart server `sudo service postgresql restart`
 5- Close this terminal

 # Return to the 2nd terminal
 $ psql
 # ALTER USER wattary with password 'your-password';
 # Press CTRL+D

 # Login to the SQL comman line from the new user
 $ psql -U wattary -h 127.0.0.1 wattary

 # PASTE the tables commands
 ```

**To start postgres after closing: **
```shell
# To start the server .. "/usr/local/var/postgres" replace it with your path
$ pg_ctl -D /usr/local/var/postgres -l logfile start
```

 To use this module well:
 please read the following lines.

 Database Schema:
 ---------------------------------------------------------------------------------------------------------
 - Table Name(*)   | column1(type)  | column2(type)     | column3(type) ...                               
 ---------------------------------------------------------------------------------------------------------
 - users(1)        | user_id(int)   | user_name(string) | user_face(string) | a_t(string)                 
 ---------------------------------------------------------------------------------------------------------
 - light(2)        | user_id(int)   | val(bool)         | u_val(bool)       | flag(bool)                  
 ---------------------------------------------------------------------------------------------------------
 - air_con(2)      | user_id(int)   | o_val(int)        | in_val(int)       | u_val(int)   | flag(int)    
  ---------------------------------------------------------------------------------------------------------
 - tv(2)           | user_id(int)   | val(int)          | u_val(int)        | flag(bool)                  
 ---------------------------------------------------------------------------------------------------------
 - light_DS(3)     | user_id(int)   | val(bool)         | day(int)          | date(date)   | time(time)   
 ---------------------------------------------------------------------------------------------------------
 - air_con_DS(3)   | user_id(int)   | val(int)          | day(int)          | date(date)   | time(time)   
 ---------------------------------------------------------------------------------------------------------
 - tv_DS(3)        | user_id(int)   | val(int)          | day(int)          | date(date)   | time(time)   
 ---------------------------------------------------------------------------------------------------------
 - camera(4)       | user_id(int)   | src(string)                                                         
 ---------------------------------------------------------------------------------------------------------
 - user_pref(5)    | user_id(int)                                                                         
 ---------------------------------------------------------------------------------------------------------
 *:
   1. contains users basic data.
   2. contains the current state of the device.
   3. contains the data-set of the device.
   4. contains the latest images which passed to the camera.
   5. contains the user preferences>


 **Notes:**
 1. We don't need to add date and time columns in dataset tables because they will added automaticly.
 2. In dataset tables the date and time will be based on the date and time of the server.


 To load this module in your script, use:
 ```python
 from Memory import memory
 ```
 or
 ```python
 import Memory.memory
 ```
 or
 ```python
 import Memory.memory as anyName
 ```

 ## To read data from this module:
 use function `getValues(params)`
 - this function takes 3 parameters:

   1. table name. Ex: air_con_DS.
   2. a list of columns you need. Ex: ['o_val', 'in_val', 'flag'].
   3. the user-Id of the values you need.

 - and returning 2 values:

   1. code. Ex: 101.
   2. a dictionary with the values. Ex: {'o_val': 33, 'in_val': 24, 'flag': true}

   code meaning:

   101: this means the operation succeeded.
   102: this means that the user-ID is not exist and the dictionary will be None.
   103: this means failed to connect to the database and the dictionary will be None.
   104: this means wrong table name.
   105: this means wrong columns name.

 Ex:
 ```python
   code, data = memory.getValues('air_con_DS', ['o_val', 'in_val', 'flag'], 13)
   if code == 101:
       outSideVal  = data['o_val']
       inSideVal   = data['in_val']
       flag        = data['flag']
   elif code == 102:
       logging.warning('the user_id is not exist.')
   elif code == 103:
       logging.warning('Failed to connect to the Database.')
   else:
       logging.warning('unrecognized code: ' + code)
```

 ## To insert data to a table:
 use function `insertValues(params)`
 - this function takes 2 parameters:
   1. table name. Ex: air_con_DS.
   2. a dictionary of columns and the values you want. Ex: {'o_val': 33, 'in_val': 22}.

 - and returning 2 values:
   1. code. Ex: 201.
   1. the inserted id.

   code meaning:

   201: this means the operation succeeded.
   203: this means failed to connect to the database.
   204: this means wrong table name.
   205: this means wrong columns name.

 Ex:
 ```python
   code, userID = memory.insertValues('air_con_DS', {'o_val': 33, 'in_val': 22})
   if code == 202:
       logging.warning('the user_id is not exist.')
   elif code == 203:
       logging.warning('Failed to connect to the Database.')
   elif code != 201:
       logging.warning('unrecognized code: ' + code)
```

 ## To Modify data in a table:
 use function `modifyValues(params)`

 **WARNING: this function doesn't work for tables of type (2 or 3).**

  - this function takes 3 parameters:
   1. table name. Ex: air_con.
   2. a dictionary of columns and the values you want to modify. Ex: {'o_val': 33, 'in_val': 22}.
   3. the user-Id of the values you need.

 - and returning 1 value:
   1. code. Ex: 301.

   code meaning:

   301: this means the operation succeeded.
   302: this means that the user-ID is not exist.
   303: this means failed to connect to the database.
   304: this means wrong table name.
   305: this means wrong columns name.
   306: this can't use this function for this type of table.

 Ex:
 ```python
   code = memory.modifyValues(air_con, {'o_val': 33, 'in_val': 22}, 13)
   if code == 302:
       logging.warning('the user_id is not exist.')
   elif code == 303:
       logging.warning('Failed to connect to the Database.')
   elif code != 301:
       logging.warning('unrecognized code: ' + code)
```
