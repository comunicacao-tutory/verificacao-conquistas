#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cria o arquivo de um certificado a partir do codigo de verificacao.

Uso:
    python3 gerar-certificado.py "TUT-OURO-0125" \
        --mentor "Marcos Correia" \
        --mentoria "Mentoria Mestre" \
        --data "22/10/2026"

O nome do arquivo e o SHA-256 do sal mais o codigo normalizado. Quem nao
tem o codigo nao consegue montar a URL, e a pagina nao revela nenhum
certificado no codigo-fonte.

NUNCA coloque CPF, e-mail ou telefone aqui: o arquivo fica publico para
quem tiver o codigo.
"""

import argparse
import hashlib
import json
import os
import re
import unicodedata

SAL = "tutory-conquistas-2026"   # precisa ser identico ao SAL do index.html
AQUI = os.path.dirname(os.path.abspath(__file__))


def normalizar(codigo: str) -> str:
    """maiusculas, sem acento, so A-Z e 0-9 — igual ao normalizar() do JS."""
    s = unicodedata.normalize("NFD", codigo.upper())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return "".join(c for c in s if c.isalnum())


def nome_arquivo(codigo: str) -> str:
    base = normalizar(codigo)
    return hashlib.sha256((SAL + base).encode("utf-8")).hexdigest()[:24] + ".json"


def main() -> int:
    p = argparse.ArgumentParser(description="Gera o arquivo de um certificado.")
    p.add_argument("codigo", help="codigo de verificacao, ex. TUT-OURO-0125")
    p.add_argument("--mentor", required=True, help="nome completo do mentor")
    p.add_argument("--mentoria", required=True, help="nome da mentoria")
    p.add_argument("--data", required=True, help="data da conquista, DD/MM/AAAA")
    p.add_argument("--conquista", default="Placa Ouro", help="nome da conquista")
    p.add_argument("--alunos", default="100 alunos", help="marco atingido")
    a = p.parse_args()

    if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", a.data):
        print("  data precisa estar como DD/MM/AAAA")
        return 1

    registro = {
        "mentor": a.mentor,
        "mentoria": a.mentoria,
        "conquista": a.conquista,
        "alunos": a.alunos,
        "data": a.data,
        "codigo": a.codigo.upper(),
    }

    pasta = os.path.join(AQUI, "dados")
    os.makedirs(pasta, exist_ok=True)
    arquivo = nome_arquivo(a.codigo)
    caminho = os.path.join(pasta, arquivo)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(registro, f, ensure_ascii=False, indent=2)

    print()
    print(f'  codigo      : {a.codigo.upper()}')
    print(f'  normalizado : {normalizar(a.codigo)}')
    print(f'  arquivo     : dados/{arquivo}')
    print()
    print("  Publique e o codigo passa a ser verificavel.")
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
