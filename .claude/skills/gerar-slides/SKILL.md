---
name: gerar-slides
description: Gera e atualiza os decks .pptx da formação a partir dos arquivos de conteúdo em slides/conteudo/. Use ao criar slides, editar o texto de um slide, adicionar figura ou reconstruir o deck.
---

# Gerar os slides da formação

O deck é código. Ninguém edita o `.pptx` à mão: edita-se o conteúdo em Markdown e o arquivo é reconstruído.

## Fluxo

1. Edite o conteúdo em `slides/conteudo/<aula>.md`, seguindo a gramática abaixo.
2. Reconstrua:

   ```bash
   python slides/scripts/build_deck.py slides/conteudo/<aula>.md
   ```

3. Confira antes de entregar:

   ```bash
   python slides/scripts/conferir.py slides/saida/<aula>.pptx
   ```

   O resultado precisa terminar com `0 alerta(s)`. Alerta de texto denso significa dividir o slide, não reduzir a fonte.

## Gramática do conteúdo

Slides separados por uma linha com `---`. Dentro de cada slide:

| Marca | Efeito |
|---|---|
| `# Título` | slide de conteúdo |
| `## Título` | divisória de bloco, em negativo |
| `### Subtítulo` | linha de apoio sob o título |
| `@capa` / `@encerramento` | abertura e fechamento |
| `!! Frase` | âncora prática, em destaque |
| `:fig nome` | figura gerada por `figuras.py` |
| `:fonte Texto` | crédito sob a figura |
| `:bloco Rótulo` | rótulo de rodapé, vale até mudar |
| `- item` / `  - item` | marcadores, dois níveis |
| `> nota` | nota do apresentador |

Figura junto de marcadores gera layout de duas colunas. Figura sozinha ocupa a área útil inteira.

## Figuras

Toda figura é gerada por script, nunca colada de imagem pronta:

```bash
python slides/scripts/figuras.py            # todas
python slides/scripts/figuras.py subagente  # uma
```

Para criar uma nova, adicione uma função `fig_<nome>` em `slides/scripts/figuras.py`, devolvendo uma figura matplotlib. O nome no conteúdo é o sufixo com hífens.

Detalhes de paleta, tipografia, regras de citação de fonte e critérios de qualidade acadêmica estão em [references/estilo-visual.md](references/estilo-visual.md). Leia antes de criar figura ou mexer em cor.

## Regras

**Número que veio da documentação carrega fonte.** O crédito vai no `:fonte` do slide, com o mês de captura.

**Cor e tipografia moram em `slides/scripts/estilo.py`.** Não escreva cor literal em figura nem no construtor.

**O `.pptx` é artefato gerado.** Nunca edite o arquivo de saída: a próxima reconstrução descarta a alteração.
