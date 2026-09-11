# Roteiro bloco a bloco — Aula 1

Detalhamento dos blocos 0 a 6, que compõem a **Aula 1 (~63 min, conceitual)**, definidos em [estrutura-apresentacao.md](estrutura-apresentacao.md). A ordem dos blocos é aprovada e não muda sem consultar o autor. Os tempos são estimativa de planejamento: dimensionam o conteúdo e orientam o que cortar sob pressão, mas o ritmo real acompanha a absorção da turma.

A **Aula 2 (60 min, prática)** tem plano próprio em [pratica-guiada.md](pratica-guiada.md), com a folha de prompts do aluno em [folha-do-aluno.md](folha-do-aluno.md).

Convenção de cada bloco: **objetivo** (o que o aluno leva), **roteiro minutado**, **o que mostrar**, **âncora prática** (obrigatória nos blocos 1 a 5), **fontes** no espelho [claude-oficial-doc/](claude-oficial-doc/).

---

## Bloco 0 — Abertura (3 min)

**Objetivo:** estabelecer contrato de expectativa. Não é palestra de futurologia nem tutorial de prompt.

| Min | Tópico |
|---|---|
| 0–1 | Quem sou, por que este formato: uma aula de "por quê" e outra, inteira, de mão na massa. |
| 1–2 | A promessa concreta: ao final das duas aulas você abre o Claude no seu próprio projeto e sabe o que está acontecendo em cada camada. |
| 2–3 | Mapa da sessão: mostrar a pirâmide de dependências (token → janela → sessão → agente) e dizer que a ordem é obrigatória, não estética. |

**O que mostrar:** um slide único com a cadeia de dependências. Ele reaparece no início de cada bloco com o item atual destacado — é a barra de progresso conceitual da apresentação.

**Frase de abertura sugerida:** "Vocês já sabem ler um paper e já sabem programar. O que falta é saber o que acontece entre apertar Enter e a resposta aparecer. Nesta aula a gente abre essa caixa. Na próxima, vocês operam ela."

---

## Bloco 1 — Fundamentos de LLM (12 min)

**Objetivo:** o aluno consegue explicar por que o modelo alucina, por que tem data de corte e por que não lembra de nada — a partir do mecanismo, não de analogia.

| Min | Tópico | Tratamento |
|---|---|---|
| 0–2 | Discriminativo vs. generativo | Público conhece classificador. Ponte: classificador estima P(classe dada a entrada); LLM estima P(próximo token dados os anteriores). Mesma família, objetivo diferente. |
| 2–4 | Token como unidade | Não é palavra nem caractere. É a unidade de **custo**, de **limite** e de **latência** — as três coisas que o aluno vai sentir no bolso e no relógio. Mostrar tokenização de um texto em português vs. inglês: português gasta mais tokens, fato relevante para o público. |
| 4–6 | Predição do próximo token | Autoregressão. O modelo não sabe a resposta antes de gerar; constrói token a token. Consequência que já planta a alucinação: nunca há um passo em que ele consulta uma base de fatos. |
| 6–9 | Atenção e Transformer | Intuição, sem matriz: cada token olha para todos os outros para decidir o que importa. Todo par de tokens é considerado, então o **custo cresce de forma superlinear com o comprimento**. Esta é a origem física do limite de contexto. Não é decisão comercial. |
| 9–10.5 | Pré-treino vs. post-training | Pré-treino: prever texto. Post-training: virar assistente útil e seguro. Explica por que o modelo tem preferências de formato que ninguém programou explicitamente. |
| 10.5–11.5 | Amostragem e temperatura | Mesmo prompt, saídas diferentes. Menção rápida — o que importa é a consequência: **não é reprodutível por construção**, e isso volta no Bloco 5. |
| 11.5–12 | Três limitações estruturais | (1) alucinação: gera plausível, não verdadeiro; (2) data de corte: não conhece o que veio depois; (3) ausência de estado: cada requisição começa do zero. As três decorrem do que foi visto, não são bugs. |

**O que mostrar:** tokenizador ao vivo com uma frase em PT e a mesma em EN, contando tokens. Maior retorno visual do bloco.

**Âncora prática:** *"O modelo não busca, ele completa. Por isso toda saída que você for citar em um paper precisa ser verificada por você — e por isso escrever em português custa mais caro que em inglês."*

---

## Bloco 2 — Anatomia de uma requisição (17 min)

**Objetivo:** o aluno descobre que fala com uma aplicação, não com o modelo; entende o que é enviado a cada turno; e passa a enxergar a janela como orçamento que ele administra.

| Min | Tópico | Tratamento |
|---|---|---|
| 0–3 | **Harness: você não conversa com o modelo** | Abrir o bloco respondendo à pergunta que o Bloco 1 deixou: se o modelo não guarda estado e não executa nada, quem faz o resto? O harness — Claude Code, Chat e Cowork são harnesses; o modelo está dentro deles. Ele monta a requisição, injeta system prompt, `CLAUDE.md` e descrições de skills, reenvia o histórico, executa a ferramenta que o modelo pediu, aplica permissões, compacta e abre subagentes. O modelo recebe texto e devolve texto; o resto é tudo harness. Termo oficial, não apelido: [code/glossary.md](claude-oficial-doc/code/glossary.md). |
| 3–6 | O que é enviado a cada turno | Desmontar uma requisição real: system prompt, memória, informação de ambiente, descrições de skills, `CLAUDE.md`, e só então o prompt do usuário. Números do simulador oficial: system prompt cerca de 4.200 tokens, `CLAUDE.md` de projeto cerca de 1.800, descrições de skills cerca de 450, ferramentas MCP diferidas cerca de 120. O prompt do aluno: cerca de 45. **A maior parte do que o modelo lê não foi escrita naquele turno.** |
| 6–8.5 | Janela como orçamento finito | 200 mil tokens de padrão; 1 milhão em modelos com janela estendida. Não é quanto ele lembra, é quanto cabe **nesta** requisição. Cada leitura de arquivo debita: um arquivo médio custa entre 1.100 e 2.400 tokens. |
| 8.5–11 | Sessão em modelo stateless | O modelo não guarda nada. A conversa existe porque o harness reenvia todo o histórico a cada turno. Consequências em cascata: custo cresce, latência cresce, e a janela enche até o conteúdo relevante competir com ruído acumulado. |
| 11–12.5 | Prompt caching | Contrapeso honesto: o reenvio existe, mas o prefixo repetido é cacheado e sai muito mais barato que a primeira vez. Sem isso a conta explodiria. Com isso, sessão longa é cara em janela, não tanto em dinheiro. |
| 12.5–14 | Compaction | Quando a janela satura, o harness resume a conversa e recomeça — o resumo fica em torno de 12% do que havia. É salva-vidas, não é grátis: o que foi resumido perdeu detalhe. Daí a decisão consciente entre compactar e abrir sessão nova. |
| 14–15.5 | Contexto persistente | O que atravessa sessões: `CLAUDE.md` no Code, Projects e memória no Chat. Entra **sempre**, em toda requisição. Por isso é caro escrever demais nele — e é a alavanca de maior retorno quando bem escrito. |
| 15.5–17 | Modelos, thinking e effort | Escolha de modelo: capacidade × latência × custo. Thinking: o modelo gera raciocínio antes da resposta, e esse raciocínio também são tokens. Effort (`low`, `medium`, `high`, `xhigh`, `max`; padrão `high`): quanto desse raciocínio investir. Regra prática: tarefa mecânica com effort alto é dinheiro e tempo jogados fora; tarefa de projeto com effort baixo é retrabalho. |

**O que mostrar:** o simulador de janela de contexto da doc oficial ([code/context-window.md](claude-oficial-doc/code/context-window.md)), ou uma reprodução dele em slide: barra de 200k enchendo item a item. Slide mais importante da aula.

**Âncora prática:** *"Conversa longa degrada porque o histórico inteiro volta a cada turno e vai empurrando o que importa para o meio do ruído. Por isso vale abrir sessão nova quando o assunto muda — e por isso vale escrever o `CLAUDE.md` uma vez em vez de reexplicar o projeto toda vez."*

---

## Bloco 3 — Do sistema ao agente (15 min)

**Objetivo:** o aluno entende como um modelo que só prevê texto passa a executar trabalho, e conhece as quatro alavancas que ele mesmo controla: MCP, skills, references e subagents.

| Min | Tópico | Tratamento |
|---|---|---|
| 0–3 | Tool use via MCP | Abrir por aqui, não por tool use abstrato. MCP é protocolo cliente-servidor: o servidor expõe ferramentas com nome, descrição e schema; o harness injeta essa lista no contexto; o modelo responde pedindo uma chamada; o harness executa e devolve o resultado. **O modelo nunca executa nada — ele pede.** Para este público, essa é a frase que destrava tudo. |
| 3–5 | O laço | Perceber, planejar, agir, observar, repetir. Desenhar o laço e mapear cada etapa no que acabou de ser descrito. O laço encerra quando o modelo devolve texto em vez de pedir ferramenta. |
| 5–7 | Agente orquestrador | Quem roda o laço. Mantém o objetivo, decide qual ferramenta chamar, quando delegar e quando parar. É o papel, não um produto. |
| 7–9.5 | Skills | Procedimento empacotado: um `SKILL.md` com nome, descrição e instruções. **O truque está no custo:** só a descrição fica em contexto (cerca de 450 tokens para o conjunto); o corpo carrega quando a skill é usada. Comparação direta com `CLAUDE.md`, que entra sempre. |
| 9.5–11.5 | References | Os arquivos de apoio da skill: `references/*.md`, `scripts/`, `assets/`. O `SKILL.md` cita e diz quando abrir; o modelo lê **só quando precisa**. Exemplo do público: uma skill de análise de captura com `references/formato-pcap.md` e `scripts/parse.py` — quarenta páginas de referência custam zero até o dia em que fazem falta. Script é **executado**, não lido: custo de contexto ainda menor. |
| 11.5–14 | Subagents | Contexto isolado, com janela própria, que devolve só o resultado. Números do simulador: abrir um subagente custa cerca de 80 tokens no contexto principal e ele devolve cerca de 420. As leituras de arquivo que ele fez por dentro custam **zero** no principal. É a resposta direta ao problema do Bloco 2. |
| 14–15 | Fechamento do bloco | Reamarrar: MCP dá capacidade, skills dão procedimento, references dão material sob demanda, subagents dão janela extra. As quatro alavancas são do aluno, não do fornecedor. |

**O que mostrar:** o laço desenhado e, ao lado, o mesmo laço com os números de token do subagente — a economia fica visível em vez de assertiva.

**Âncora prática:** *"Contexto é o recurso escasso, e você tem três formas de gastá-lo menos: skill em vez de repetir instrução, reference em vez de colar documentação, subagente em vez de ler dez arquivos no contexto principal."*

---

## Bloco 4 — Claude concreto (9 min)

**Objetivo:** o aluno sai sabendo qual porta abrir para qual tarefa e reconhece que os conceitos do Bloco 3 são os mesmos nos três produtos.

| Min | Tópico | Tratamento |
|---|---|---|
| 0–2 | Família de modelos | Opus, Sonnet, Haiku e o critério de escolha. Aliases e janela estendida para sessões longas. Ponto honesto: nomes mudam, o critério capacidade × latência × custo não. |
| 2–3.5 | Chat | Conversa, Projects, memória, connectors. É onde o pesquisador começa: leitura de paper, exploração de ideia, escrita. Aqui contexto persistente tem cara de Project. |
| 3.5–5 | Cowork | Trabalho delegado sobre arquivos e tarefas, com dispatch e agent teams. É o orquestrador do Bloco 3 com interface: vários agentes em paralelo sobre o mesmo material. |
| 5–7 | Code | Agente no repositório. Quatro superfícies: terminal, IDE, desktop e web. Aqui aparecem `CLAUDE.md`, skills, references, subagents, hooks e checkpointing. Menção rápida: hooks executam comando determinístico em torno do modelo — gancho para reprodutibilidade no Bloco 5; checkpointing permite desfazer o que o agente fez. |
| 7–9 | Tabela "quando usar qual" | Matriz conceito × produto, preenchida ao vivo: onde cada um dos treze conceitos aparece em Chat, Cowork e Code. Começar pela primeira linha, o harness: os três produtos são harnesses diferentes sobre o mesmo modelo. Slide de referência, o aluno fotografa. |

**O que mostrar:** a matriz conceito × produto. É o artefato que o aluno leva embora.

**Âncora prática:** *"Não é escolher entre três produtos. É a mesma base conceitual com três portas: pensar no Chat, delegar no Cowork, executar no repositório com o Code."*

---

## Bloco 5 — Aplicação em pesquisa em computação (5 min)

**Objetivo:** o aluno vê os conceitos aplicados ao trabalho dele e sai com regras de conduta claras. Bloco denso: cortar exemplo antes de cortar regra.

**Princípio de generalidade:** o laboratório tem projetos muito diferentes — redes ópticas elásticas, aplicações em educação e saúde, revisões bibliográficas. O bloco **não é organizado por domínio, e sim por tipo de trabalho**, porque as quatro atividades abaixo aparecem em todos eles. Cada atividade é apresentada com um exemplo neutro e um segundo exemplo tirado de um domínio diferente, para que ninguém precise traduzir mentalmente do domínio alheio para o seu.

| Min | Tópico | Tratamento |
|---|---|---|
| 0–1.5 | Quatro tipos de trabalho, não quatro domínios | (1) **Entender artefato herdado**: simulador que o aluno anterior deixou, pipeline de dados, protótipo de aplicação — o problema é sempre código sem quem o explique. (2) **Analisar resultado experimental**: saída de simulação, log, captura, planilha de coleta, resposta de questionário — o problema é sempre volume acima da leitura manual. (3) **Levantar e organizar literatura**: triagem de artigos, extração de critérios, montagem de tabela comparativa em revisão sistemática — com a ressalva de que o modelo **não é fonte bibliográfica**, e sim ferramenta de organização sobre textos que você forneceu. (4) **Apoiar a escrita**: estrutura, clareza, revisão de argumento. Um exemplo curto cada, sem demo. Atravessando os quatro: **reprodutibilidade** — o que o agente fez precisa virar script, commit e ambiente registrados, senão o experimento não volta. É aqui que hooks reaparecem, como o jeito determinístico de garantir isso em torno de um modelo que não é determinístico (Bloco 1). |
| 1.5–3 | Permissões e plan mode | Um agente com acesso ao repositório edita arquivos e roda comandos. Quem pede aprovação é o **harness**, não o modelo: o portão está fora do componente estocástico, e é por isso que ele é confiável. Modos de permissão definem o portão: pedir aprovação, aceitar edições, ou plan mode — o agente **planeja e mostra antes de agir**. Regra: repositório de terceiro, base de coleta ou qualquer artefato que você não pode recriar começa em plan mode. |
| 3–4 | Dados sensíveis | Duas categorias distintas. **Dado técnico:** credencial, chave, endereço de infraestrutura, captura com identificador de rede. **Dado de pessoa:** o que aparece em projeto de educação e de saúde — registro de aluno, prontuário, resposta de questionário, qualquer coisa sob TCLE ou aprovação de comitê de ética. Para a segunda categoria a régua não é o que a ferramenta permite, é o que o protocolo de pesquisa e a LGPD permitem: se o consentimento não previu processamento por serviço de terceiro, o dado não sai da máquina. Citar a política oficial de privacidade e uso de dados em vez de opinar. |
| 4–5 | Verificação e honestidade acadêmica | Saída plausível não é saída correta — o Bloco 1 já provou. O que o modelo produz é rascunho até você rodar, conferir e reproduzir. Duas armadilhas específicas: referência bibliográfica inventada com aparência perfeita, e resultado numérico produzido sem executar nada. Declarar uso conforme a norma do programa e do veículo. Nada assinado por você entra sem você ter verificado. |

**Âncora prática:** *"O agente acelera a parte mecânica e não assume nenhuma responsabilidade. A assinatura no paper é sua, então a verificação também é — e o dado que saiu do seu computador não volta."*

---

## Bloco 6 — Fechamento e ponte (2 min)

| Min | Tópico |
|---|---|
| 0–1 | Retomar a pirâmide de dependências completa, agora com os treze conceitos posicionados, e fechar nomeando o harness como a caixa onde todos eles acontecem. Uma frase por camada. |
| 1–2 | Ponte para a Aula 2: o que vai ser construído, e a tarefa de preparação — instalar o Claude Code e chegar com 4 a 6 fontes da própria área rascunhadas. Dizer que quem chegar sem isso perde os primeiros 15 minutos. |

---

## Aula 2

A prática tem plano próprio, com roteiro minutado de 60 min, o que dizer em cada momento, plano de degradação e riscos: [pratica-guiada.md](pratica-guiada.md).

Em uma linha: em pasta vazia, o aluno pede ao agente que escreva o `CLAUDE.md` do orquestrador, as duas skills e os arquivos de `references/`; coloca as próprias fontes; aciona sob demanda; verifica os links; e troca o tom pelo arquivo de apoio sem tocar em nenhuma skill.

**Conceitos exercitados:** janela de contexto, sessão, contexto persistente, skills, references, subagents, orquestrador, tool use e verificação. Ficam de fora, como observação e não como exercício: modelos, thinking/effort e permissões.

---

## Riscos de tempo

| Risco | Mitigação |
|---|---|
| Bloco 5 tem 5 min para permissões, plan mode, reprodutibilidade, dados sensíveis e honestidade acadêmica | O roteiro já prioriza: os exemplos de uso (0–1.5) são o material sacrificável; as regras não. Se apertar na simulação, propor ao autor mover 2 min do Bloco 4, que tem folga. |
| Bloco 1 pode virar aula de deep learning | Amostragem e temperatura são menção de 1 minuto. Atenção é intuição, sem uma equação no slide. |
| Aluno chega na Aula 2 sem ambiente instalado | Cobrar o pré-requisito logo após a Aula 1: Claude Code funcionando e 4 a 6 fontes rascunhadas. Detalhes em [pratica-guiada.md](pratica-guiada.md). |
