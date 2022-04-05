# README - CEBD1160 Final Project

## SQL Config
```msyql
mysql> show VARIABLES LIKE 'validate_password%';
+--------------------------------------+--------+
| Variable_name                        | Value  |
+--------------------------------------+--------+
| validate_password.check_user_name    | ON     |
| validate_password.dictionary_file    |        |
| validate_password.length             | 8      |
| validate_password.mixed_case_count   | 1      |
| validate_password.number_count       | 1      |
| validate_password.policy             | MEDIUM |
| validate_password.special_char_count | 1      |
+--------------------------------------+--------+
7 rows in set (0.03 sec)

# Allows setting the password as specified

mysql> set GLOBAL validate_password.special_char_count = 0;
mysql> set GLOBAL validate_password.mixed_case_count = 1;

# Grant permissions on the DB
mysql> GRANT ALL PRIVILEGES ON sales.* TO cebd1160_user@'%';

# Decimal column type caused jsonify exception. See below
mysql> alter table Customer drop discount;
```

### Python exception with jsonify

```python
# Exception when discount column data type was decimal
10.0.2.2 - - [04/Apr/2022 18:41:59] "GET /v1/customers HTTP/1.1" 500 -
Traceback (most recent call last):
  File "/home/ubuntu/anaconda3/lib/python3.9/site-packages/flask/app.py", line 2464, in __call__
    return self.wsgi_app(environ, start_response)
  File "/home/ubuntu/anaconda3/lib/python3.9/site-packages/flask/app.py", line 2450, in wsgi_app
    response = self.handle_exception(e)
  File "/home/ubuntu/anaconda3/lib/python3.9/site-packages/flask/app.py", line 1867, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/home/ubuntu/anaconda3/lib/python3.9/site-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/home/ubuntu/anaconda3/lib/python3.9/site-packages/flask/app.py", line 2447, in wsgi_app
    response = self.full_dispatch_request()
  File "/home/ubuntu/anaconda3/lib/python3.9/site-packages/flask/app.py", line 1952, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/home/ubuntu/anaconda3/lib/python3.9/site-packages/flask/app.py", line 1821, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/home/ubuntu/anaconda3/lib/python3.9/site-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/home/ubuntu/anaconda3/lib/python3.9/site-packages/flask/app.py", line 1950, in full_dispatch_request
    rv = self.dispatch_request()
  File "/home/ubuntu/anaconda3/lib/python3.9/site-packages/flask/app.py", line 1936, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/Documents/cebd1160/cebd-1160-projectstarter-winter-2022/WS/customer_service.py", line 11, in get_all_sales
    return jsonify(BAL.customer.get_all_customers())
  File "/home/ubuntu/anaconda3/lib/python3.9/site-packages/flask/json/__init__.py", line 370, in jsonify
    dumps(data, indent=indent, separators=separators) + "\n",
  File "/home/ubuntu/anaconda3/lib/python3.9/site-packages/flask/json/__init__.py", line 211, in dumps
    rv = _json.dumps(obj, **kwargs)
  File "/home/ubuntu/anaconda3/lib/python3.9/json/__init__.py", line 234, in dumps
    return cls(
  File "/home/ubuntu/anaconda3/lib/python3.9/json/encoder.py", line 201, in encode
    chunks = list(chunks)
  File "/home/ubuntu/anaconda3/lib/python3.9/json/encoder.py", line 429, in _iterencode
    yield from _iterencode_list(o, _current_indent_level)
  File "/home/ubuntu/anaconda3/lib/python3.9/json/encoder.py", line 325, in _iterencode_list
    yield from chunks
  File "/home/ubuntu/anaconda3/lib/python3.9/json/encoder.py", line 405, in _iterencode_dict
    yield from chunks
  File "/home/ubuntu/anaconda3/lib/python3.9/json/encoder.py", line 438, in _iterencode
    o = _default(o)
  File "/home/ubuntu/anaconda3/lib/python3.9/site-packages/flask/json/__init__.py", line 100, in default
    return _json.JSONEncoder.default(self, o)
  File "/home/ubuntu/anaconda3/lib/python3.9/json/encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '

```

## Python environment
 ```bash
 (base) ubuntu@ubuntu01:~/Documents/cebd1160/cebd-1160-projectstarter-winter-2022$  pip3 install mysql-connector

 # Setup .mysql.cnf
(base) ubuntu@ubuntu01:~/Documents/cebd1160/cebd-1160-projectstarter-winter-2022$  cat .my.cnf
[client]
user=cebd1160_user
password=cebd1160
port=3306
database=sales
 ```


## Project Setup
For this project, data is stored in `ubuntu@ubuntu01:~/Documents/cebd1160/data`