"""Genera una lista de destinatarios para pegar en Gmail desde un CSV."""

import argparse
import csv
import re
import sys
from pathlib import Path


EMAIL_COLUMN = "Dirección de correo electrónico"
EMAIL_PATTERN = re.compile(
    r"^[A-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Z0-9-]+(?:\.[A-Z0-9-]+)+$",
    re.IGNORECASE,
)


def extraer_correos(archivo_csv: Path) -> list[str]:
    """Lee y devuelve correos válidos, únicos y en el orden del CSV."""
    correos: list[str] = []
    vistos: set[str] = set()

    with archivo_csv.open("r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames is None or EMAIL_COLUMN not in lector.fieldnames:
            raise ValueError(
                f'No se encontró la columna requerida "{EMAIL_COLUMN}".'
            )

        for fila in lector:
            valor = (fila.get(EMAIL_COLUMN) or "").strip()
            clave = valor.casefold()
            if valor and EMAIL_PATTERN.fullmatch(valor) and clave not in vistos:
                vistos.add(clave)
                correos.append(valor)

    return correos


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extrae correos de un CSV y crea una lista para Gmail."
    )
    parser.add_argument("archivo_csv", type=Path, help="CSV de entrada")
    parser.add_argument(
        "-o",
        "--salida",
        type=Path,
        default=Path("correos.txt"),
        help="Archivo de salida (por defecto: correos.txt)",
    )
    argumentos = parser.parse_args()

    if not argumentos.archivo_csv.is_file():
        print(
            f"No existe el archivo CSV: {argumentos.archivo_csv}",
            file=sys.stderr,
        )
        return 1

    try:
        correos = extraer_correos(argumentos.archivo_csv)
        argumentos.salida.write_text(
            ", ".join(correos) + ("\n" if correos else ""),
            encoding="utf-8",
        )
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Se escribieron {len(correos)} correos en {argumentos.salida}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
