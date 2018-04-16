# WATTARY Eye:

**To Do:**
- [x] Write Eye API.
- [x] Write The Docs For Eye.

**Please Note: the descriptors are saved in a CSV file NOT in the database.**

**Dependencies:**
- dlib *[requires cmake >= 2.8.13]*.
- sci-kit learn *(skimage)*.
- numpy

**Instalation of Dependencies:**


1- dlib:
```shell
$ pip install dlib
```
2- scikit learn:
```shell
$ pip install scikit-learn
```

**To Use Eye:**
```python
from Eye import eye
```
Or
```python
import Eye.eye
```
Or
```python
import Eye.eye as anyName
```
**Note: A face must be more than 100px*100px to be detected.**

**To add a user to the database**
use function register(params)
- this function takes 2 parameters:
    1- User name. Ex: Sayed Mahmoud
    2- a full url of his picture. Ex: https://www.pictures.com/img_002314562.jpg

- and returning 1 value:
    1- code. Ex: 101.

**code meaning:**

    101: this means the operation succeeded.
    102: this means that I can not read the picture (not Exist).
    103: this means that I can not find any faces in the picture (retake a picture)
    104: this means that the user is exist.
    105: this means a memory (database) error.
   
   
Ex:
```python
code = register('Ahmed Abdeldaim', 'https://www.pictures.com/img_002314562.jpg')
```

**To recognize a face from a picture**
use function login(params)
- this function takes 1 parameters:
   1- a full url of his picture. Ex: https://www.pictures.com/img_002314562.jpg

- and returning 2 value:
   1- code. Ex: 201.
   2- userID (if exist else null)

**code meaning:**

    201: this means that the user is exist.    
    202: this means that I can not read the picture (not Exist).
    203: this means that I can not find any faces in the picture (retake a picture)
    204: this means that I can not recognize this person.
    
    
Ex:
```python
code, userID = login('https://www.pictures.com/img_002314562.jpg')
```
