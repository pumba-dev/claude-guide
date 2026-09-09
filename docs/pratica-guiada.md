# Bloco P — plano do instrutor

Prática aprovada: **newsletter semanal da minha área**, construída **do zero** por cada aluno.

Ninguém clona kit. O aluno abre o Claude Code em uma pasta vazia e pede ao próprio agente que escreva o `CLAUDE.md` do orquestrador, as duas skills e os arquivos de `references/`. Depois preenche as fontes dele, aciona e verifica.

O agente é acionado sob demanda. Sem agendamento, sem tarefa recorrente — é regra explícita nos prompts entregues ao aluno.

**Material do aluno:** [folha-do-aluno.md](folha-do-aluno.md) — uma página, com os prompts prontos para copiar.
**Material do instrutor:** [`gabarito/`](../gabarito/) — o resultado esperado, para preparação, comparação e emergência. Não distribuir.

## Por que construir do zero muda a aula

Se o aluno recebe as skills prontas, ele aprende **que existem**. Construindo, ele descobre a coisa que realmente importa: `CLAUDE.md` e `SKILL.md` são arquivos de texto que o próprio agente sabe escrever. A barreira de entrada desaparece na frente dele.

O custo é dispersão: cada aluno vai gerar uma estrutura levemente diferente. Isso é aceitável porque a avaliação não é sobre o texto gerado, e sim sobre cinco propriedades arquiteturais (ver abaixo).

## O que precisa aparecer no resultado de cada aluno

Checklist para circular pela sala:

1. o `CLAUDE.md` **orquestra e não lê as fontes ele mesmo**
2. uma fonte por subagente, em paralelo
3. procedimento no `SKILL.md`, configuração em `references/`
4. item sem link não entra
5. nenhum agendamento

Se as cinco aparecerem, funcionou — mesmo com redação diferente do gabarito.

## Conceitos exercitados

| Conceito | Como aparece |
|---|---|
| janela de contexto | `/context` no passo 0 e no passo 6. O aluno vê o número mudar. |
| sessão | Tudo em uma sessão só; o custo acumulado fica visível ao final. |
| contexto persistente | O aluno **escreve** o `CLAUDE.md` e vê o agente passar a se comportar de outro jeito. |
| skills | Duas, com papéis distintos, criadas por pedido. |
| references | O aluno decide o que sai do `SKILL.md` e vira arquivo de apoio. É a pergunta do checkpoint 2. |
| subagents | Um por fonte. A diferença de consumo é observável no passo 6. |
| agente orquestrador | É o que o aluno especifica no passo 1, com as próprias palavras. |
| tool use | Busca e leitura de páginas — o que dá ao agente acesso ao que é posterior ao treinamento. |
| verificação | Passo 5. Abrir dois links e conferir. |

Ficam de fora, como observação e não exercício: modelos, thinking/effort e permissões.

## Roteiro minutado (30 min)

| Min | Etapa | O que acontece |
|---|---|---|
| 0–3 | Setup | `mkdir newsletter && cd newsletter && claude`. Quem falhar entra em dupla **na hora**, sem tentar consertar. Instalação foi enviada antes; aqui é só verificação. |
| 3–5 | Linha de base | Todos rodam `/context` e anotam. Você narra o que está ali sem ninguém ter pedido nada. Amarra o Bloco 2. |
| 5–10 | Criar o orquestrador | O aluno cola o prompt do passo 1 e **lê o arquivo gerado**. Circule perguntando: "isso aí manda ele ler as fontes ou delegar?" |
| 10–16 | Criar as skills | Prompt do passo 2. Ao final, a pergunta do checkpoint: por que os critérios e o tom ficaram fora do `SKILL.md`? Deixe alguém responder em voz alta. |
| 16–20 | Colocar as fontes | Momento mais individual. Circular aqui é obrigatório — é onde as pessoas escolhem URL ruim. |
| 20–26 | Acionar e observar | "Gere a edição desta semana." Enquanto roda, nomear o que aparece na tela: janela declarada, subagentes em paralelo, retorno consolidado. |
| 26–29 | Verificar | Abrir dois links. Recolher os casos de item errado, sem corrigir. |
| 29–30 | Fechar | `/context` final, comparar com a linha de base, uma pergunta de debrief. |

Comparado à versão com kit pronto, os passos de construção comeram o tempo que havia para a troca de tom e para o debrief longo. A troca de tom virou item do "se sobrar tempo" na folha do aluno.

## O que dizer em cada momento

**3–5 min:** "Vocês não pediram nada e a janela já tem alguns milhares de tokens. É o Bloco 2 acontecendo na sua máquina."

**5–10 min:** "Repara no que você acabou de fazer: você usou o agente para escrever as instruções do próprio agente. Não tem mágica nem formato secreto — é Markdown."

**10–16 min:** o momento conceitual mais denso. A distinção procedimento × configuração fecha aqui, e ela é o que separa quem vai reusar skills de quem vai continuar colando prompt.

**20–26 min:** narrar a delegação enquanto acontece. É a única chance de ver o Bloco 3 em movimento.

**26–29 min:** não conserte o erro de ninguém. Colete. Um item alucinado na sala vale mais que dez slides sobre alucinação.

## Plano de degradação

Ordem de sacrifício:

1. **Uma skill só.** Corta `redigir-edicao`; a redação fica no `CLAUDE.md`. Economiza ~4 min e ainda ensina skill e references. É o corte preferencial.
2. **Três fontes por aluno** em vez de seis. Roda mais rápido, ensina igual.
3. **Verificação encurtada** para 2 min: recolher um caso, não vários.

Nunca cortar: a linha de base do `/context`, a criação do orquestrador, e a verificação dos links. São o que amarra a prática nos Blocos 1, 2 e 3.

Se a sala estiver muito atrasada aos 20 min, pule direto para a sua máquina: acione o gabarito no projetor e conduza os 10 min finais como demonstração comentada. Todo mundo vê o resultado, ninguém fica travado.

## Riscos e mitigação

| Risco | Probabilidade | Mitigação |
|---|---|---|
| Construção do zero estoura o tempo | **Alta** | É o risco principal desta versão. Prompts vêm prontos na folha do aluno, para colar. Degradação nível 1 corta a segunda skill. |
| Cada aluno gera estrutura diferente e você perde o controle da sala | Alta | Avaliar pelas 5 propriedades arquiteturais, não pelo texto. Não tentar uniformizar. |
| Busca na web indisponível na conta do aluno | Média | Os prompts pedem fontes como URL completa, então o agente busca a página direto. Testar antes com conta equivalente à dos alunos. |
| Aluno escolhe fonte com login ou que bloqueia acesso | Alta | Está na folha. Ter 3 URLs de reserva, de domínio neutro, para entregar na hora. |
| Fonte sem novidade na semana | Alta | Resultado válido e previsto no prompt. Tratar como acerto. |
| O agente erra a janela de datas | Média | O prompt manda declarar a janela antes de começar; o aluno percebe na hora. |
| Sala sem internet estável | Baixa | Gabarito + uma edição já gerada, para conduzir a discussão sem execução. |

## Preparação necessária antes da apresentação

- [ ] Rodar a prática **do zero**, cronometrando, com conta equivalente à dos alunos — os tempos acima são estimativa, não medição
- [ ] Repetir com busca na web desabilitada, para validar o caminho de fallback
- [ ] Guardar o resultado dessa execução no `gabarito/`, atualizando o que estiver diferente
- [ ] Enviar instruções de instalação com pelo menos 2 dias de antecedência
- [ ] Imprimir ou compartilhar a [folha do aluno](folha-do-aluno.md) — os prompts precisam ser copiáveis, não digitados
- [ ] Preparar 3 URLs de fontes de reserva
- [ ] Gerar e guardar uma edição de exemplo para o caso de falha de rede
