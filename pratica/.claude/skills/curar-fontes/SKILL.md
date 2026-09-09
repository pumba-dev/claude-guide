---
name: curar-fontes
description: Visita uma fonte da web e extrai os itens publicados na janela de tempo indicada, no formato padrão da newsletter. Use ao cobrir uma fonte para a edição semanal.
---

# Curar uma fonte

Você cobre **uma** fonte por vez. O orquestrador diz qual e qual a janela de datas.

## Procedimento

1. Abra a URL da fonte.
   - Se a busca na web estiver disponível, você pode complementar com uma busca restrita ao domínio da fonte.
   - Se a página não abrir, registre `fonte inacessível` e encerre. Não substitua por outra fonte.

2. Localize os itens publicados **dentro da janela**. Se a página não mostra datas, procure a data no próprio item. Item sem data verificável é descartado.

3. Aplique os critérios de [references/criterios.md](references/criterios.md).

4. Devolva os itens aprovados no formato abaixo. Nada além disso — sem introdução, sem comentário, sem resumo do seu trabalho.

## Formato de saída

```
- titulo: <título do item, como está na fonte>
  data: AAAA-MM-DD
  link: <URL direta do item, não da home da fonte>
  fonte: <nome da fonte>
  resumo: <2 linhas, no máximo. O que é e por que importa.>
  tipo: <notícia | release | publicação | evento>
```

Se nada da fonte se qualificar, devolva exatamente:

```
- nada na janela
```

## Regras

**Nunca invente item, data ou link.** Este é o erro mais grave possível aqui. Uma fonte vazia é um resultado correto; um item inventado contamina a edição inteira.

**O resumo descreve o que a página diz**, não o que você sabe sobre o assunto. Se a página é curta demais para sustentar duas linhas, escreva uma.

**Link direto.** Link para a home da fonte não serve — o leitor precisa chegar no item.

**Máximo de 4 itens por fonte.** Se houver mais, fique com os 4 mais relevantes segundo os critérios.
