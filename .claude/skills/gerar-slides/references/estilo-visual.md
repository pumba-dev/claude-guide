# Estilo visual dos slides

Direção: **seminário acadêmico**. A plateia inclui doutores da área. O deck precisa parecer trabalho sério e sóbrio, não material de marketing.

Os valores vivem em `slides/scripts/estilo.py`. Este arquivo explica as decisões e o que não fazer.

## Princípios

1. **Fundo claro.** Projeta bem em sala com luz, imprime, e a plateia consegue fotografar o slide sem estourar contraste.
2. **Uma ideia por slide.** Se o texto passa de ~520 caracteres, o slide vira dois. O script `conferir.py` cobra isso.
3. **Figura mostra mecanismo, não decora.** Nenhuma imagem ilustrativa genérica, nenhum ícone sem função.
4. **Todo número tem procedência.** Valor tirado da documentação aparece com crédito e mês de captura no rodapé do slide.
5. **Sem ornamento.** Nada de sombra, gradiente, animação, emoji ou ícone colorido. Régua: sobreviveria a uma revisão de qualificação?

## Paleta

| Papel | Uso |
|---|---|
| `ACENTO` (azul institucional) | o conceito em foco, o que o usuário controla |
| `NEUTRO` (cinza) | o que está fora de foco, o que o sistema faz sozinho |
| `ALERTA` (vermelho contido) | limitação, risco, item descartado |
| `OK` (verde contido) | ganho, confirmação, retorno |
| `CAMADA_A` / `B` / `C` / `T` | as camadas dos conceitos núcleo |

As cores das camadas variam em luminosidade, não só em matiz: continuam distinguíveis em escala de cinza e sob deuteranopia. Se acrescentar cor, mantenha essa propriedade.

Cor tem significado fixo no deck inteiro. Azul não pode significar "controlado por você" em uma figura e "sistema" em outra.

## Tipografia

- Títulos em serifada (`Georgia`), corpo em `Segoe UI`, código em `Consolas`.
- Ambas presentes por padrão em Windows e Office, para o arquivo abrir igual na máquina do auditório.
- Corpo do marcador não desce abaixo de 16 pt. Se não coube, o problema é excesso de texto, não o tamanho da fonte.

## Figuras

- Geradas por `figuras.py`, em PNG a 220 dpi, com fundo igual ao do slide.
- Mesma família tipográfica do deck.
- Legenda de eixo e rótulo em português; termo técnico consagrado em inglês permanece em inglês.
- Curva ilustrativa é declarada como ilustrativa no crédito. Dado real cita a fonte.

## Notas do apresentador

Todo slide com figura precisa de nota. A nota diz o que falar enquanto a figura está no ar — não repete o que está escrito.

## O que não fazer

- Editar o `.pptx` de saída à mão.
- Colar imagem de terceiro sem licença e sem crédito.
- Usar captura de tela de interface como se fosse explicação de mecanismo.
- Escrever cor literal dentro de uma figura em vez de importar de `estilo.py`.
- Reduzir fonte para caber mais texto.
