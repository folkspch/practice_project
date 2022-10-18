# Phoenix2

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
---watch mode - this mode will update output.css in realtime.
```bash
tailwindcss -i ./static/src/main.css -o ./static/src/output.css --watch
```

minifying css for production
```bash
tailwindcss -i ./static/src/main.css -o ./static/src/output.css --minify
```

Help text of pytailwindcss
run
```bash
tailwindcss
```



