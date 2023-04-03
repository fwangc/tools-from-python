1. How to generate requirments.txt file 
    pip freeze > requirements.txt
    pip freeze --exclude="*-dev" --exclude="*-test" > requirements.txt  #This will create a requirements.txt file without including packages whose names contain "dev" or "test".
2. how to install all packages in requirments in python
    pip install -r requirements.txt