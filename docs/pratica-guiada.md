# Aula 2 — plano do instrutor

Aula prática de 60 minutos. Prática aprovada: **newsletter semanal da minha área**, construída **do zero** por cada aluno.

Ninguém clona kit. O aluno abre o Claude Code em uma pasta vazia e pede ao próprio agente que escreva o `CLAUDE.md` do orquestrador, as duas skills e os arquivos de `references/`. Depois coloca as fontes dele, aciona, verifica e reconfigura o tom.

O agente é acionado sob demanda. Sem agendamento, sem tarefa recorrente — regra explícita nos prompts entregues ao aluno.

**Material do aluno:** [folha-do-aluno.md](folha-do-aluno.md) — prompts prontos para copiar.
**Material do instrutor:** [`gabarito/`](../gabarito/) — resultado esperado, para preparação, comparação e emergência. Não distribuir.

## Pré-requisito enviado após a Aula 1

Cobrar por mensagem, com pelo menos dois dias de antecedência:

1. Claude Code instalado e testado (`claude --version` responde)
2. Lista rascunhada de 4 a 6 fontes da própria área, com URLs

Sem isso, os primeiros 15 min da aula viram suporte técnico. Com isso, a aula começa no passo 1.

## Por que construir do zero

Se o aluno recebe as skills prontas, ele aprende **que existem**. Construindo, ele descobre o que importa: `CLAUDE.md` e `SKILL.md` são arquivos de texto que o próprio agente sabe escrever. A barreira de entrada desaparece na frente dele.

O custo é dispersão: cada aluno gera uma estrutura levemente diferente. Aceitável, porque a avaliação não é sobre o texto e sim sobre cinco propriedades arquiteturais.

## O que precisa aparecer no resultado de cada aluno

Checklist para circular pela sala:

1. o `CLAUDE.md` **orquestra e não lê as fontes ele mesmo**
2. uma fonte por subagente, em paralelo
3. procedimento no `SKILL.md`, configuração em `references/`
4. item sem link não entra
5. nenhum agendamento

Se as cinco aparecerem, funcionou — mesmo com redação diferente do gabarito.

## Cobertura dos treze conceitos

Com 60 minutos, a prática exercita **todos os treze**. Era o que faltava no formato de 30.

| Conceito | Onde aparece |
|---|---|
| harness | A prática inteira acontece dentro dele. Fica visível no `/context` e ao ver os subagentes sendo abertos |
| janela de contexto | `/context` no passo 0 e no passo 7 |
| sessão | Uma sessão só do começo ao fim; custo acumulado visível |
| contexto persistente | O aluno **escreve** o `CLAUDE.md` e vê o comportamento mudar |
| modelos | Comparação opcional no passo 4 |
| thinking e effort | Comparação opcional no passo 4 |
| tool use / MCP | Busca e leitura de páginas: o que dá acesso ao posterior ao treinamento |
| skills | Duas, com papéis distintos, criadas por pedido |
| references | O aluno decide o que sai da skill; e prova no passo 6, trocando o tom |
| subagents | Um por fonte; diferença de consumo observável no passo 7 |
| agente orquestrador | É o que o aluno especifica no passo 1 |
| permissões e plan mode | Passo 1 acontece em plan mode: o aluno lê o plano antes de aprovar |
| verificação | Passo 5: abrir dois links e conferir |

## Roteiro minutado (60 min)

| Min | Etapa | O que acontece |
|---|---|---|
| 0–4 | Retomada | Pirâmide dos treze conceitos da Aula 1, e o que vai ser construído hoje. Mostrar uma edição pronta — o destino, em 30 segundos. |
| 4–8 | Setup e linha de base | `mkdir newsletter && cd newsletter && claude`, depois `/context` e anotar. Quem falhar no setup entra em dupla **na hora**. |
| 8–16 | Orquestrador em plan mode | O aluno entra em plan mode e cola o prompt do passo 1. Lê o plano, aprova, lê o arquivo. Circule perguntando: "isso manda ele ler as fontes ou delegar?" |
| 16–26 | Skills e references | Prompt do passo 2. Ao final, a pergunta em voz alta: por que os critérios e o tom ficaram fora do `SKILL.md`? Deixe alguém responder. |
| 26–32 | Fontes | Momento mais individual. Circular é obrigatório: é onde as pessoas escolhem URL ruim. Quem trouxe a lista de casa termina em 3 min e ajuda o vizinho. |
| 32–44 | Acionar e observar | "Gere a edição desta semana." Enquanto roda, nomear o que aparece: janela declarada, subagentes em paralelo, retorno consolidado. Quem terminar cedo compara modelo ou effort. |
| 44–50 | Verificar | Abrir dois links. Recolher os casos de item errado, **sem corrigir**. |
| 50–56 | Trocar o tom | Editar o arquivo de tom e pedir a reescrita. Nenhuma skill tocada. É aqui que o conceito de reference fecha de verdade. |
| 56–60 | Debrief e ponte | Erros recolhidos no passo 5, `/context` final contra a linha de base, e a pergunta de saída: qual parte do seu trabalho tem essa mesma forma? |

## O que dizer em cada momento

**4–8:** "Vocês não pediram nada e a janela já tem alguns milhares de tokens. É a Aula 1 acontecendo na sua máquina."

**8–16:** "Repara no que você acabou de fazer: usou o agente para escrever as instruções do próprio agente. Não tem formato secreto — é Markdown." E, sobre o plano: "esse é o portão. Num repositório de verdade, é ele que separa uma sugestão de um estrago."

**16–26:** momento conceitual mais denso. A distinção procedimento × configuração separa quem vai reusar skills de quem vai continuar colando prompt.

**32–44:** narrar a delegação enquanto acontece. É a única chance de ver o Bloco 3 em movimento.

**44–50:** não conserte o erro de ninguém. Colete. Um item alucinado na sala vale mais que dez slides sobre alucinação.

**50–56:** "Ninguém abriu o `SKILL.md`. Vocês mudaram um arquivo de apoio e a saída inteira mudou."

## Plano de degradação

Com 60 min a folga é real, mas o risco não sumiu. Ordem de sacrifício:

1. **Corta a comparação de modelo/effort** no passo 4 — já é opcional.
2. **Uma skill só:** corta `redigir-edicao`, a redação fica no `CLAUDE.md`. Economiza ~6 min e ainda ensina skill e references.
3. **Três fontes** por aluno em vez de seis.
4. **Troca de tom vira tarefa de casa**, com o passo 6 da folha.

Nunca cortar: a linha de base do `/context`, a criação do orquestrador em plan mode, e a verificação dos links.

Se a sala estiver muito atrasada aos 40 min, mude para demonstração: acione o gabarito no projetor e conduza os 20 finais comentando. Todo mundo vê o resultado, ninguém fica travado.

## Riscos e mitigação

| Risco | Probabilidade | Mitigação |
|---|---|---|
| Aluno chega sem Claude Code instalado | **Alta** | Cobrança após a Aula 1. Dupla imediata para quem falhar, sem parar a aula. |
| Busca na web indisponível na conta do aluno | Média | Os prompts pedem fontes como URL completa; o agente busca a página direto. Testar antes com conta equivalente à dos alunos. |
| Fonte com login ou que bloqueia acesso | Alta | Está na folha. Ter 3 URLs de reserva, de domínio neutro. |
| Fonte sem novidade na semana | Alta | Resultado válido e previsto no prompt. Tratar como acerto. |
| Cada aluno gera estrutura diferente | Alta | Avaliar pelas 5 propriedades arquiteturais. Não tentar uniformizar. |
| O agente erra a janela de datas | Média | O prompt manda declarar a janela antes de começar; o aluno percebe na hora. |
| Sala sem internet estável | Baixa | Gabarito e uma edição já gerada, para conduzir sem execução. |

## Preparação necessária

- [ ] Rodar a prática **do zero**, cronometrando, com conta equivalente à dos alunos — os tempos acima são estimativa, não medição
- [ ] Repetir com busca na web desabilitada, para validar o fallback
- [ ] Guardar o resultado no `gabarito/`, atualizando o que estiver diferente
- [ ] Enviar o pré-requisito logo após a Aula 1
- [ ] Compartilhar a [folha do aluno](folha-do-aluno.md) de forma copiável — os prompts não podem ser digitados à mão
- [ ] Preparar 3 URLs de fontes de reserva
- [ ] Gerar e guardar uma edição de exemplo, para abrir nos primeiros 4 min e para o caso de falha de rede
