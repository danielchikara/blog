# Blog
## el proyecto esta divido en 2 partes la pimera app se llama User que divide la logica tennemos dentro de esa app toda la parte de crud de usuarios el  inicio de sesion con token 





Documentación API: https://documenter.getpostman.com/view/10921323/2s93mAVLaX

## Este proyecto utiliza una base de datos sqlite que esta dentro de git

## Activar entorno virtual  de s preferencia  e instalar requqerimientos

```
pip install -r requirements.txt
```

## ya viene con base de datos pero si se desaea usar una aparte puedes correr el comando para hacer las migraciones 

```
sh migrate.sh
``` 

### en blog_app usamos todo lo referente al blog y usamos el el siste  de permisos creado en el archvo permission.py  que limita a los usarios y da los permisos de roles  


###  a la hora de crerar una nueva entrada al blog se verifica si las etiquetas o categorias existen y si no existen las crea y las guarda de manera inmendiata

### si necesitan credenciales para entrar son admin y la contraseña es qwertyuiop1

### quedo al pendiente muchas gracias por la oportunidad