"""Confere o .pptx gerado: densidade de texto, figuras e risco de estouro.

Uso:
    python slides/scripts/conferir.py slides/saida/aula-1.pptx

Não substitui abrir o arquivo no PowerPoint. Pega o que dá para pegar sem
renderizar: slide com texto demais, título longo, figura fora de proporção,
slide sem nota do apresentador.
"""

from __future__ import annotations

import sys
from pathlib import Path

from pptx import Presentation
from pptx.util import Emu

LIMITE_CARACTERES = 520  # texto projetado por slide, fora título
LIMITE_TITULO = 62
LIMITE_LINHAS = 9
LIMITE_ANCORA = 300  # âncora prática: frase única, projetada em corpo grande


def conferir(caminho: Path) -> int:
    prs = Presentation(str(caminho))
    larg = Emu(prs.slide_width).inches
    alt = Emu(prs.slide_height).inches
    print(f"{caminho.name}: {len(prs.slides.__iter__.__self__._sldIdLst)} slides, {larg:.2f} x {alt:.2f} pol\n")

    alertas = 0
    for i, slide in enumerate(prs.slides, start=1):
        textos, figuras_ = [], []
        for forma in slide.shapes:
            if forma.has_text_frame and forma.text_frame.text.strip():
                textos.append(forma.text_frame.text.strip())
            if forma.shape_type == 13:  # PICTURE
                figuras_.append(forma)

        corpo = "\n".join(textos)
        titulo = textos[0].split("\n")[0] if textos else ""
        linhas = sum(t.count("\n") + 1 for t in textos)
        nota = slide.notes_slide.notes_text_frame.text.strip() if slide.has_notes_slide else ""

        # Slide de âncora: uma frase longa é o conteúdo, não um defeito.
        ancora = len(figuras_) == 0 and len(textos) <= 3 and len(titulo) > 100

        problemas = []
        if ancora:
            if len(titulo) > LIMITE_ANCORA:
                problemas.append(f"âncora longa demais para projetar: {len(titulo)} caracteres")
            print(f"  {i:>3}. (âncora) {titulo[:52]}...")
            for pr in problemas:
                print(f"        -> {pr}")
                alertas += len(problemas)
            continue
        if len(corpo) > LIMITE_CARACTERES:
            problemas.append(f"texto denso: {len(corpo)} caracteres")
        if len(titulo) > LIMITE_TITULO:
            problemas.append(f"título longo: {len(titulo)} caracteres")
        if linhas > LIMITE_LINHAS:
            problemas.append(f"muitas linhas: {linhas}")
        for fig in figuras_:
            direita = Emu(fig.left + fig.width).inches
            base = Emu(fig.top + fig.height).inches
            if direita > larg - 0.3 or base > alt - 0.35:
                problemas.append(f"figura invade a margem (direita {direita:.2f}, base {base:.2f})")
        if not nota and figuras_:
            problemas.append("figura sem nota do apresentador")

        marca = "!" if problemas else " "
        resumo = titulo[:58] if titulo else "(sem título)"
        extras = f" [fig: {len(figuras_)}]" if figuras_ else ""
        print(f"{marca} {i:>3}. {resumo}{extras}")
        for p in problemas:
            print(f"        -> {p}")
            alertas += 1

    print(f"\n{alertas} alerta(s).")
    return alertas


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("uso: python slides/scripts/conferir.py <arquivo.pptx>")
    sys.exit(1 if conferir(Path(sys.argv[1])) else 0)
