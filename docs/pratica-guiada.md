# Bloco P — plano do instrutor

Prática aprovada: **newsletter semanal da minha área**. Cada aluno monta um agente que é acionado sob demanda, busca o que saiu na semana anterior nas fontes que ele mesmo listou, e gera uma edição em Markdown.

Sem agendamento. O agente não fica rodando nem cria tarefa recorrente — isso é regra explícita no `CLAUDE.md` do kit.

Kit do aluno: [`pratica/`](../pratica/). O aluno recebe tudo pronto menos dois arquivos, que são dele.

## Por que esta prática

| Conceito | Como aparece |
|---|---|
| janela de contexto | `/context` no início e no fim. O aluno vê o número mudar. |
| sessão | A prática inteira roda em uma sessão; o custo acumulado fica visível. |
| contexto persistente | O `CLAUDE.md` do kit é o orquestrador. Sem ele, o aluno teria que explicar o procedimento a cada vez. |
| skills | Duas, com papéis distintos: `curar-fontes` (buscar) e `redigir-edicao` (escrever). |
| references | `fontes.md`, `criterios.md` e `tom.md`. **É onde o aluno mexe.** Mesma skill, edição diferente por pessoa. |
| subagents | Um por fonte, em paralelo. A página inteira é lida no contexto do subagente; só os itens voltam. |
| agente orquestrador | O `CLAUDE.md` descreve o laço: janela → delegar → consolidar → redigir → relatar. |
| tool use | Busca e leitura de páginas. É o que torna o agente capaz de saber algo posterior ao treinamento. |
| verificação | Passo 5 é abrir dois links e conferir. Alguém vai achar um item errado — e é para isso que serve. |

Restam de fora: modelos, thinking/effort e permissões. São observados, não exercitados — mencionar durante a execução.

## Roteiro minutado (30 min)

| Min | Etapa | O que acontece |
|---|---|---|
| 0–5 | Setup e verificação | `git clone`, `cd pratica`, `claude`. Quem falhar entra em dupla imediatamente, sem tentar consertar. Instruções de instalação foram enviadas **antes** da sessão; estes 5 min são só verificação. |
| 5–7 | Linha de base | Todos rodam `/context` e anotam o número. Você comenta em voz alta o que está ali sem ninguém ter pedido: system prompt, `CLAUDE.md`, descrições das skills. Amarra o Bloco 2. |
| 7–12 | Configurar as fontes | O aluno preenche `references/fontes.md` com 4 a 6 fontes da área dele. É o momento mais individual da prática. Circular pela sala aqui. |
| 12–20 | Acionar o agente | `Gere a edição desta semana.` Enquanto roda: apontar os subagentes abrindo em paralelo, um por fonte. Perguntar em voz alta: "quantos tokens de página vocês acham que isso leu? E quanto voltou pro contexto principal?" |
| 20–24 | Verificar | Abrir dois links da edição. Conferir data e resumo. Perguntar quem encontrou item fora da janela, sem link, ou com resumo que não bate. Recolher os casos — eles são o material do debrief. |
| 24–27 | Mudar o tom | Editar `references/tom.md` para a variação "calouro de graduação" e pedir a reescrita. Nenhuma skill foi tocada. Este é o momento em que o conceito de reference fecha. |
| 27–30 | Debrief | Duas perguntas: o que surpreendeu, o que você usa amanhã. Fechar mostrando `/context` final e onde consultar a documentação. |

## O que dizer em cada momento

**Nos 5–7 min:** "Vocês ainda não pediram nada e a janela já tem alguns milhares de tokens. Isso é o Bloco 2 acontecendo na sua máquina."

**Nos 12–20:** o momento de maior densidade conceitual. Enquanto os subagentes rodam, nomear o que está na tela: delegação, contexto isolado, retorno consolidado.

**Nos 20–24:** não corrigir o erro de ninguém. Coletar. Um item alucinado na sala vale mais que dez slides sobre alucinação.

**Nos 24–27:** "Ninguém abriu o `SKILL.md`. Vocês mudaram um arquivo de apoio e a saída inteira mudou. Isso é o que separa procedimento de configuração."

## Plano de degradação

Ordem de sacrifício, se o tempo apertar:

1. **Corta a mudança de tom (24–27).** Vira tarefa de casa, com o passo 6 do README. É a perda menos grave porque o aluno consegue fazer sozinho depois.
2. **Encurta a verificação para 2 min.** Recolher só um caso, não vários.
3. **Reduz para 3 fontes** por aluno em vez de 6. A prática funciona igual, roda mais rápido.

Nunca cortar: a linha de base do `/context`, e a verificação dos links. São o que amarra a prática nos Blocos 1 e 2.

## Riscos e mitigação

| Risco | Probabilidade | Mitigação |
|---|---|---|
| Busca na web indisponível na conta do aluno | Média | O kit é desenhado para funcionar com URLs explícitas em `fontes.md`. Sem busca, o agente busca as páginas direto. Testar antes com uma conta igual à dos alunos. |
| Aluno escolhe fonte que exige login ou bloqueia acesso automatizado | Alta | Está no README. Ter 3 URLs de reserva, de domínio neutro, para entregar na hora. |
| Fonte não publicou nada na semana | Alta | É resultado válido e está previsto na skill: `nada na janela`. Tratar como acerto, não falha. |
| O agente erra a data e cobre a semana errada | Média | O `CLAUDE.md` manda declarar a janela antes de começar. Se a janela declarada estiver errada, o aluno percebe imediatamente. |
| Setup consome o bloco | Média | Instruções enviadas antes; 5 min só de verificação; dupla imediata para quem falhar. |
| Sala sem internet estável | Baixa | Ter uma edição pronta, gerada por você, para conduzir a discussão dos 20–30 min mesmo sem execução. |

## Preparação necessária antes da apresentação

- [ ] Publicar o repositório do kit e testar `git clone` em máquina limpa
- [ ] Rodar a prática inteira do zero, cronometrando, com uma conta equivalente à dos alunos
- [ ] Testar com busca na web desabilitada, para validar o caminho de fallback
- [ ] Enviar instruções de instalação com pelo menos 2 dias de antecedência
- [ ] Preparar 3 URLs de fontes de reserva
- [ ] Gerar e guardar uma edição de exemplo, para o caso de falha de rede
