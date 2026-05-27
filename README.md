# Claude Code Multi-Agent Demo

## Overview
This project demonstrates a Claude-style multi-agent orchestration system using modular Python architecture.

The workflow simulates how AI agents coordinate with tools and routing logic to answer operational questions.

---

## Features

- Planner agent routing
- MCP-style tool orchestration
- SQL tool integration
- Modular Python architecture
- Extensible AI workflow design

---

## Project Structure

```bash
claude-code-demo/
│
├── agents/
│   └── planner_agent.py
│
├── tools/
│   └── sql_tool.py
│
├── mcp/
│   └── server.py
│
├── app/
│   └── main.py
│
├── requirements.txt
└── README.md