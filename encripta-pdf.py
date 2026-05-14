#!/usr/bin/env python3
"""
encripta-pdf.py — Aplica les restriccions de còpia/impressió a un PDF.

ÚS:
    python3 encripta-pdf.py <fitxer.pdf> [<més_fitxers.pdf>...]

Substituirà cada PDF in-place per la versió amb:
    · Còpia de text deshabilitada
    · Impressió deshabilitada
    · Extracció de contingut deshabilitada
    · Anotacions deshabilitades

REQUISITS:
    pip install pikepdf

Si no tens pikepdf:
    Windows:  py -m pip install pikepdf
    Mac:      python3 -m pip install pikepdf
    Linux:    pip3 install pikepdf
"""
import sys
import secrets
from pathlib import Path

try:
    import pikepdf
except ImportError:
    print("Falta la llibreria 'pikepdf'. Instal·la-la amb:")
    print("    pip install pikepdf")
    sys.exit(1)


def encrypt_in_place(path: Path) -> None:
    """Encrypt a PDF in place with no-copy/no-print/no-extract restrictions."""
    if not path.exists():
        print(f"  [!] No existeix: {path}")
        return

    # Random owner password — keeps the user password empty so the PDF opens
    # without prompting, but locks down all interactive permissions.
    owner_pwd = secrets.token_urlsafe(16)
    tmp = path.with_suffix(".tmp.pdf")
    try:
        pdf = pikepdf.open(str(path))
        pdf.save(
            str(tmp),
            encryption=pikepdf.Encryption(
                user="",
                owner=owner_pwd,
                R=6,  # AES-256
                allow=pikepdf.Permissions(
                    extract=False,
                    modify_other=False,
                    modify_annotation=False,
                    modify_assembly=False,
                    modify_form=False,
                    print_lowres=False,
                    print_highres=False,
                ),
            ),
        )
        pdf.close()
        tmp.replace(path)
        print(f"  ✓ Encriptat: {path.name}")
    except Exception as e:
        if tmp.exists():
            tmp.unlink()
        print(f"  [!] Error encriptant {path.name}: {e}")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        sys.exit(1)
    for arg in argv[1:]:
        encrypt_in_place(Path(arg))


if __name__ == "__main__":
    main(sys.argv)
