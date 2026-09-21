# IA Generativa, LLMs e o ecossistema Claude

Formação de duas aulas de 60 minutos sobre o funcionamento interno de modelos de
linguagem e sobre como operar ferramentas agênticas em projetos de pesquisa.
Este repositório reúne todo o material: slides, roteiro do instrutor, folha do
aluno e o gabarito da prática.

**Aula 1 é conceitual. Aula 2 é prática.** Na segunda aula cada participante
constrói, do zero, um agente que lê as fontes da própria área e escreve uma
newsletter semanal — com orquestrador, skills e material de apoio.

## Para quem

Mestrandos e pesquisadores em ciência da computação: alta maturidade técnica em
sistemas, protocolos e programação, pouca familiaridade com o funcionamento
interno de LLMs e com ferramentas agênticas.

Idioma do material: português do Brasil. Termos técnicos permanecem em inglês
quando a tradução soaria artificial (token, prompt, thinking, subagent).

## Objetivo

Ao final das duas aulas, o participante deve:

- entender **por que** uma LLM se comporta como se comporta;
- saber **operar** Claude Chat, Cowork e Code nos próprios projetos.

## Formato

| Aula | Duração | Foco |
|---|---|---|
| **1 — Conceitos** | ~66 min | Blocos 0 a 6: fundamentos de LLM, anatomia de uma requisição, do sistema ao agente, produtos concretos, aplicação em pesquisa. |
| **2 — Prática** | 60 min | Construção do agente de newsletter em pasta vazia, acionado sob demanda. |

Entre as duas aulas, o participante instala o Claude Code e rascunha de 4 a 6
fontes da própria área.

## Os treze conceitos

A formação inteira se organiza em torno de treze conceitos, em quatro camadas
que respondem a quatro perguntas:

| Camada | Pergunta | Conceitos |
|---|---|---|
| 0 | Onde você está | harness |
| A | O que o modelo vê | janela de contexto, sessão, contexto persistente |
| B | Como ele responde | modelos, thinking e effort |
| C | O que ele consegue fazer | tool use / MCP e connectors, skills, references, subagents, agente orquestrador |
| Transversal | — | permissões e modos de execução, verificação |

Toda a teoria existe para sustentá-los, e não o contrário. A ordem dos blocos
segue uma cadeia de dependências: token sustenta janela de contexto, que
sustenta sessão; tool use sustenta orquestrador e subagents.

## O que tem aqui

```
.
├── docs/
│   ├── estrutura-apresentacao.md   <- fonte única da estrutura: público, conceitos, blocos
│   ├── roteiro-blocos.md           <- detalhamento minutado da Aula 1
│   ├── pratica-guiada.md           <- plano do instrutor para a Aula 2
│   ├── folha-do-aluno.md           <- prompts prontos, material entregue ao aluno
│   └── claude-oficial-doc/         <- espelho local da documentação oficial (consulta)
├── slides/                         <- deck gerado por código a partir de Markdown
└── gabarito/                       <- resultado esperado da prática (material do instrutor)
```

| Documento | Para quê |
|---|---|
| [Estrutura da apresentação](docs/estrutura-apresentacao.md) | Ponto de entrada. Público, objetivo, os treze conceitos, os blocos das duas aulas. |
| [Roteiro bloco a bloco](docs/roteiro-blocos.md) | Aula 1 minutada: o que mostrar e a âncora prática de cada bloco. |
| [Prática guiada](docs/pratica-guiada.md) | Aula 2 pelo lado do instrutor: passos, tempos e pontos de intervenção. |
| [Folha do aluno](docs/folha-do-aluno.md) | Aula 2 pelo lado do aluno: os prompts que ele copia. |
| [Slides](slides/README.md) | Como o deck é construído, conferido e exportado. |
| [Gabarito](gabarito/README.md) | O agente pronto, para preparação e emergência. Não distribuir. |

## Slides

O deck é gerado por código: o que se edita é o conteúdo em Markdown, e o
`.pptx` é artefato de saída.

```bash
pip install python-pptx matplotlib pillow

python slides/scripts/figuras.py                                 # gera as figuras
python slides/scripts/build_deck.py slides/conteudo/aula-1.md    # monta .pptx e .pdf
python slides/scripts/conferir.py slides/saida/aula-1.pptx       # lint estrutural
```

A conferência precisa terminar em `0 alerta(s)`, e o PDF deve ser revisado antes
da sala: o lint pega texto demais e figura fora da margem, mas é cego para
marcação que vazou como texto ou rótulo estourando a caixa. Detalhes e checklist
de sala em [slides/README.md](slides/README.md).

## Requisito de cada bloco

Os blocos 1 a 5 da Aula 1 terminam obrigatoriamente com uma **âncora prática**:
uma frase de consequência imediata para o dia a dia — do tipo "por isso conversa
longa degrada" ou "por isso vale abrir sessão nova". É requisito, não enfeite: é
o que impede que a aula conceitual pareça teoria solta.

## Estado

- Aula 1: roteiro completo e deck gerado (`slides/saida/aula-1.pptx`).
- Aula 2: plano do instrutor, folha do aluno e gabarito completos. Deck curto
  ainda pendente.
