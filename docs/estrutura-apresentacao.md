# Estrutura da apresentação

## Público

Mestrandos e pesquisadores em ciência da computação. Alta maturidade técnica em sistemas, protocolos e programação. Pouca ou nenhuma familiaridade com o funcionamento interno de LLMs e com ferramentas agênticas.

Idioma: **português do Brasil**. Termos técnicos em inglês podem ficar em inglês quando o equivalente em português for artificial (token, prompt, thinking, subagent).

## Objetivo pedagógico

Ao final, o aluno deve:

- (a) entender **por que** uma LLM se comporta como se comporta;
- (b) saber **operar** Claude Chat, Cowork e Code nos próprios projetos de pesquisa.

### Conceitos núcleo (obrigatórios)

1. **sessão**
2. **janela de contexto**
3. **modelos**
4. **thinking**
5. **effort**
6. **skills**
7. **references** — os arquivos de apoio de uma skill: `references/*.md`, `scripts/`, `assets/`. Material que o `SKILL.md` cita e que o modelo lê **apenas quando precisa**. É o mecanismo concreto de carregamento sob demanda (progressive disclosure): documentação longa custa quase nada de janela até ser aberta.
8. **subagents**
9. **agente orquestrador**

Toda a teoria existe para sustentar esses nove conceitos, e não o contrário. Os conceitos estão passíveis de mudanças e de adição de novos conceitos.

### Conceitos de apoio (aprovados como acréscimo)

Entram a serviço dos nove acima, nunca como tópico próprio:

| Conceito | Entra em | Para que serve na narrativa |
|---|---|---|
| prompt caching | Bloco 2 | Fecha o loop de "sessão = reenvio stateless": o reenvio existe, mas não custa linearmente. |
| compaction / auto-compact | Bloco 2 | O que o sistema faz quando a janela satura. Sem isso, sessão só aparece como problema. |
| contagem de tokens e custo real | Bloco 2 | Dá número ao "orçamento finito". |
| MCP | Bloco 3 | Tool use como protocolo cliente-servidor — a forma mais palpável do conceito para público de redes e sistemas. |
| permissões e sandbox | Bloco 3 | O portão do laço agir-observar. Gancho direto para dados sensíveis no Bloco 5. |
| hooks | Bloco 3 (menção) / Bloco 4 | Determinismo em torno de um núcleo estocástico. Liga-se a reprodutibilidade. |
| plan mode | Bloco 3 (menção) / Bloco P | Torna a etapa "planejar" do laço visível em sala. |
| agent teams / dispatch | Bloco 3 e 4 | Orquestrador como mecanismo real, não metáfora. |
| superfícies do Code (terminal, IDE, desktop, web) | Bloco 4 | Code não é uma coisa só. |
| projects e memória | Bloco 4 | Onde skills e material de apoio aparecem no Chat. |
| analytics, privacidade e uso de dados para treino | Bloco 5 | Sustenta a parte de dados sensíveis com fonte oficial, não com opinião. |

Fonte de consulta para todos: [claude-oficial-doc/](claude-oficial-doc/).

## Estrutura aprovada (abordagem bottom-up)

**Não reordene os blocos sem consultar o autor.** A ordem segue uma cadeia de dependências conceituais: token sustenta janela de contexto, que sustenta sessão, thinking e effort; tool use sustenta orquestrador e subagents.

| Bloco | Tempo | Conteúdo |
|---|---|---|
| 0 — Abertura | 3 min | Objetivo, mapa da sessão, o que cada um sai sabendo fazer. |
| 1 — Fundamentos de LLM | 12 min | Discriminativo vs. generativo; token como unidade de custo, limite e latência; predição do próximo token; intuição de atenção e Transformer, com o custo superlinear que origina o limite de contexto; pré-treino vs. post-training; amostragem e temperatura; três limitações estruturais (alucinação, data de corte, ausência de estado). |
| 2 — Anatomia de uma requisição | 14 min | O que é enviado ao modelo a cada turno; janela de contexto como orçamento finito, com números de custo e contagem de tokens; sessão como reenvio de histórico em um modelo stateless, com consequências em custo, latência e degradação; **prompt caching** como a razão de o reenvio ser viável; **compaction** como resposta do sistema à saturação; escolha de modelo como trade-off capacidade × latência × custo; thinking; effort. |
| 3 — Do sistema ao agente | 15 min | Tool use, apresentado via **MCP** como protocolo cliente-servidor; laço perceber-planejar-agir-observar; **permissões e sandbox** como o portão do laço; agente orquestrador; skills carregadas sob demanda; **references** (`references/`, `scripts/`, `assets/`) como o material que a skill abre só quando precisa; subagents e contextos isolados como solução para saturação de janela; menção rápida a **plan mode** e **hooks**. |
| 4 — Claude concreto | 9 min | Família de modelos; Chat, Cowork e Code como três interfaces sobre a mesma base conceitual; **superfícies do Code** (terminal, IDE, desktop, web); onde cada conceito do Bloco 3 aparece em cada produto — projects e memória no Chat, dispatch e agent teams no Cowork, skills, subagents e hooks no Code; tabela de "quando usar qual". |
| 5 — Aplicação em pesquisa de redes | 5 min | Código de simulação herdado, análise de capturas e logs, reprodutibilidade de experimentos, apoio à escrita; verificação obrigatória, dados sensíveis (com a política oficial de privacidade e uso de dados) e honestidade acadêmica. |
| 6 — Fechamento | 2 min | Fechamento e ponte para a prática. |
| P — Prática guiada | 30 min | 5 min de setup e verificação de ambiente; 10 min de exercício no Chat focado em sessão e janela de contexto; 12 min de exercício no Code sobre um repositório de exemplo, exercitando references, skills e subagents, com plan mode como passo visível; 3 min de debrief. |

## Requisito: âncora prática

Cada bloco de 1 a 5 **deve terminar com uma âncora prática**: uma frase de consequência imediata para o dia a dia do aluno, do tipo "por isso conversa longa degrada" ou "por isso vale abrir sessão nova".

Isso é requisito, não enfeite. É o que impede que os primeiros 30 minutos pareçam teoria solta.
