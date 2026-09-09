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
| sessão | `code/sessions.md`, `code/agent-sdk--sessions.md` |
| janela de contexto | `code/costs.md`, `code/sessions.md` |
| modelos | `code/model-config.md`, `chat/*choose-a-claude-plan*` |
| thinking / effort | `code/model-config.md`, `code/settings.md` |
| skills | `chat/skills--overview.md`, `chat/skills--how-to.md`, `code/skills.md` |
| references (arquivos de apoio de skill) | `code/skills.md` (seção "Add supporting files"), `chat/skills--how-to.md` (seção "Adding resources") |
| memória / CLAUDE.md (não confundir com references) | `code/memory.md` |
| subagents | `code/sub-agents.md`, `code/agent-sdk--subagents.md`, `code/agent-teams.md` |
| agente orquestrador | `code/agent-sdk--agent-loop.md`, `cowork/cowork--guide--dispatch.md` |
