"""Gera as figuras do deck em PNG, a partir dos dados reais da documentação.

Uso:
    python slides/scripts/figuras.py [nome-da-figura ...]

Sem argumentos, gera todas em slides/build/figuras/.

Cada função `fig_*` devolve uma figura matplotlib. O nome da figura no
conteúdo do deck é o sufixo do nome da função, com hífens.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

sys.path.insert(0, str(Path(__file__).parent))
import estilo as E  # noqa: E402

SAIDA = Path(__file__).resolve().parents[1] / "build" / "figuras"

plt.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": [E.FONTE_FIG, "DejaVu Sans"],
        "figure.facecolor": E.FUNDO,
        "axes.facecolor": E.FUNDO,
        "savefig.facecolor": E.FUNDO,
        "text.color": E.TEXTO,
        "axes.labelcolor": E.TEXTO,
        "xtick.color": E.TEXTO_FRACO,
        "ytick.color": E.TEXTO_FRACO,
        "axes.edgecolor": E.LINHA,
        "axes.linewidth": 0.8,
        "font.size": 12,
    }
)


def _limpa(ax, manter=()):
    for lado in ("top", "right", "bottom", "left"):
        if lado not in manter:
            ax.spines[lado].set_visible(False)
    if "bottom" not in manter:
        ax.set_xticks([])
    if "left" not in manter:
        ax.set_yticks([])


def _caixa(ax, x, y, w, h, texto, cor, cor_texto=None, fonte=11, alpha=1.0, negrito=False):
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            linewidth=0,
            facecolor=cor,
            alpha=alpha,
            zorder=2,
        )
    )
    ax.text(
        x + w / 2,
        y + h / 2,
        texto,
        ha="center",
        va="center",
        fontsize=fonte,
        color=cor_texto or E.TEXTO_NEGATIVO,
        weight="bold" if negrito else "normal",
        zorder=3,
        linespacing=1.35,
    )


def _seta(ax, p1, p2, cor=None, estilo="-|>", lw=1.4, curva=0.0):
    ax.add_patch(
        FancyArrowPatch(
            p1,
            p2,
            arrowstyle=estilo,
            mutation_scale=13,
            linewidth=lw,
            color=cor or E.TEXTO_FRACO,
            connectionstyle=f"arc3,rad={curva}",
            zorder=4,
        )
    )


# --- 1. Pirâmide de dependências --------------------------------------------


def fig_piramide():
    """Cadeia de dependências conceituais. Slide recorrente da Aula 1."""
    fig, ax = plt.subplots(figsize=(10, 5.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.4)
    _limpa(ax)

    niveis = [
        ("token", "unidade de custo, limite e latência", E.NEUTRO, E.TEXTO, 0.35, 9.3),
        ("janela de contexto", "orçamento finito por requisição", E.CAMADA_A, None, 0.95, 8.1),
        ("sessão", "reenvio de histórico em modelo stateless", E.CAMADA_A, None, 1.55, 7.0),
        ("modelos · thinking · effort", "como o esforço é regulado", E.CAMADA_B, None, 2.15, 6.0),
        ("tool use / MCP", "a fronteira entre chatbot e agente", E.CAMADA_C, None, 2.75, 5.1),
        ("skills · references · subagents", "capacidade e contexto sob demanda", E.CAMADA_C, None, 3.35, 4.3),
        ("agente orquestrador", "o laço que coordena tudo acima", E.CAMADA_T, None, 3.95, 3.6),
    ]
    for rotulo, sub, cor, cor_txt, y, larg in niveis:
        x = (10 - larg) / 2
        _caixa(ax, x, y, larg, 0.52, "", cor, fonte=12)
        ax.text(
            5,
            y + 0.31,
            rotulo,
            ha="center",
            va="center",
            fontsize=12.5,
            color=cor_txt or E.TEXTO_NEGATIVO,
            weight="bold",
            zorder=3,
        )
        ax.text(
            5,
            y + 0.13,
            sub,
            ha="center",
            va="center",
            fontsize=9,
            color=cor_txt or E.TEXTO_NEGATIVO,
            alpha=0.85,
            zorder=3,
        )

    ax.annotate(
        "sustenta",
        xy=(9.55, 2.6),
        xytext=(9.55, 0.5),
        ha="center",
        fontsize=9.5,
        color=E.TEXTO_FRACO,
        rotation=90,
        arrowprops=dict(arrowstyle="-|>", color=E.TEXTO_FRACO, linewidth=1.1),
    )
    return fig


# --- 2. Discriminativo vs. generativo ---------------------------------------


def fig_discriminativo_generativo():
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.4))
    for ax, titulo, cor in zip(
        axes, ("Modelo discriminativo", "Modelo generativo"), (E.NEUTRO, E.ACENTO)
    ):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        _limpa(ax)
        ax.set_title(titulo, fontsize=14, color=E.TEXTO, weight="bold", pad=14)

    ax = axes[0]
    _caixa(ax, 0.6, 3.6, 3.0, 1.1, "entrada\n(texto, imagem)", E.FUNDO_CAIXA, E.TEXTO, 10.5)
    _seta(ax, (3.8, 4.15), (5.6, 4.15))
    _caixa(ax, 5.8, 3.6, 3.4, 1.1, "P(classe | entrada)", E.NEUTRO, E.TEXTO, 11, negrito=True)
    ax.text(
        5.0,
        2.3,
        "responde: a qual categoria isto pertence?\nsaída em espaço fechado e pequeno",
        ha="center",
        va="center",
        fontsize=10.5,
        color=E.TEXTO_FRACO,
        linespacing=1.5,
    )

    ax = axes[1]
    _caixa(ax, 0.6, 3.6, 3.0, 1.1, "contexto\n(tokens anteriores)", E.FUNDO_CAIXA, E.TEXTO, 10.5)
    _seta(ax, (3.8, 4.15), (5.35, 4.15), cor=E.ACENTO)
    _caixa(ax, 5.5, 3.6, 3.9, 1.1, "P(próximo token\n| contexto)", E.ACENTO, fonte=11, negrito=True)
    ax.text(
        5.0,
        2.3,
        "responde: o que vem a seguir?\nsaída em todo o vocabulário, repetida a cada token",
        ha="center",
        va="center",
        fontsize=10.5,
        color=E.TEXTO_FRACO,
        linespacing=1.5,
    )
    fig.tight_layout()
    return fig


# --- 3. Tokenização PT vs. EN ------------------------------------------------


def fig_tokenizacao():
    """Comparação ilustrativa: a mesma frase custa mais tokens em português."""
    fig, ax = plt.subplots(figsize=(10, 4.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    _limpa(ax)

    pt = ["A ", "jan", "ela ", "de ", "cont", "ex", "to ", "é ", "fin", "ita"]
    en = ["The ", "context ", "window ", "is ", "fin", "ite"]

    def linha(tokens, y, rotulo, cor):
        ax.text(0.15, y + 0.62, rotulo, fontsize=11, color=E.TEXTO_FRACO)
        x = 0.15
        for i, t in enumerate(tokens):
            w = 0.28 + 0.165 * len(t)
            ax.add_patch(
                FancyBboxPatch(
                    (x, y),
                    w,
                    0.5,
                    boxstyle="round,pad=0.01,rounding_size=0.05",
                    facecolor=cor,
                    alpha=0.22 + 0.05 * (i % 2),
                    edgecolor=cor,
                    linewidth=0.9,
                )
            )
            ax.text(
                x + w / 2,
                y + 0.25,
                t.replace(" ", "·"),
                ha="center",
                va="center",
                fontsize=11.5,
                family=E.FONTE_MONO,
                color=E.TEXTO,
            )
            x += w + 0.09
        ax.text(
            x + 0.15,
            y + 0.25,
            f"{len(tokens)} tokens",
            va="center",
            fontsize=12,
            color=cor,
            weight="bold",
        )

    linha(pt, 2.9, "português", E.ALERTA)
    linha(en, 1.4, "inglês", E.ACENTO)
    ax.text(
        0.15,
        0.5,
        "Mesmo conteúdo, mais tokens: mais custo, mais latência e menos espaço na janela.",
        fontsize=11,
        color=E.TEXTO_FRACO,
    )
    return fig


# --- 4. Atenção e custo superlinear -----------------------------------------


def fig_atencao():
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.3), gridspec_kw={"width_ratios": [1, 1.15]})

    ax = axes[0]
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    _limpa(ax)
    ax.set_title("Cada token olha para todos", fontsize=13, color=E.TEXTO, weight="bold", pad=12)
    pos = [(1.0, 4.6), (2.6, 5.2), (4.2, 4.6), (5.0, 3.0), (3.6, 1.6), (1.6, 2.0)]
    for i, (x1, y1) in enumerate(pos):
        for j, (x2, y2) in enumerate(pos):
            if i < j:
                ax.plot([x1, x2], [y1, y2], color=E.ACENTO_CLARO, linewidth=0.7, alpha=0.55, zorder=1)
    for x, y in pos:
        ax.add_patch(plt.Circle((x, y), 0.30, color=E.ACENTO, zorder=3))
    ax.text(
        3.0,
        0.35,
        "n tokens → n(n−1)/2 pares",
        ha="center",
        fontsize=11,
        color=E.TEXTO_FRACO,
    )

    ax = axes[1]
    n = list(range(1, 33))
    pares = [k * (k - 1) / 2 for k in n]
    linear = [k * 8 for k in n]
    ax.plot(n, pares, color=E.ALERTA, linewidth=2.4, label="pares de tokens (atenção)")
    ax.plot(n, linear, color=E.NEUTRO, linewidth=1.6, linestyle="--", label="crescimento linear")
    ax.set_xlabel("comprimento do contexto (tokens)", fontsize=10.5)
    ax.set_ylabel("trabalho relativo", fontsize=10.5)
    ax.set_title("O custo não cresce em linha reta", fontsize=13, color=E.TEXTO, weight="bold", pad=12)
    ax.legend(frameon=False, fontsize=10, loc="upper left")
    _limpa(ax, manter=("bottom", "left"))
    ax.set_xticks([0, 8, 16, 24, 32])
    ax.set_yticks([])
    fig.tight_layout()
    return fig


# --- 5. Orçamento da janela de contexto -------------------------------------

# Valores do simulador oficial da documentação do Claude Code.
ORCAMENTO = [
    ("System prompt", 4200, "automático"),
    ("Memória automática", 680, "automático"),
    ("Informação de ambiente", 280, "automático"),
    ("Ferramentas MCP (diferidas)", 120, "automático"),
    ("Descrições de skills", 450, "automático"),
    ("CLAUDE.md pessoal", 320, "automático"),
    ("CLAUDE.md do projeto", 1800, "automático"),
    ("Seu prompt", 45, "você"),
]


def fig_orcamento_janela():
    """O que ocupa a janela antes de o usuário pedir qualquer coisa."""
    fig, ax = plt.subplots(figsize=(10.5, 4.8))
    rotulos = [r for r, _, _ in ORCAMENTO][::-1]
    valores = [v for _, v, _ in ORCAMENTO][::-1]
    origens = [o for _, _, o in ORCAMENTO][::-1]
    sob_controle = {"Seu prompt", "CLAUDE.md do projeto", "CLAUDE.md pessoal", "Descrições de skills"}
    cores = [E.ACENTO if r in sob_controle else E.NEUTRO for r in rotulos]

    barras = ax.barh(rotulos, valores, color=cores, height=0.62)
    for barra, valor in zip(barras, valores):
        ax.text(
            valor + 60,
            barra.get_y() + barra.get_height() / 2,
            f"{valor:,}".replace(",", "."),
            va="center",
            fontsize=11,
            color=E.TEXTO,
        )
    ax.set_xlim(0, 5100)
    _limpa(ax, manter=("left",))
    ax.tick_params(axis="y", length=0, labelsize=11.5)
    total = sum(valores)
    ax.set_title(
        f"Antes do primeiro pedido: {total:,}".replace(",", ".")
        + " tokens já ocupam a janela de 200.000",
        fontsize=13.5,
        color=E.TEXTO,
        weight="bold",
        pad=16,
        loc="left",
    )
    ax.text(
        0,
        -1.25,
        "Em azul, o que você escreveu ou controla. Em cinza, o que entra sem você pedir.",
        fontsize=10.5,
        color=E.TEXTO_FRACO,
        transform=ax.get_yaxis_transform(),
    )
    fig.tight_layout()
    return fig


# --- 6. Sessão stateless -----------------------------------------------------


def fig_sessao_stateless():
    """Cada turno reenvia todo o histórico: o custo por turno cresce."""
    fig, ax = plt.subplots(figsize=(10.5, 4.6))
    ax.set_xlim(0, 10.6)
    ax.set_ylim(0, 5.2)
    _limpa(ax)

    turnos = 4
    for t in range(turnos):
        x = 0.35 + t * 2.55
        altura_total = 0.0
        blocos = [("sistema", 0.42, E.NEUTRO)]
        for k in range(t):
            blocos.append((f"turno {k + 1}", 0.34, E.ACENTO_CLARO))
        blocos.append((f"turno {t + 1}", 0.34, E.ACENTO))
        y = 0.95
        for rotulo, h, cor in blocos:
            ax.add_patch(
                FancyBboxPatch(
                    (x, y),
                    2.1,
                    h - 0.05,
                    boxstyle="round,pad=0.005,rounding_size=0.03",
                    facecolor=cor,
                    edgecolor="none",
                )
            )
            if h > 0.4 or t == 0 or rotulo.startswith(f"turno {t + 1}"):
                ax.text(
                    x + 1.05,
                    y + (h - 0.05) / 2,
                    rotulo,
                    ha="center",
                    va="center",
                    fontsize=9,
                    color=E.TEXTO_NEGATIVO,
                )
            y += h
            altura_total += h
        ax.text(
            x + 1.05,
            0.6,
            f"requisição {t + 1}",
            ha="center",
            fontsize=10.5,
            color=E.TEXTO,
            weight="bold",
        )
        ax.text(
            x + 1.05,
            y + 0.18,
            f"{int(altura_total * 3000):,}".replace(",", ".") + " tokens",
            ha="center",
            fontsize=9.5,
            color=E.TEXTO_FRACO,
        )

    ax.text(
        0.35,
        4.75,
        "O modelo não guarda estado. A conversa existe porque o cliente reenvia tudo, a cada turno.",
        fontsize=11.5,
        color=E.TEXTO,
    )
    ax.text(
        0.35,
        0.15,
        "Consequência: custo e latência sobem a cada turno, e o conteúdo relevante disputa espaço com o histórico.",
        fontsize=10.5,
        color=E.TEXTO_FRACO,
    )
    return fig


# --- 7. Laço do agente -------------------------------------------------------


def fig_laco_agente():
    fig, ax = plt.subplots(figsize=(9.6, 4.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    _limpa(ax)

    etapas = [
        ("perceber", "lê o contexto e o\nresultado anterior", 1.55, 3.55),
        ("planejar", "decide o próximo\npasso", 5.0, 4.15),
        ("agir", "pede uma chamada\nde ferramenta", 8.45, 3.55),
        ("observar", "recebe o resultado\nda execução", 5.0, 1.55),
    ]
    for rotulo, sub, x, y in etapas:
        _caixa(ax, x - 1.25, y - 0.62, 2.5, 1.24, "", E.ACENTO)
        ax.text(x, y + 0.24, rotulo, ha="center", fontsize=13, color=E.TEXTO_NEGATIVO, weight="bold", zorder=3)
        ax.text(x, y - 0.22, sub, ha="center", fontsize=9.5, color=E.TEXTO_NEGATIVO, alpha=0.9, zorder=3, linespacing=1.4)

    _seta(ax, (2.85, 3.85), (3.7, 4.05), cor=E.ACENTO, curva=-0.25)
    _seta(ax, (6.3, 4.05), (7.15, 3.85), cor=E.ACENTO, curva=-0.25)
    _seta(ax, (8.45, 2.9), (6.3, 1.75), cor=E.ACENTO, curva=-0.25)
    _seta(ax, (3.7, 1.75), (1.55, 2.9), cor=E.ACENTO, curva=-0.25)

    ax.text(
        5.0,
        0.55,
        "O modelo nunca executa nada: ele pede. Quem executa é o harness, que devolve o resultado.",
        ha="center",
        fontsize=11.5,
        color=E.TEXTO,
    )
    ax.text(
        5.0,
        0.15,
        "O laço encerra quando o modelo responde com texto em vez de pedir uma ferramenta.",
        ha="center",
        fontsize=10.5,
        color=E.TEXTO_FRACO,
    )
    return fig


# --- 8. Subagente e contexto isolado ----------------------------------------


def fig_subagente():
    """Custo real de delegar, com os números do simulador oficial."""
    fig, ax = plt.subplots(figsize=(10.5, 4.9))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 5.4)
    _limpa(ax)

    # Contexto principal
    ax.add_patch(
        FancyBboxPatch(
            (0.3, 0.7),
            4.2,
            4.1,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor=E.FUNDO_CAIXA,
            edgecolor=E.LINHA,
            linewidth=1.2,
        )
    )
    ax.text(2.4, 4.5, "contexto principal", ha="center", fontsize=12, color=E.TEXTO, weight="bold")
    _caixa(ax, 0.75, 3.35, 3.3, 0.62, "abrir subagente\n80 tokens", E.ACENTO, fonte=10.5)
    _caixa(ax, 0.75, 1.35, 3.3, 0.62, "resumo devolvido\n420 tokens", E.OK, fonte=10.5)
    ax.text(
        2.4,
        0.95,
        "total: 500 tokens",
        ha="center",
        fontsize=11,
        color=E.TEXTO,
        weight="bold",
    )

    # Contexto do subagente
    ax.add_patch(
        FancyBboxPatch(
            (6.3, 0.7),
            4.4,
            4.1,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor="#FFFFFF",
            edgecolor=E.ACENTO,
            linewidth=1.2,
            linestyle="--",
        )
    )
    ax.text(8.5, 4.5, "contexto do subagente", ha="center", fontsize=12, color=E.ACENTO, weight="bold")
    leituras = ["ler session.ts", "ler timeouts.ts", "ler config/*.ts", "ler auth.ts", "ler middleware.ts", "ler testes"]
    for i, leitura in enumerate(leituras):
        y = 3.75 - i * 0.44
        ax.add_patch(
            FancyBboxPatch(
                (6.7, y),
                3.6,
                0.34,
                boxstyle="round,pad=0.005,rounding_size=0.03",
                facecolor=E.NEUTRO,
                alpha=0.5,
                edgecolor="none",
            )
        )
        ax.text(8.5, y + 0.17, leitura, ha="center", va="center", fontsize=9.5, color=E.TEXTO)
    ax.text(
        8.5,
        1.05,
        "milhares de tokens,\nnenhum no contexto principal",
        ha="center",
        fontsize=9.5,
        color=E.TEXTO_FRACO,
    )

    _seta(ax, (4.15, 3.66), (6.6, 3.66), cor=E.ACENTO, lw=1.6)
    _seta(ax, (6.6, 1.66), (4.15, 1.66), cor=E.OK, lw=1.6)
    ax.text(5.4, 3.85, "tarefa", ha="center", fontsize=9.5, color=E.ACENTO)
    ax.text(5.4, 1.85, "resultado", ha="center", fontsize=9.5, color=E.OK)
    ax.text(
        5.5,
        0.2,
        "Delegar não é só paralelizar: é comprar janela de contexto.",
        ha="center",
        fontsize=11.5,
        color=E.TEXTO,
    )
    return fig


# --- 9. Skill, references e carregamento sob demanda ------------------------


def fig_skill_references():
    fig, ax = plt.subplots(figsize=(10.4, 4.7))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 5)
    _limpa(ax)

    _caixa(ax, 0.4, 3.6, 3.0, 0.95, "CLAUDE.md\nentra sempre", E.CAMADA_A, fonte=11.5, negrito=True)
    ax.text(1.9, 3.35, "custo fixo, todo turno", ha="center", fontsize=9.5, color=E.TEXTO_FRACO)

    _caixa(ax, 4.1, 3.6, 3.0, 0.95, "descrição da skill\nsempre em contexto", E.CAMADA_C, fonte=11, negrito=True)
    ax.text(4.15, 3.35, "poucas centenas de tokens", ha="left", fontsize=9.5, color=E.TEXTO_FRACO)

    _caixa(ax, 4.1, 1.95, 3.0, 0.85, "SKILL.md\ncarrega ao ser usada", E.CAMADA_C, fonte=11, alpha=0.75)
    _seta(ax, (6.75, 3.55), (6.75, 2.85), cor=E.CAMADA_C)

    for i, (nome, desc) in enumerate(
        [("references/*.md", "lido só quando citado"), ("scripts/*.py", "executado, não lido"), ("assets/", "template, esquema")]
    ):
        y = 2.55 - i * 0.78
        _caixa(ax, 7.8, y, 2.9, 0.6, "", "#FFFFFF", fonte=10)
        ax.add_patch(
            FancyBboxPatch(
                (7.8, y),
                2.9,
                0.6,
                boxstyle="round,pad=0.01,rounding_size=0.05",
                facecolor="none",
                edgecolor=E.CAMADA_C,
                linewidth=1.1,
                linestyle="--",
            )
        )
        ax.text(9.25, y + 0.38, nome, ha="center", fontsize=10.5, color=E.TEXTO, family=E.FONTE_MONO)
        ax.text(9.25, y + 0.16, desc, ha="center", fontsize=9, color=E.TEXTO_FRACO)
        _seta(ax, (7.15, 2.35), (7.75, y + 0.3), cor=E.NEUTRO, lw=1.0, curva=0.15)

    ax.text(
        0.4,
        0.75,
        "Progressive disclosure: quarenta páginas de referência custam zero até o dia em que fazem falta.",
        fontsize=11.5,
        color=E.TEXTO,
    )
    ax.text(
        0.4,
        0.35,
        "Procedimento fica no SKILL.md. Configuração fica nos arquivos de apoio.",
        fontsize=10.5,
        color=E.TEXTO_FRACO,
    )
    return fig


# --- 10. Três produtos, uma base conceitual ---------------------------------


def fig_tres_produtos():
    fig, ax = plt.subplots(figsize=(10.4, 4.6))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 5)
    _limpa(ax)

    _caixa(
        ax,
        0.5,
        0.55,
        10.0,
        1.15,
        "mesma base conceitual: janela · sessão · modelos · tool use · skills · references · subagents",
        E.FUNDO_SECAO,
        fonte=12,
    )

    produtos = [
        ("Claude Chat", ["conversa e leitura", "Projects e memória", "connectors"], 0.5, E.CAMADA_A),
        ("Claude Cowork", ["trabalho delegado", "dispatch", "agent teams"], 4.0, E.CAMADA_B),
        ("Claude Code", ["agente no repositório", "CLAUDE.md, skills, hooks", "terminal, IDE, desktop, web"], 7.5, E.CAMADA_C),
    ]
    for nome, itens, x, cor in produtos:
        _caixa(ax, x, 2.35, 3.0, 2.1, "", cor)
        ax.text(x + 1.5, 4.05, nome, ha="center", fontsize=13, color=E.TEXTO_NEGATIVO, weight="bold", zorder=3)
        for i, item in enumerate(itens):
            ax.text(
                x + 1.5,
                3.55 - i * 0.36,
                item,
                ha="center",
                fontsize=10,
                color=E.TEXTO_NEGATIVO,
                alpha=0.92,
                zorder=3,
            )
        _seta(ax, (x + 1.5, 2.3), (x + 1.5, 1.78), cor=E.NEUTRO, lw=1.2)

    ax.text(
        5.5,
        0.2,
        "Três portas para o mesmo prédio. O que muda é a interface, não o mecanismo.",
        ha="center",
        fontsize=11,
        color=E.TEXTO_FRACO,
    )
    return fig


# --- 11. Compaction ----------------------------------------------------------


def fig_compaction():
    fig, ax = plt.subplots(figsize=(10.2, 3.9))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 4.2)
    _limpa(ax)

    ax.add_patch(
        FancyBboxPatch(
            (0.4, 1.5),
            4.3,
            2.0,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            facecolor=E.ACENTO_CLARO,
            edgecolor="none",
        )
    )
    ax.text(2.55, 3.7, "janela saturada", ha="center", fontsize=12, color=E.TEXTO, weight="bold")
    ax.text(2.55, 2.5, "histórico completo", ha="center", fontsize=11, color=E.TEXTO_NEGATIVO)

    _seta(ax, (4.95, 2.5), (6.3, 2.5), cor=E.TEXTO_FRACO, lw=1.6)
    ax.text(5.6, 2.75, "compaction", ha="center", fontsize=10.5, color=E.TEXTO)

    ax.add_patch(
        FancyBboxPatch(
            (6.55, 2.28),
            0.55,
            0.45,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            facecolor=E.ACENTO,
            edgecolor="none",
        )
    )
    ax.text(7.4, 2.5, "≈ 12% do volume anterior", va="center", fontsize=11.5, color=E.TEXTO)
    ax.text(
        6.55,
        1.55,
        "o que foi resumido perdeu detalhe:\nsalva-vidas, não é de graça",
        fontsize=10.5,
        color=E.ALERTA,
        linespacing=1.5,
    )
    ax.text(
        0.4,
        0.55,
        "Por isso a decisão consciente entre compactar e abrir sessão nova.",
        fontsize=11,
        color=E.TEXTO_FRACO,
    )
    return fig


# --- 12. Harness: a aplicação em volta do modelo ----------------------------


def fig_harness():
    """Quem faz o trabalho. O modelo é uma função de texto para texto."""
    fig, ax = plt.subplots(figsize=(11.4, 5.0))
    ax.set_xlim(0, 12.8)
    ax.set_ylim(0, 5.4)
    _limpa(ax)

    # Você
    _caixa(ax, 0.25, 2.35, 1.95, 1.5, "", E.FUNDO_CAIXA)
    ax.text(1.22, 3.5, "você", ha="center", fontsize=12.5, color=E.TEXTO, weight="bold", zorder=3)
    ax.text(
        1.22,
        2.95,
        "prompt\narquivos\ncomandos",
        ha="center",
        va="center",
        fontsize=9.5,
        color=E.TEXTO_FRACO,
        linespacing=1.5,
        zorder=3,
    )

    # Harness
    _caixa(ax, 2.9, 1.15, 5.3, 3.6, "", E.ACENTO)
    ax.text(5.55, 4.35, "harness", ha="center", fontsize=14, color=E.TEXTO_NEGATIVO, weight="bold", zorder=3)
    ax.text(
        5.55,
        4.05,
        "Claude Code, Chat, Cowork",
        ha="center",
        fontsize=9.5,
        color=E.TEXTO_NEGATIVO,
        alpha=0.85,
        zorder=3,
    )
    tarefas = [
        "injeta system prompt, CLAUDE.md e skills",
        "reenvia o histórico a cada turno",
        "executa a ferramenta que o modelo pediu",
        "aplica o portão de permissões",
        "gerencia a janela e compacta",
        "abre subagentes e consolida o retorno",
    ]
    for i, tarefa in enumerate(tarefas):
        y = 3.62 - i * 0.42
        ax.text(3.2, y, "·", fontsize=13, color=E.TEXTO_NEGATIVO, va="center", zorder=3)
        ax.text(3.45, y, tarefa, fontsize=9.8, color=E.TEXTO_NEGATIVO, va="center", zorder=3)

    # Modelo
    _caixa(ax, 9.5, 2.35, 2.9, 1.5, "", E.NEUTRO)
    ax.text(10.95, 3.5, "modelo", ha="center", fontsize=12.5, color=E.TEXTO, weight="bold", zorder=3)
    ax.text(
        10.95,
        2.95,
        "recebe texto,\ndevolve texto.\nMais nada.",
        ha="center",
        va="center",
        fontsize=9.8,
        color=E.TEXTO,
        linespacing=1.5,
        zorder=3,
    )

    _seta(ax, (2.25, 3.35), (2.85, 3.35), cor=E.TEXTO_FRACO, lw=1.6)
    _seta(ax, (8.3, 3.35), (9.45, 3.35), cor=E.ACENTO, lw=1.6)
    _seta(ax, (9.45, 2.65), (8.3, 2.65), cor=E.TEXTO_FRACO, lw=1.6)
    ax.text(8.87, 3.52, "requisição", ha="center", fontsize=9, color=E.ACENTO)
    ax.text(8.87, 2.28, "resposta", ha="center", fontsize=9, color=E.TEXTO_FRACO)

    ax.text(
        0.25,
        0.6,
        "Você nunca fala com o modelo: fala com o harness, que fala com o modelo.",
        fontsize=11.5,
        color=E.TEXTO,
    )
    ax.text(
        0.25,
        0.2,
        "A resposta que sai do modelo é texto. Quem executa qualquer coisa a partir dela é o harness.",
        fontsize=10.5,
        color=E.TEXTO_FRACO,
    )
    return fig


# --- 13. As mensagens trocadas entre harness e modelo -----------------------


def fig_mensagens():
    """Um turno completo: o que vai, o que volta, e por que o laço repete."""
    fig, ax = plt.subplots(figsize=(13.2, 5.5))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 6.35)
    _limpa(ax)

    ax.text(2.5, 6.05, "harness", ha="center", fontsize=13, color=E.ACENTO, weight="bold")
    ax.text(10.5, 6.05, "modelo", ha="center", fontsize=13, color=E.TEXTO_FRACO, weight="bold")
    for x in (2.5, 10.5):
        ax.plot([x, x], [0.3, 5.85], color=E.LINHA, linewidth=1.1, zorder=1)

    # (lado, y, título, linhas, cor, rótulo da seta)
    trocas = [
        ("→", 5.2, "requisição",
         ['system: "você é um assistente…"',
          'messages: [ {role: "user", content: [text]} ]',
          'tools: [ {name: "read_file", input_schema} ]'],
         E.ACENTO, "o harness monta e envia"),
        ("←", 3.72, "resposta  ·  stop_reason: tool_use",
         ['{role: "assistant", content: [',
          '  {type: "thinking"}, {type: "text"},',
          '  {type: "tool_use", id: "tu_01", input: {…}} ] }'],
         E.TEXTO_FRACO, "o modelo pede uma ferramenta"),
        ("→", 2.12, "nova requisição",
         ['{role: "user", content: [',
          '  {type: "tool_result", tool_use_id: "tu_01",',
          '   content: "…", is_error: false} ] }'],
         E.ACENTO, "histórico inteiro + resultado da execução"),
        ("←", 0.6, "resposta  ·  stop_reason: end_turn",
         ['{role: "assistant", content: [ {type: "text"} ] }'],
         E.OK, "o laço encerra"),
    ]

    for sentido, y, titulo, linhas, cor, legenda in trocas:
        altura = 0.46 + 0.30 * len(linhas)
        _caixa(ax, 3.1, y - altura + 0.55, 6.8, altura, "", cor, alpha=0.10)
        ax.add_patch(
            FancyBboxPatch(
                (3.1, y - altura + 0.55),
                6.8,
                altura,
                boxstyle="round,pad=0.02,rounding_size=0.06",
                facecolor="none",
                edgecolor=cor,
                linewidth=1.1,
                zorder=3,
            )
        )
        ax.text(3.42, y + 0.3, titulo, fontsize=12, color=cor, weight="bold", zorder=4)
        ax.text(9.6, y + 0.3, legenda, ha="right", fontsize=10, color=E.TEXTO_FRACO, zorder=4)
        for i, linha in enumerate(linhas):
            ax.text(
                3.42,
                y - 0.04 - i * 0.30,
                linha,
                fontsize=10.8,
                family=E.FONTE_MONO,
                color=E.TEXTO,
                zorder=4,
            )
        if sentido == "→":
            _seta(ax, (2.55, y + 0.3), (3.05, y + 0.3), cor=cor, lw=1.6)
            _seta(ax, (9.95, y + 0.3), (10.45, y + 0.3), cor=cor, lw=1.6)
        else:
            _seta(ax, (10.45, y + 0.3), (9.95, y + 0.3), cor=cor, lw=1.6)
            _seta(ax, (3.05, y + 0.3), (2.55, y + 0.3), cor=cor, lw=1.6)

    ax.text(
        0.35,
        0.12,
        "Tudo é texto estruturado. O modelo não chama a função: ele devolve um bloco tool_use, e o harness decide o que fazer com ele.",
        fontsize=11.5,
        color=E.TEXTO,
    )
    return fig


FIGURAS = {
    nome[4:].replace("_", "-"): fn
    for nome, fn in sorted(globals().items())
    if nome.startswith("fig_") and callable(fn)
}


def gerar(nomes=None):
    SAIDA.mkdir(parents=True, exist_ok=True)
    alvos = nomes or sorted(FIGURAS)
    for nome in alvos:
        if nome not in FIGURAS:
            raise SystemExit(f"figura desconhecida: {nome}\ndisponíveis: {', '.join(sorted(FIGURAS))}")
        fig = FIGURAS[nome]()
        destino = SAIDA / f"{nome}.png"
        fig.savefig(destino, dpi=E.FIG_DPI, bbox_inches="tight", pad_inches=0.18, transparent=True)
        plt.close(fig)
        print(f"gerada  {destino.relative_to(SAIDA.parents[2])}")


if __name__ == "__main__":
    gerar(sys.argv[1:] or None)
