# Libreria Epson TM-T900FA Python 

_Libreria para manejo de la impresora fiscal Epson modelo TM-T900FA escrita en python para sistemas operativos Windows._ 

![alt text](https://raw.githubusercontent.com/sambenzt/TM-T900FA/master/image.jpeg =250x)
 
### Instalación 

_Descomprimir el archivo **Python - Epson dll.rar**_

_Instalar python-2.7.2.msi_

_Agregar python a las variables de entorno de windows._

_Copiar el archivo **EpsonFiscalInterface.dll** en la ruta **C:\Windows\SysWOW64**_

_Abri la consola de comandos e ingresar a la ruta ****C:\Windows\SysWOW64**** y registrar **EpsonFiscalInterface.dll**:_
```
> cd C:\Windows\SysWOW64
```

_luego_

```
> regsvr32 EpsonFiscalInterface.dll
```
## Probando la libreria

_Abre una consola de comandos en la carpeta del proyecto y ejecuta_

```
> python
```
_Si python esta bien instaldo deberia aparecer el siguiente mensaje en la consola_

```
> Python 2.7.2 (default, Jun 12 2011, 15:08:59) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
_Dentro de la carpeta del proyecto ejecutar_

 
 ```
> python app_client_using_dll.py
```

_La impresora deberia imprimir los siguientes tipos de comprobantes como se muestra en la seccion **main** de la libreria_

* _**Tique**_
* _**Tique Factura**_
* _**Tique Factura B**_
* _**Tique nota de debito**_
* _**ique nota de debito B**_
* _**Tique nota de credito**_
* _**Tique nota de credito B**_
* _**Cierre X y Z**_
*  _**Auditoria**_

_Probado en windows 7 de 64bits._

## Licencia 📄

La libreria pertence a Epson. Enlace de descarga de archivos originales en la web de [Epson](https://epson.com.ar/Soporte/Punto-de-venta/Impresoras-fiscales/Epson-TM-T900FA/s/SPT_C31CB76402)


---
⌨️ con ❤️ por [Sambenzt](https://github.com/sambenzt) 😊