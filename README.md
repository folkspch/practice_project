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
* go to tailwindApp folder this is a tailwind configuration folder
```bash
cd tailwindApp
```
* update npm package 
* =========== only update npm in [tailwindApp/static_src] folder ===========
```bash
npm i
npm upgrade
```

## Start dev
start environment
```bash
source penv/bin/activate
```
run server
```bash
python manage.py runserver 
python manage.py tailwind start
```
##


