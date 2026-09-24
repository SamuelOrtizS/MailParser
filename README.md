# MailParser

Script para extraer direcciones de correo electrónico desde un archivo CSV y
generar una lista lista para pegar en Gmail.

## Requisitos

- Python 3.9 o superior.
- Un archivo CSV con una columna llamada exactamente:

```text
Dirección de correo electrónico
```

El script usa únicamente la biblioteca estándar de Python, por lo que no es
necesario instalar dependencias adicionales.

## Uso rápido

Abre PowerShell en la carpeta del repositorio y ejecuta:

```powershell
python .\generar_correos.py "archivo.csv"
```

El resultado se guardará en `correos.txt` dentro de la carpeta actual. Los
correos estarán en una sola línea, separados por comas, para poder copiarlos y
pegarlos en los campos de destinatarios de Gmail.

### Ejemplo con el CSV incluido

```powershell
python ".\generar_correos.py" ".\FORMULARIO INSCRIPCIÓN CONVERSATORIO INTERNACIONAL DE TELECOMUNICACIONES (respuestas) - Respuestas de formulario 1.csv"
```

El repositorio incluye un [correos.txt](correos.txt) generado con ese archivo
de ejemplo.

## Elegir el archivo de salida

Usa `-o` o `--salida` para especificar otro nombre o ubicación:

```powershell
python .\generar_correos.py "archivo.csv" -o "destinatarios.txt"
```

Si no se indica esta opción, el archivo de salida será `correos.txt`.

## Qué hace el script

1. Lee el CSV en codificación UTF-8, incluyendo archivos con marca BOM.
2. Busca la columna `Dirección de correo electrónico`.
3. Elimina espacios al inicio y al final de cada valor.
4. Omite valores vacíos o que no tienen un formato de correo válido.
5. Elimina duplicados sin distinguir mayúsculas de minúsculas y conserva el
   orden de aparición.
6. Escribe los correos válidos separados por comas.

## Errores comunes

### No se encuentra la columna requerida

Verifica que el encabezado del CSV coincida exactamente con:

```text
Dirección de correo electrónico
```

También comprueba que el archivo use la primera fila como encabezado.

### No existe el archivo CSV

Comprueba la ruta y el nombre del archivo. Cuando el nombre contiene espacios,
enciérralo entre comillas:

```powershell
python .\generar_correos.py "C:\ruta\mi archivo.csv"
```

## Uso en Gmail

Abre `correos.txt`, copia su contenido y pégalo en el campo de destinatarios de
Gmail. Para proteger la privacidad de los destinatarios, considera usar el
campo **CCO (copia oculta)** cuando corresponda y verifica la lista antes de
enviar el mensaje.
