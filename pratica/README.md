# Prática guiada — newsletter semanal da sua área

Você vai montar um agente que busca o que saiu na **semana passada** na sua área de pesquisa e escreve uma newsletter em Markdown.

O agente não roda sozinho nem fica agendado. Você o aciona, ele trabalha e devolve o arquivo.

## O que já está pronto aqui

```
pratica/
├── CLAUDE.md                  <- o orquestrador. Leia, é o cérebro da prática
├── edicoes/                   <- onde as edições geradas vão parar
└── .claude/skills/
    ├── curar-fontes/
    │   ├── SKILL.md           <- como visitar uma fonte e o que extrair
    │   └── references/
    │       ├── fontes.md      <- VOCÊ PREENCHE. Suas fontes
    │       └── criterios.md   <- o que entra e o que sai da edição
    └── redigir-edicao/
        ├── SKILL.md           <- como montar a edição a partir dos itens
        ├── references/
        │   └── tom.md         <- VOCÊ AJUSTA. Voz e formato
        └── assets/
            └── template.md    <- esqueleto da newsletter
```

Dois arquivos são seus: `fontes.md` e `tom.md`. O resto funciona sem você tocar.

## Passo a passo

### 1. Abra o Claude Code nesta pasta

```bash
cd pratica
claude
```

Rode `/context` antes de qualquer outra coisa. Olhe o que já está ocupando a janela **sem você ter pedido nada**: system prompt, `CLAUDE.md`, descrições das skills. Anote o número.

### 2. Preencha suas fontes

Abra `.claude/skills/curar-fontes/references/fontes.md` e coloque de 4 a 6 fontes da **sua** área: blogs de grupos de pesquisa, páginas de novidades de ferramentas que você usa, portais de notícia técnica, feeds de conferência.

Prefira URLs de páginas que listam publicações recentes, não a home institucional.

Este arquivo é a razão de a edição de cada pessoa da sala sair diferente com a mesma skill.

### 3. Ajuste o critério, se quiser

`.claude/skills/curar-fontes/references/criterios.md` define o que conta como relevante. Está genérico de propósito. Aperte ou solte conforme a sua área.

### 4. Acione o agente

No Claude Code:

```
Gere a edição desta semana.
```

Só isso. O `CLAUDE.md` já diz ao orquestrador o que fazer.

Enquanto roda, observe: ele abre um subagente por fonte. Cada subagente lê a página inteira dentro do contexto **dele**, e devolve ao principal apenas os itens.

### 5. Verifique

Abra dois links da edição gerada. Confira se a data está dentro da semana passada e se o resumo bate com o que a página diz.

Se algum item não tiver link, ou o link não abrir, o agente errou — e é exatamente isso que você precisa ver acontecer uma vez.

### 6. Mude o tom, não a skill

Edite `references/tom.md` (por exemplo: de "técnico e seco" para "explicando para calouro") e peça:

```
Reescreva a edição desta semana com o tom atualizado.
```

Nenhuma linha de skill mudou. Só o material de apoio.

### 7. Feche olhando o contexto

Rode `/context` de novo e compare com o número do passo 1. Quanto custou tudo isso no contexto principal?

## Se a busca na web não estiver disponível

Nem toda conta tem busca. Não tem problema: se `fontes.md` tiver URLs explícitas, o agente busca as páginas diretamente. É por isso que o arquivo pede URLs, e não nomes de sites.
