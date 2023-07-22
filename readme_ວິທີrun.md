# ນາງ ປິ່ນແກ້ວ ເຂັມຄຳພູມີ ຫ້ອງ 3TC

ເວັບນີ້ສ້າງໂດຍໃຊ້ framework ຂອງ Python ທີ່ຊື່ວ່າ Flask ໃນການ run ຕ້ອງມີພາສາ python ແລະ ຕິດຕັ້ງແພກເກັຈທັງໝົດໃນ requirement.txt

## Runnig on Linux

```
cd digital-garden-assignment-main
```
### create virtual environment and activate it

```
$ sudo apt install python3-venv
```
```
$ python3 -m venv venv
```
```
$ source venv/bin/activate
```

### Install all packages in requirement.txt
```
$ pip install -r requirement.txt
```

### Run the server
```
$ export FLASK_APP=fg
```
```
$ flask run
```


## Running On Windows
