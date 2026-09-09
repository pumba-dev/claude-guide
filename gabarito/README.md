# Gabarito da prática — não distribuir aos alunos

Este diretório é **material do instrutor**. Os alunos constroem tudo isto do zero durante o Bloco P, conversando com o Claude Code. Entregar o gabarito pronto anularia a prática.

Ele serve para três coisas:

1. **Referência de qualidade.** É mais ou menos isto que deve sair da máquina do aluno. Se o que ele gerou está muito distante, você sabe onde intervir.
2. **Preparação.** Você roda a prática com este material antes da apresentação para cronometrar e testar o caminho sem busca na web.
3. **Rede de segurança.** Se a sala travar — rede caindo, contas sem acesso — você abre isto na sua máquina e conduz a discussão com um agente que funciona.

Roteiro da prática, do lado do aluno: [../docs/folha-do-aluno.md](../docs/folha-do-aluno.md).
Plano do instrutor: [../docs/pratica-guiada.md](../docs/pratica-guiada.md).

## O que tem aqui

```
gabarito/
├── CLAUDE.md                  <- orquestrador: laço, delegação, regras
├── edicoes/                   <- saída
└── .claude/skills/
    ├── curar-fontes/
    │   ├── SKILL.md           <- visita uma fonte, extrai itens da janela
    │   └── references/
    │       ├── fontes.md      <- as fontes do aluno
    │       └── criterios.md   <- o que entra e o que sai
    └── redigir-edicao/
        ├── SKILL.md           <- monta a edição a partir dos itens
        ├── references/
        │   └── tom.md         <- voz, tamanho, público
        └── assets/
            └── template.md    <- esqueleto da newsletter
```

## O que importa que o aluno reproduza

Não é o texto. É a **arquitetura**:

- o `CLAUDE.md` orquestra e **não** lê as fontes ele mesmo
- uma fonte por subagente, em paralelo
- o procedimento fica no `SKILL.md`, a configuração fica em `references/`
- item sem link não entra
- nada de agendamento: o agente é acionado sob demanda

Se essas cinco coisas aparecerem no que o aluno gerou, a prática funcionou, mesmo que a redação esteja diferente.
