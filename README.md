# PhoenixV2

## Installation

at root create your environment with
```bash
virtualenv [envname]
```
then run your env
```bash
source [envname]/bin/activate
```
* install django requirement
```bash
pip install -r requirements.txt
```
* go to tailwind folder
```bash
cd tailwind
```
* update npm package 
* =========== only update npm in [tailwind] folder ===========
```bash
npm i
npm upgrade
```

## Start dev
start environment
```bash
source [envname]/bin/activate
```
[First Terminal] run django server
```bash
python manage.py runserver 
```
[Second Terminal] run tailwind server
```bash
cd tailwind
npm run watch
```
##


