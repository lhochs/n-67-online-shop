# group67project

Project Idea: N 67° Online Store

Stack: Python

Description:

For our group project we decided to create an online store. It will display products users (registered or not) can buy. Sellers (registered users with a reference number) can add/edit/delete. Only sellers of the added product can edit or delete their product from the store. Users can view items in their shopping cart and their total before deciding to purchase their items. Here they can adjust the quantity on each item or delete items from their cart. Check out will redirect users to the Home page. 

Roles:

Lily Ochs – Co-Group Lead, Front-End, Check-Out Page;
Angel Galicia – Front-End;
Matthew Luk – Co-Group Lead, Back-End;
Corey Duffy – Front-End;
Ngan Tran – Back-End, Api;

## Run the app on your localhost
1. Install pipenv for virtual environment
```
pip3 install pipenv
```

2. Activating our Virtual Environment
```
python3 -m pipenv shell
```

3. Install dependencies for Pipfile
```
pipenv install -r requirements.txt
```
Note: To install any dependency, you can run this command:
```
pipenv install <dependency_name>
For ex: `pipenv install flask`
```

4. Run our server!
```
python3 server.py
```
