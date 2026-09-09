# Estrutura da apresentação

## Público

Mestrandos e pesquisadores em ciência da computação. Alta maturidade técnica em sistemas, protocolos e programação. Pouca ou nenhuma familiaridade com o funcionamento interno de LLMs e com ferramentas agênticas.

Idioma: **português do Brasil**. Termos técnicos em inglês podem ficar em inglês quando o equivalente em português for artificial (token, prompt, thinking, subagent).

## Objetivo pedagógico

Ao final, o aluno deve:

- (a) entender **por que** uma LLM se comporta como se comporta;
- (b) saber **operar** Claude Chat, Cowork e Code nos próprios projetos de pesquisa.

Conceitos operacionais obrigatórios (núcleo da apresentação):

1. sessão
2. janela de contexto
3. modelos
4. thinking
5. effort
6. skills
7. references
8. subagents
9. agente orquestrador

Toda a teoria existe para sustentar esses nove conceitos, e não o contrário. Os conceitos estão passíveis de mudanças e de adição de novos conceitos.

## Estrutura aprovada (abordagem bottom-up)

**Não reordene os blocos sem consultar o autor.** A ordem segue uma cadeia de dependências conceituais: token sustenta janela de contexto, que sustenta sessão, thinking e effort; tool use sustenta orquestrador e subagents.

| Bloco | Tempo | Conteúdo |
|---|---|---|
| 0 — Abertura | 3 min | Objetivo, mapa da sessão, o que cada um sai sabendo fazer. |
| 1 — Fundamentos de LLM | 12 min | Discriminativo vs. generativo; token como unidade de custo, limite e latência; predição do próximo token; intuição de atenção e Transformer, com o custo superlinear que origina o limite de contexto; pré-treino vs. post-training; amostragem e temperatura; três limitações estruturais (alucinação, data de corte, ausência de estado). |
| 2 — Anatomia de uma requisição | 14 min | O que é enviado ao modelo a cada turno; janela de contexto como orçamento finito; sessão como reenvio de histórico em um modelo stateless, com consequências em custo, latência e degradação; escolha de modelo como trade-off capacidade × latência × custo; thinking; effort. |
| 3 — Do sistema ao agente | 15 min | Tool use; laço perceber-planejar-agir-observar; agente orquestrador; references; skills carregadas sob demanda; subagents e contextos isolados como solução para saturação de janela. |
| 4 — Claude concreto | 9 min | Família de modelos; Chat, Cowork e Code como três interfaces sobre a mesma base conceitual; onde cada conceito do Bloco 3 aparece em cada produto; tabela de "quando usar qual". |
| 5 — Aplicação em pesquisa de redes | 5 min | Código de simulação herdado, análise de capturas e logs, reprodutibilidade de experimentos, apoio à escrita; verificação obrigatória, dados sensíveis e honestidade acadêmica. |
| 6 — Fechamento | 2 min | Fechamento e ponte para a prática. |
| P — Prática guiada | 30 min | 5 min de setup e verificação de ambiente; 10 min de exercício no Chat focado em sessão e janela de contexto; 12 min de exercício no Code sobre um repositório de exemplo, exercitando references, skills e subagents; 3 min de debrief. |

## Requisito: âncora prática

Cada bloco de 1 a 5 **deve terminar com uma âncora prática**: uma frase de consequência imediata para o dia a dia do aluno, do tipo "por isso conversa longa degrada" ou "por isso vale abrir sessão nova".

Isso é requisito, não enfeite. É o que impede que os primeiros 30 minutos pareçam teoria solta.
