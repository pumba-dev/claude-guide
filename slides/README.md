# Slides

O deck é gerado por código. O que se edita é o conteúdo em Markdown; o `.pptx` é artefato de saída.

```
slides/
├── conteudo/aula-1.md      <- o texto dos slides. É aqui que se escreve
├── scripts/
│   ├── estilo.py           <- paleta, tipografia, medidas, autor
│   ├── figuras.py          <- as figuras, geradas com matplotlib
│   ├── build_deck.py       <- monta o .pptx e exporta o PDF
│   ├── conferir.py         <- confere densidade, margens e notas
│   └── exportar_pdf.ps1    <- converte para PDF, via PowerPoint
├── build/
│   ├── figuras/            <- PNGs gerados
│   └── aula-1.pdf          <- PDF de conferência
└── saida/aula-1.pptx       <- entregável
```

## Uso

```bash
pip install python-pptx matplotlib pillow

python slides/scripts/figuras.py                        # gera as figuras
python slides/scripts/build_deck.py slides/conteudo/aula-1.md   # .pptx + .pdf
python slides/scripts/conferir.py slides/saida/aula-1.pptx      # lint estrutural
```

`build_deck.py` gera sozinho qualquer figura que esteja faltando e, ao final,
exporta `build/aula-1.pdf` usando o PowerPoint instalado. Use `--sem-pdf` para pular.

## Por que o PDF importa

O lint estrutural pega texto demais e figura fora da margem, mas é cego para o
que só aparece renderizado: marcação que vazou como texto literal, rótulo
estourando a caixa de uma figura, seta cruzando legenda. O PDF é o que permite
**ver** o slide e corrigir isso antes da sala.

Três defeitos reais foram encontrados exatamente assim, e nenhum deles aparecia
no lint. Portanto: revisar o PDF é parte do processo, não etapa opcional.

Se a conversão falhar com `Call was rejected by callee`, o PowerPoint está
ocupado. Feche o programa e rode de novo.

A conferência precisa terminar em `0 alerta(s)`. Alerta de texto denso se resolve dividindo o slide, nunca diminuindo a fonte.

## Por que assim, e não no PowerPoint

- **Rastreabilidade.** Os números do orçamento de janela e do custo de subagente vêm da documentação oficial. Mudou o número, muda a figura, e o `git diff` mostra o que mudou.
- **Revisão.** Conteúdo em Markdown se revisa em pull request. Um `.pptx` binário, não.
- **Reprodutibilidade.** O deck inteiro se refaz com um comando, em qualquer máquina.
- **Coerência com o conteúdo.** A aula defende procedimento versionado e material de apoio separado. O próprio deck é o exemplo: [skill `gerar-slides`](../.claude/skills/gerar-slides/SKILL.md) com o procedimento, e `references/estilo-visual.md` com a configuração.

## Antes de apresentar

- [ ] Abrir o `.pptx` no PowerPoint da máquina do auditório e percorrer os 40 slides
- [ ] Conferir se `Georgia`, `Segoe UI` e `Consolas` renderizaram como esperado
- [ ] Ajustar `INSTITUICAO` em `scripts/estilo.py` para o nome oficial do laboratório
- [ ] Revisar as notas do apresentador, que saem no modo apresentador
- [ ] Confirmar que todo slide com número da documentação está com o crédito e o mês de captura

## Pendente

- Deck da Aula 2. A prática é conduzida pela [folha do aluno](../docs/folha-do-aluno.md), então o deck da Aula 2 é curto: abertura, retomada dos doze conceitos, os passos projetados e o fechamento.
