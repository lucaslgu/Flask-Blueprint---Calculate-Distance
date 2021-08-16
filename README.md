# Flask-Blueprint - Calculate the distance from the Moscow ring road to the requested destination

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/lucaslgu/Flask-Blueprint---Calculate-Distance/blob/main/LICENSE) 

# About Project

This is an application developed in the micro framework flask to calculate the distance between two points, one of which is being sent by the API and the other is the location of the MKAD that is inside the application.

# Technologies used
## Back end
- Python
- Flask
- Geodesic
- Logging
- PyUnit

# How to run the project

## Back end
Prerequisites: Python 3.8, Insominia or Postman

```bash
# clone repository
git clone https://github.com/lucaslgu/Flask-Blueprint---Calculate-Distance.git

# run the project
python main.py

# request endpoint
http://localhost:5000/?yourLocate=00.00000000000,00.00000000000

# return
message - distance calculation
status_code - code http
```

# Author

Lucas Henrique da Silva Ribeiro

https://www.linkedin.com/in/lucas-ribeiro-py/
