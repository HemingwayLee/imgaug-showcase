# imgaug-showcase
* Init
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt 
```

* Init by docker
```
docker build -t imgaug .
docker run -it --rm -v $(PWD):/home/app imgaug
```

* Run scripts
```
python3 hello.py
```

