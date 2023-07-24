# digital-garden-assignment# ນາງ ປິ່ນແກ້ວ ເຂັມຄຳພູມີ ຫ້ອງ 3TC
ເວັບນີ້ແມ່ນເພີ່ມຖານຂໍ້ມູນຜູ້ໃຂ້ຂຶ້ນມາ ສາມາດສ້າງບັນຊີ ແລະ Login ໄດ້


ເວັບນີ້ສ້າງໂດຍໃຊ້ framework ຂອງ Python ທີ່ຊື່ວ່າ Flask ໃນການ run ຕ້ອງມີພາສາ python ແລະ ຕິດຕັ້ງແພກເກັຈທັງໝົດໃນ requirement.txt

## ສຳລັບ Linux

```
cd digital-garden-assignment-main
```
### create virtual environment and activate it

```
sudo apt install python3-venv
```
```
python3 -m venv venv
```
```
source venv/bin/activate
```

### Install all packages in requirement.txt
```
pip install -r requirement.txt
```

### Run the server
```
export FLASK_APP=fg
```
```
flask run
```


## ສຳລັບ Windows
```
cd digital-garden-assignment-main
```
### create new file in digital-garden-assignment-main directory
place these code and save it as "main.py"
```
from fg import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=False)
```
### Create virtual environment
```
python -m venv venv
```
activate it
```
venv\Scripts\activate
```

### Install all packages in requirement.txt
```
pip install -r requirement.txt
```

### Run the Server
```
python main.py
```

## ສຳລັບ Mac
### ນ້ອງບໍ່ຮູ້ວິທີ run ເທິງ Mac Os ເພາະຍັງບໍ່ໄດ້ລອງ ແຕ່ວິທີອາດຈະຄ້າຍຄືກັນ, ແຕ່ແນະນຳໃຫ້ run ເທິງ Linux ຫຼືບໍ່ກໍ Windows 
----
ສາມາດໄປໂຫລດໄຟລທັງໝົດໄດ້ທີ່ (https://github.com/Pinkeo/digital-garden-assignment)
