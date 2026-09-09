"""Paleta, tipografia e medidas compartilhadas entre o deck e as figuras.

Fonte única de verdade do visual. Mudou aqui, muda no .pptx e nos .png.

Direção visual: seminário acadêmico. Fundo claro, alta legibilidade em
projeção e em fotografia de plateia, paleta contida, sem ornamento.
"""

# --- Identificação -----------------------------------------------------------

AUTOR = "Paulo E. R. Araujo"
INSTITUICAO = "Laboratório de Computação"  # ajustar para o nome oficial
EVENTO = "Seminário — IA Generativa, LLMs e o ecossistema Claude"

# --- Paleta ------------------------------------------------------------------
# Fundo claro quente, texto quase preto. Um azul de acento e um vermelho
# reservado para limitação e risco. Cinzas fazem todo o trabalho estrutural.

FUNDO = "#FBFAF7"
FUNDO_SECAO = "#1B2A3A"  # divisórias de bloco, em negativo
FUNDO_CAIXA = "#F1EEE7"

TEXTO = "#16181D"
TEXTO_FRACO = "#6A6E76"
TEXTO_NEGATIVO = "#F7F6F2"

ACENTO = "#1F4E79"  # azul institucional: conceito em foco
ACENTO_CLARO = "#7FA8C9"
ALERTA = "#A32C33"  # limitação, risco, descarte
OK = "#2E6F52"  # confirmação, ganho
NEUTRO = "#C9C5BC"  # o que está fora de foco
LINHA = "#D8D4CB"

# Cores por camada dos conceitos núcleo. Distinguíveis também em escala de
# cinza e sob deuteranopia: variam em luminosidade, não só em matiz.
CAMADA_A = "#1F4E79"  # o que o modelo vê
CAMADA_B = "#7A5195"  # como ele responde
CAMADA_C = "#BC7A2F"  # o que ele consegue fazer
CAMADA_T = "#2E6F52"  # transversal

# --- Tipografia --------------------------------------------------------------
# Famílias com presença garantida no Windows e no Office, para o arquivo
# abrir igual na máquina do auditório.

FONTE_TITULO = "Georgia"  # serifada nos títulos: registro acadêmico
FONTE_CORPO = "Segoe UI"
FONTE_MONO = "Consolas"

PT_TITULO_CAPA = 40
PT_SUBTITULO_CAPA = 18
PT_TITULO = 30
PT_SUBTITULO = 17
PT_BULLET = 19
PT_BULLET_2 = 16
PT_ANCORA = 25
PT_LEGENDA = 12
PT_RODAPE = 10

# --- Geometria ---------------------------------------------------------------
# Slide 16:9, em polegadas.

LARGURA = 13.333
ALTURA = 7.5
MARGEM = 0.95
TOPO_TITULO = 0.62
TOPO_CORPO = 1.85
RODAPE_Y = 6.95

# --- Figuras -----------------------------------------------------------------

FIG_DPI = 220
FONTE_FIG = "Segoe UI"
CREDITO_PADRAO = "Elaboração própria."
CREDITO_DOC = "Elaboração própria a partir da documentação oficial do Claude Code (set. 2026)."
