# Estrutura da apresentação

## Público

Mestrandos e pesquisadores em ciência da computação. Alta maturidade técnica em sistemas, protocolos e programação. Pouca ou nenhuma familiaridade com o funcionamento interno de LLMs e com ferramentas agênticas.

Idioma: **português do Brasil**. Termos técnicos em inglês podem ficar em inglês quando o equivalente em português for artificial (token, prompt, thinking, subagent).

## Objetivo pedagógico

Ao final, o aluno deve:

- (a) entender **por que** uma LLM se comporta como se comporta;
- (b) saber **operar** Claude Chat, Cowork e Code nos próprios projetos de pesquisa.

## Conceitos núcleo

Doze conceitos, em três camadas. As camadas são mnemônicas e respondem a três perguntas: o que o modelo vê, como ele responde, o que ele consegue fazer. Toda a teoria existe para sustentá-los, e não o contrário.

### Camada A — o que o modelo vê

1. **janela de contexto** — orçamento finito de tokens por requisição.
2. **sessão** — reenvio do histórico a cada turno em um modelo stateless. Origem do custo, da latência crescente e da degradação.
3. **contexto persistente** — o que atravessa sessões: `CLAUDE.md` no Code, Projects e memória no Chat. Entra **sempre**, ao contrário das references. É a alavanca mais barata e de maior retorno: evita reexplicar o projeto a cada sessão.

### Camada B — como ele responde

4. **modelos** — trade-off capacidade × latência × custo; família Claude e critério de escolha.
5. **thinking e effort** — controle do esforço de raciocínio. Tratados como um conceito só, em duas granularidades: ligar o raciocínio explícito e regular quanto dele investir.

### Camada C — o que ele consegue fazer

6. **tool use / MCP e connectors** — a fronteira entre chatbot e agente. Protocolo cliente-servidor que dá ao modelo acesso a arquivos, comandos e sistemas externos. Sem ele, orquestrador e subagents não têm o que orquestrar.
7. **skills** — procedimentos empacotados, carregados sob demanda.
8. **references** — arquivos de apoio de uma skill: `references/*.md`, `scripts/`, `assets/`. Material que o `SKILL.md` cita e que o modelo lê **apenas quando precisa** (progressive disclosure). Documentação longa custa quase nada de janela até ser aberta.
9. **subagents** — contextos isolados, executando em paralelo, como resposta à saturação da janela.
10. **agente orquestrador** — o laço perceber-planejar-agir-observar coordenando ferramentas, skills e subagents.

### Transversal

11. **permissões e modos de execução** (incl. plan mode) — contraparte obrigatória do tool use: o portão do laço agir-observar. Apresentado no Bloco 5, junto de dados sensíveis, onde é consequência prática e não mais um mecanismo.
12. **verificação** — o único conceito que não é feature. Uma LLM produz saída plausível por construção; sem transformar conferência em hábito operacional, o aluno usa toda a capacidade e publica errado.

Os conceitos estão passíveis de mudanças e de adição de novos conceitos.

## Conceitos de apoio

Entram a serviço dos doze acima, nunca como tópico próprio:

| Conceito | Entra em | Para que serve na narrativa |
|---|---|---|
| prompt caching | Bloco 2 | Fecha o loop de "sessão = reenvio stateless": o reenvio existe, mas não custa linearmente. |
| compaction / auto-compact | Bloco 2 | O que o sistema faz quando a janela satura. Sem isso, sessão só aparece como problema. |
| contagem de tokens e custo real | Bloco 2 | Dá número ao "orçamento finito". |
| hooks | Bloco 4 (menção) | Determinismo em torno de um núcleo estocástico; liga-se a reprodutibilidade. Poder alto, público errado para 60 min. |
| agent teams / dispatch | Bloco 4 | Caso particular de orquestrador. Exemplo, não conceito. |
| checkpointing | Bloco 4 (menção) | Conforto operacional, não capacidade nova. |
| superfícies do Code (terminal, IDE, desktop, web) | Bloco 4 | Code não é uma coisa só. |
| analytics, privacidade e uso de dados para treino | Bloco 5 | Sustenta a parte de dados sensíveis com fonte oficial, não com opinião. |

Fonte de consulta para todos: [claude-oficial-doc/](claude-oficial-doc/).

## Estrutura aprovada (abordagem bottom-up)

**Não reordene os blocos sem consultar o autor.** A ordem segue uma cadeia de dependências conceituais: token sustenta janela de contexto, que sustenta sessão, thinking e effort; tool use sustenta orquestrador e subagents.

| Bloco | Tempo | Conteúdo |
|---|---|---|
| 0 — Abertura | 3 min | Objetivo, mapa da sessão, o que cada um sai sabendo fazer. |
| 1 — Fundamentos de LLM | 12 min | Discriminativo vs. generativo; token como unidade de custo, limite e latência; predição do próximo token; intuição de atenção e Transformer, com o custo superlinear que origina o limite de contexto; pré-treino vs. post-training; amostragem e temperatura; três limitações estruturais (alucinação, data de corte, ausência de estado). |
| 2 — Anatomia de uma requisição | 14 min | O que é enviado ao modelo a cada turno; janela de contexto como orçamento finito, com números de custo e contagem de tokens; sessão como reenvio de histórico em um modelo stateless, com consequências em custo, latência e degradação; prompt caching como a razão de o reenvio ser viável; compaction como resposta do sistema à saturação; contexto persistente (CLAUDE.md, Projects, memória) como o que atravessa sessões; escolha de modelo; thinking e effort. |
| 3 — Do sistema ao agente | 15 min | Tool use apresentado via MCP e connectors, como protocolo cliente-servidor; laço perceber-planejar-agir-observar; agente orquestrador; skills carregadas sob demanda; references (`references/`, `scripts/`, `assets/`) como o material que a skill abre só quando precisa; subagents e contextos isolados como solução para saturação de janela. |
| 4 — Claude concreto | 9 min | Família de modelos; Chat, Cowork e Code como três interfaces sobre a mesma base conceitual; superfícies do Code (terminal, IDE, desktop, web); onde cada conceito da Camada C aparece em cada produto — Projects e memória no Chat, dispatch e agent teams no Cowork, skills, subagents, hooks e checkpointing no Code; tabela de "quando usar qual". |
| 5 — Aplicação em pesquisa de redes | 5 min | Código de simulação herdado, análise de capturas e logs, reprodutibilidade de experimentos, apoio à escrita; **permissões e modos de execução (incl. plan mode)** como portão do agente sobre um repositório real; verificação obrigatória, dados sensíveis (com a política oficial de privacidade e uso de dados) e honestidade acadêmica. |
| 6 — Fechamento | 2 min | Fechamento e ponte para a prática. |
| P — Prática guiada | 30 min | 5 min de setup e verificação de ambiente; 10 min de exercício no Chat focado em sessão e janela de contexto; 12 min de exercício no Code sobre um repositório de exemplo, exercitando references, skills e subagents, com plan mode como passo visível; 3 min de debrief. |

## Roteiro detalhado

O detalhamento minutado de cada bloco, com o que mostrar e a âncora prática de cada um, está em [roteiro-blocos.md](roteiro-blocos.md).

## Requisito: âncora prática

Cada bloco de 1 a 5 **deve terminar com uma âncora prática**: uma frase de consequência imediata para o dia a dia do aluno, do tipo "por isso conversa longa degrada" ou "por isso vale abrir sessão nova".

Isso é requisito, não enfeite. É o que impede que os primeiros 30 minutos pareçam teoria solta.
