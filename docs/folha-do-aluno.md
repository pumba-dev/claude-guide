# Folha do aluno — construa seu agente de newsletter

Você vai montar, do zero, um agente que busca o que saiu na **semana passada** na sua área e escreve uma newsletter.

Você não vai escrever os arquivos à mão. Você vai pedir ao Claude Code que os escreva — e é esse o ponto: `CLAUDE.md` e skills são arquivos de texto, e o agente sabe produzi-los.

Nada aqui fica agendado. O agente é acionado por você e para quando termina.

---

## 0. Preparar (2 min)

```bash
mkdir newsletter && cd newsletter
claude
```

Antes de pedir qualquer coisa, rode:

```
/context
```

**Anote o número.** Você ainda não pediu nada e a janela já tem conteúdo. Vamos comparar no final.

---

## 1. Criar o orquestrador (5 min)

Peça, com suas palavras ou copiando:

> Crie um arquivo CLAUDE.md que faça de você o orquestrador de uma newsletter semanal da minha área de pesquisa.
>
> O laço deve ser: calcular a janela da semana anterior a partir da data atual do sistema; ler minha lista de fontes; abrir **um subagente por fonte**, todos em paralelo, para que a leitura das páginas aconteça no contexto deles e não no principal; consolidar os itens que voltarem, removendo duplicatas e o que estiver fora da janela; mandar redigir a edição; e me relatar o que entrou e o que foi descartado.
>
> Regras: nunca inventar item ou link; item sem link verificável não entra; fonte sem novidade na janela é resultado válido; não criar nenhum agendamento ou tarefa recorrente.

Quando ele terminar, **leia o arquivo**. Você entende cada passo? Tem algo ali que você não pediu?

Checkpoint: existe um `CLAUDE.md` e ele descreve delegação, não execução direta.

---

## 2. Criar as skills (6 min)

> Crie duas skills neste projeto.
>
> A primeira, `curar-fontes`: visita **uma** fonte e devolve só os itens publicados dentro da janela, em formato fixo, com título, data, link direto, fonte e um resumo de no máximo duas linhas. Os critérios do que é relevante devem ficar em um arquivo de referência separado, não dentro da skill. Se a fonte não tiver nada na janela, ela devolve exatamente isso.
>
> A segunda, `redigir-edicao`: recebe os itens já consolidados e monta a edição em Markdown. Ela não busca nada. O modelo da edição e o tom da escrita ficam em arquivos separados, fora da skill.
>
> Crie também um arquivo de referência onde eu vou listar minhas fontes.

Checkpoint: você tem duas pastas de skill, cada uma com um `SKILL.md` **curto** e arquivos de apoio ao lado.

Pergunte a si mesmo: por que os critérios e o tom ficaram fora do `SKILL.md`?

---

## 3. Colocar suas fontes (4 min)

Abra o arquivo de fontes que ele criou e coloque **de 4 a 6 fontes suas**: blog de grupo de pesquisa, página de novidades de uma ferramenta que você usa, portal de notícia técnica, chamada de conferência.

Duas regras que evitam frustração:

- use a URL da página que **lista coisas recentes**, não a home institucional
- fonte que exige login não vai funcionar; troque por uma aberta

Este arquivo é o motivo de a edição de cada pessoa da sala sair diferente com o mesmo agente.

---

## 4. Acionar (8 min)

```
Gere a edição desta semana.
```

Enquanto roda, observe:

- ele declarou a janela de datas antes de começar? Está certa?
- quantos subagentes abriram? Um por fonte?
- o que voltou de cada subagente: a página inteira ou só os itens?

---

## 5. Verificar (4 min)

Abra **dois links** da edição.

- a data está dentro da janela?
- o resumo bate com o que a página diz?
- algum item ficou sem link?

Se achar um item errado, guarde — vai ser discutido no fechamento. Achar um erro aqui vale mais que a edição sair perfeita.

---

## 6. Fechar (1 min)

```
/context
```

Compare com o número do passo 0. Quanto custou tudo isso? E quanto teria custado se as páginas tivessem sido lidas no contexto principal?

---

## Se sobrar tempo

Mude o tom no arquivo de referência — por exemplo, de técnico para "explicando para um calouro" — e peça a reescrita da edição.

Repare no que você **não** precisou tocar: nenhuma skill.

---

## Se algo travar

| Problema | O que fazer |
|---|---|
| Busca na web não disponível | Garanta que suas fontes estão como URLs completas. O agente busca as páginas direto. |
| Uma fonte não abre | Deixe. `nada na janela` ou `fonte inacessível` é resultado válido. |
| Nenhuma fonte rendeu nada | Peça ao instrutor uma das URLs de reserva. |
| O agente quer criar agendamento | Diga que não: este agente é acionado sob demanda. |
| Ficou para trás | Junte-se a quem está ao lado. A prática funciona em dupla. |
