# Documentação oficial (espelho local)

Cópia local em Markdown da documentação oficial, baixada em 2026-09-09 para servir de fonte de consulta ao construir os artefatos da apresentação. **Não editar** estes arquivos: são espelho. Correções e notas vão em [docs/](../).

## Organização

| Pasta | Conteúdo | Origem |
|---|---|---|
| `chat/` | Claude (app web/desktop/mobile), projetos, memória, skills, connectors, Chrome | `support.claude.com/en/articles/*`, `claude.com/docs/{skills,connectors}` |
| `cowork/` | Claude Cowork: overview, dispatch, projects, plugins, monitoring, changelog | `support.claude.com` (seção Cowork), `claude.com/docs/cowork/*` |
| `code/` | Claude Code: CLI, IDE, desktop, web, subagents, skills, hooks, MCP, Agent SDK | `code.claude.com/docs/en/*`, `support.claude.com` (seção Claude Code) |

Nomes de arquivo: caminho da URL com `/` trocado por `--`.

## Páginas mais úteis por conceito da apresentação

| Conceito | Arquivos |
|---|---|
| harness | `code/glossary.md` (verbete "Agentic harness"), `code/how-claude-code-works.md` |
| janela de contexto | `code/context-window.md`, `code/costs.md` |
| sessão | `code/sessions.md`, `code/agent-sdk--sessions.md` |
| contexto persistente | `code/memory.md`, `chat/11473015-retrieval-augmented-generation-rag-for-projects.md`, `chat/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context.md` |
| modelos | `code/model-config.md`, `chat/*choose-a-claude-plan*` |
| thinking e effort | `code/model-config.md`, `code/settings.md`, `chat/11095361-when-should-i-use-web-search-extended-thinking-and-research.md` |
| tool use / MCP e connectors | `code/mcp.md`, `code/mcp-quickstart.md`, `chat/11176164-use-connectors-to-extend-claude-s-capabilities.md` |
| skills | `chat/skills--overview.md`, `chat/skills--how-to.md`, `code/skills.md` |
| references (arquivos de apoio de skill) | `code/skills.md` (seção "Add supporting files"), `chat/skills--how-to.md` (seção "Adding resources") |
| subagents | `code/sub-agents.md`, `code/agent-sdk--subagents.md`, `code/agent-teams.md` |
| agente orquestrador | `code/agent-sdk--agent-loop.md`, `cowork/cowork--guide--dispatch.md` |
| permissões e plan mode | `code/permissions.md`, `code/permission-modes.md`, `code/agent-sdk--permissions.md` |
| verificação | Bloco 5 — prática, sem página própria |

## Conceitos de apoio

| Conceito | Arquivos |
|---|---|
| prompt caching / compaction | `code/costs.md`, `code/context-window.md` |
| hooks | `code/hooks-guide.md`, `code/hooks.md` |
| checkpointing | `code/checkpointing.md` |
| privacidade e uso de dados | `code/analytics.md`, artigos de privacidade em `chat/` |
