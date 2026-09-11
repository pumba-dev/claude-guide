@capa
# IA Generativa, LLMs e o ecossistema Claude
### Aula 1 — dos fundamentos ao agente
> 3 min de abertura. Não é palestra de futurologia nem tutorial de prompt.

---

:bloco Abertura
# O que esta aula entrega
- Ao final das duas aulas você abre o Claude no seu próprio projeto e sabe o que acontece em cada camada
- Aula 1: por que uma LLM se comporta como se comporta
- Aula 2: você constrói um agente do zero, com orquestrador, skills e material de apoio
- Treze conceitos operacionais. Toda a teoria existe para sustentá-los, não o contrário
> "Vocês já sabem ler um paper e já sabem programar. O que falta é saber o que acontece entre apertar Enter e a resposta aparecer. Nesta aula a gente abre essa caixa. Na próxima, vocês operam ela."

---

# A ordem desta aula não é estética
### Cada conceito depende do anterior. Por isso começamos por baixo
:fig piramide
:fonte Elaboração própria.
> Este slide reaparece no início de cada bloco, com o item da vez destacado. É a barra de progresso conceitual da aula. Adiantar uma frase: tudo isto acontece dentro de uma aplicação, o harness, que é o primeiro assunto do próximo bloco.

---

## Bloco 1
### Fundamentos: por que o modelo faz o que faz

---

:bloco 1 · Fundamentos
# Duas famílias, dois objetivos
:fig discriminativo-generativo
:fonte Elaboração própria.
> Público já conhece classificador. A ponte é essa. O generativo repete a pergunta a cada token — é o que torna a saída aberta.

---

# Token: a unidade que importa
- Não é palavra nem caractere: é o pedaço que o modelo enxerga
- É a unidade de **custo**, de **limite** e de **latência**
- Português rende mais tokens que inglês para o mesmo conteúdo
:fig tokenizacao
:fonte Segmentação ilustrativa; a divisão exata depende do tokenizador do modelo.
> Se der para mostrar um tokenizador ao vivo, é o maior retorno visual do bloco.

---

# Predição do próximo token
- O modelo estima uma distribuição sobre o vocabulário e escolhe o próximo token
- Repete o processo, agora incluindo o que acabou de gerar
- Não existe um passo em que ele consulta uma base de fatos
  - a resposta é construída, não recuperada
  - daí a alucinação não ser um defeito de implementação, e sim o modo de operação
> Aqui já se planta a limitação estrutural que fecha o bloco.

---

# Atenção: de onde vem o limite de contexto
:fig atencao
:fonte Elaboração própria. Curva ilustrativa do número de pares de tokens.
> Intuição, sem matriz. O ponto único: o custo não cresce em linha reta, e é isso que origina o limite de contexto. Não é decisão comercial.

---

# Duas etapas de treinamento
- **Pré-treino**: prever texto em larga escala. Produz capacidade bruta
- **Post-training**: alinhar a modelo de assistente útil e seguro
  - explica preferências de formato que ninguém programou explicitamente
  - explica também por que dois modelos com dados parecidos se comportam diferente
- **Amostragem e temperatura**: mesmo prompt, saídas diferentes
  - consequência direta: não é reprodutível por construção
> Amostragem é menção de 1 minuto. O que importa é a consequência, que volta no Bloco 5.

---

# Três limitações estruturais
- **Alucinação** — gera o plausível, não o verdadeiro
- **Data de corte** — não conhece o que veio depois do treinamento
- **Ausência de estado** — cada requisição começa do zero
  - as três decorrem do mecanismo que acabamos de ver
  - nenhuma delas é bug a ser corrigido na próxima versão
> Fecha o bloco. Cada uma volta adiante: alucinação no Bloco 5, data de corte no tool use, ausência de estado já no próximo slide. Deixar a pergunta no ar antes de virar: se o modelo não guarda nada e não executa nada, quem faz o resto?

---

!! O modelo não busca, ele completa. Por isso toda saída que você for citar em um paper precisa ser verificada por você — e por isso escrever em português custa mais caro que em inglês.
# Âncora do Bloco 1

---

## Bloco 2
### Anatomia de uma requisição

---

:bloco 2 · Anatomia da requisição
# Você não conversa com o modelo
:fig harness
:fonte Elaboração própria a partir do glossário da documentação oficial do Claude Code (set. 2026).
> A pergunta que fechou o Bloco 1: se o modelo não guarda estado e não executa nada, quem faz o resto? Esta figura é a resposta. O modelo é uma função de texto para texto; a sessão, a memória, os arquivos e as ferramentas são todos do harness. Termo oficial, não apelido: "Claude Code is the harness; Claude is the model inside it".

---

# O que o harness faz por você
- **Monta a requisição** — injeta system prompt, `CLAUDE.md` e descrições de skills antes do seu texto
- **Mantém a sessão** — reenvia o histórico a cada turno, porque o modelo não guarda nada
- **Executa as ferramentas** — o modelo pede, o harness faz e devolve o resultado
- **Aplica o portão** — permissões e plan mode ficam fora do componente estocástico
- **Administra a janela** — conta, compacta e abre subagentes quando falta espaço
> Cada linha aqui é um bloco desta aula. Dizer isso em voz alta: o resto da aula é detalhar o que esta caixa faz. Notar que o portão de permissões é do harness — é justamente por isso que ele é confiável.

---

# O que é enviado a cada turno
:fig orcamento-janela
:fonte Elaboração própria a partir do simulador de janela de contexto da documentação oficial do Claude Code (set. 2026).
> A maior parte do que o modelo lê não foi escrita naquele turno. Este é o slide mais importante da aula.

---

# A janela é um orçamento, não uma memória
- 200 mil tokens no padrão; 1 milhão em modelos de janela estendida
- Não é "quanto ele lembra": é quanto cabe **nesta** requisição
- Cada leitura de arquivo debita do mesmo orçamento
  - um arquivo de código médio custa entre 1.100 e 2.400 tokens
  - dez arquivos e o orçamento do turno já mudou de figura
> Números do simulador oficial. Se alguém perguntar de onde vêm, a fonte está no rodapé do slide anterior.

---

# Sessão: o modelo é stateless
:fig sessao-stateless
:fonte Elaboração própria. Valores ilustrativos.
> Custo sobe, latência sobe, e o relevante começa a competir com o histórico. É a explicação mecânica de "conversa longa degrada".

---

# Dois contrapesos do sistema
- **Prompt caching** — o prefixo repetido é cacheado e sai muito mais barato que a primeira vez
  - sem isso, o reenvio a cada turno seria inviável
  - sessão longa é cara em janela, menos em dinheiro
- **Compaction** — quando a janela satura, a conversa é resumida e recomeça
:fig compaction
:fonte Elaboração própria a partir da documentação oficial do Claude Code (set. 2026).
> Honestidade: o resumo perde detalhe. Daí a decisão consciente entre compactar e abrir sessão nova.

---

# O que atravessa sessões
- **Contexto persistente**: `CLAUDE.md` no Code, Projects e memória no Chat
- Entra **sempre**, em toda requisição — ao contrário do material de apoio, que entra sob demanda
- Consequência dupla:
  - escrever demais nele é caro, porque o custo é recorrente
  - escrever bem nele é a alavanca de maior retorno que existe
> É a resposta prática à ausência de estado do Bloco 1.

---

# Modelo, thinking e effort
- **Modelo**: capacidade × latência × custo. Não existe escolha universalmente certa
- **Thinking**: o modelo raciocina antes de responder — e esse raciocínio também são tokens
- **Effort**: quanto desse raciocínio investir
  - níveis disponíveis: `low`, `medium`, `high`, `xhigh`, `max`; padrão `high`
  - tarefa mecânica com effort alto é tempo e dinheiro jogados fora
  - tarefa de projeto com effort baixo é retrabalho
:fonte Níveis conforme a documentação oficial do Claude Code (set. 2026).
> Não é botão de "ficar mais inteligente". É alocação de orçamento.

---

!! Conversa longa degrada porque o histórico inteiro volta a cada turno e empurra o que importa para o meio do ruído. Por isso vale abrir sessão nova quando o assunto muda — e por isso vale escrever o CLAUDE.md uma vez em vez de reexplicar o projeto toda vez.
# Âncora do Bloco 2

---

## Bloco 3
### Do sistema ao agente

---

:bloco 3 · Do sistema ao agente
# Tool use, apresentado como protocolo
- O servidor expõe ferramentas com nome, descrição e schema
- O harness injeta essa lista no contexto do modelo
- O modelo responde **pedindo** uma chamada; o harness executa e devolve o resultado
- MCP é o protocolo aberto que padroniza esse contrato
  - a mesma ferramenta serve a qualquer harness que fale o protocolo
> "O modelo nunca executa nada — ele pede." Para este público, é a frase que destrava o bloco inteiro.

---

# O laço
:fig laco-agente
:fonte Elaboração própria.
> Mapear cada etapa no que acabou de ser descrito. Quem percorre este laço é o harness: ele é que chama o modelo, executa o que foi pedido e decide se roda outra volta. O laço encerra quando o modelo devolve texto em vez de pedir ferramenta.

---

# Agente orquestrador
- Quem roda o laço: mantém o objetivo, escolhe a ferramenta, decide quando delegar e quando parar
- É um **papel**, não um produto — o mesmo papel aparece nos três produtos da próxima seção
- No Claude Code, esse papel é descrito em texto, no `CLAUDE.md` do projeto
  - é literalmente Markdown: sem formato secreto, sem API
  - é o que vocês vão escrever na Aula 2
> Ponte explícita para a prática.

---

# Skills e o material de apoio
:fig skill-references
:fonte Elaboração própria a partir da documentação oficial de Agent Skills (set. 2026).
> Procedimento no SKILL.md, configuração nos arquivos de apoio. É o que separa quem reusa skills de quem continua colando prompt.

---

# Subagents: comprar janela de contexto
:fig subagente
:fonte Elaboração própria a partir do simulador de janela de contexto da documentação oficial do Claude Code (set. 2026).
> A economia fica visível em vez de afirmada. É a resposta direta ao problema do Bloco 2.

---

!! Contexto é o recurso escasso, e você tem três formas de gastá-lo menos: skill em vez de repetir instrução, material de apoio em vez de colar documentação, subagente em vez de ler dez arquivos no contexto principal.
# Âncora do Bloco 3

---

## Bloco 4
### Claude concreto: três interfaces, uma base

---

:bloco 4 · Claude concreto
# Três portas para o mesmo prédio
:fig tres-produtos
:fonte Elaboração própria.
> Retomar o Bloco 2 com uma frase: Chat, Cowork e Code são três harnesses sobre o mesmo modelo. O que muda entre eles é o que o harness faz por você, não a inteligência por trás. E nomes de modelo mudam; o critério capacidade × latência × custo não — dizer isso em voz alta protege o material do tempo.

---

# Onde cada conceito aparece — Chat e Cowork
- Os dois são harnesses: mesma base, ambientes diferentes
- **Chat** — a porta de entrada do pesquisador
  - Projects e memória fazem o papel de contexto persistente
  - connectors são tool use com outra roupa
- **Cowork** — trabalho delegado sobre arquivos e tarefas
  - dispatch e times de agentes são o orquestrador com interface
> Quando usar qual: pensar no Chat, delegar no Cowork, executar no repositório com o Code.

---

# Onde cada conceito aparece — Code
- **Code** — o agente dentro do repositório
  - `CLAUDE.md`, skills, material de apoio e subagents
  - quatro superfícies: terminal, IDE, aplicativo de desktop e web
- **Hooks** — comando determinístico em torno de um núcleo estocástico
  - é a ponte para reprodutibilidade, que volta no próximo bloco
- **Checkpointing** — desfazer o que o agente fez
> Este é o slide que o aluno fotografa. Deixar tempo para isso.

---

## Bloco 5
### Aplicação em pesquisa em computação

---

:bloco 5 · Aplicação em pesquisa
# Quatro tipos de trabalho, não quatro domínios
- **Entender artefato herdado**
  - o simulador que o aluno anterior deixou, um pipeline, um protótipo
  - o problema é sempre o mesmo: código sem ninguém para explicá-lo
- **Analisar resultado experimental**
  - saída de simulação, log, captura, planilha de coleta, questionário
  - o problema é sempre o mesmo: volume acima da leitura manual
> O bloco é organizado por tipo de trabalho justamente porque o laboratório tem domínios muito diferentes. Ninguém precisa traduzir do domínio alheio para o seu.

---

# Quatro tipos de trabalho, não quatro domínios
- **Levantar e organizar literatura**
  - triagem, extração de critérios, tabela comparativa de revisão sistemática
  - ressalva: o modelo não é fonte bibliográfica, e sim ferramenta de organização sobre o que você forneceu
- **Apoiar a escrita** — estrutura, clareza, revisão de argumento
- Atravessando os quatro: **reprodutibilidade**
  - o que o agente fez precisa virar script, commit e ambiente registrados
> É aqui que hooks reaparecem: o jeito determinístico de garantir isso em torno de um modelo que não é determinístico.

---

# Permissões: o portão do laço
- Um agente com acesso ao repositório edita arquivos e executa comandos
- O portão é do **harness**, não do modelo: pedir aprovação, aceitar edições, ou planejar antes de agir
- **Plan mode**: o agente mostra o plano e espera. Você lê antes de qualquer escrita
- Regra prática: repositório de terceiro, base de coleta ou artefato que você não pode recriar começa em plan mode
> Vocês vão usar plan mode na Aula 2, no primeiro passo.

---

# Dados sensíveis: duas categorias, duas réguas
- **Dado técnico**
  - credencial, chave, endereço de infraestrutura, identificador de rede
  - régua: política da instituição e bom senso operacional
- **Dado de pessoa**
  - prontuário, registro de aluno, resposta de questionário, qualquer coisa sob TCLE
  - régua: o protocolo de pesquisa e a LGPD, não o que a ferramenta permite
> Consultar a política oficial de privacidade e uso de dados, não a opinião de quem está no palco. Este slide é o mais importante do bloco para quem pesquisa saúde e educação.

---

# A régua do dado de pessoa
- Se o consentimento não previu processamento por serviço de terceiro, o dado não sai da máquina
- Anonimização é decisão de projeto, não etapa improvisada na véspera
- Na dúvida, o caminho é o comitê de ética, não a documentação da ferramenta
:fonte Política de privacidade e de uso de dados da Anthropic; LGPD, Lei nº 13.709/2018.
> Deixar este slide no ar por alguns segundos a mais. É o único ponto da aula sem margem para interpretação.

---

# Verificação e honestidade acadêmica
- Saída plausível não é saída correta — o Bloco 1 já mostrou por quê
- O que o modelo produz é rascunho até você rodar, conferir e reproduzir
- Duas armadilhas específicas do nosso trabalho:
  - referência bibliográfica inventada com aparência perfeita
  - resultado numérico produzido sem que nada tenha sido executado
- Declarar o uso conforme a norma do programa e do veículo
> Nada assinado por você entra sem você ter verificado.

---

!! O agente acelera a parte mecânica e não assume nenhuma responsabilidade. A assinatura no paper é sua, então a verificação também é — e o dado que saiu do seu computador não volta.
# Âncora do Bloco 5

---

@encerramento
# Na próxima aula, vocês constroem
- Um agente que busca o que saiu na semana anterior na sua área e escreve uma newsletter
- Do zero: orquestrador, skills e material de apoio, escritos com o próprio agente
- Para chegar pronto: Claude Code instalado e testado, e 4 a 6 fontes da sua área com as URLs
- Quem chegar sem isso perde os primeiros quinze minutos
> Ponte para a Aula 2 e cobrança do pré-requisito. Repetir que o pré-requisito é o que devolve tempo real de prática.

---

:bloco Referências
# Referências
- Documentação oficial do Claude Code — code.claude.com/docs, incluindo o glossário e "How Claude Code works", onde o harness é definido
- Documentação de Agent Skills e do formato `SKILL.md`
- Central de ajuda do Claude: Projects, memória, connectors e Cowork
- Política de privacidade e de uso de dados da Anthropic
- Espelho local consultado para esta aula, com data de captura registrada no repositório
:fonte Documentação consultada em setembro de 2026. Produtos e números podem mudar; o mecanismo, não.
> Deixar aberto durante as perguntas.
