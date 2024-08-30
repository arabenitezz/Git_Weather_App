#!/bin/bash

# Mostrar un mensaje inicial
echo "Iniciando la instalación de dependencias..."

# Verificar si pip está instalado
if ! command -v pip &> /dev/null
then
    echo "pip no está instalado. Por favor, instala pip antes de continuar."
    exit 1
fi

# Instalar dependencias desde requirements.txt
echo "Instalando dependencias desde requirements.txt..."
pip install -r requirements.txt

# Verificar si la instalación fue exitosa
if [ $? -eq 0 ]; then
    echo "Dependencias instaladas correctamente."
else
    echo "Error al instalar dependencias. Revisa el archivo requirements.txt y asegúrate de que todo esté correcto."
    exit 1
fi

# Mensaje final
echo "Instalación completada."
