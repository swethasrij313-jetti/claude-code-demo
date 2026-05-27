# Claude Code Multi-Agent Demo

# Goal of This Project

The goal of this project is to understand how modern AI agent systems work behind the scenes.

Instead of building a simple chatbot, this project demonstrates how AI systems can:
- understand a user question
- decide which tool to use
- execute actions
- generate a response
- organize workflows using modular architecture

This project was inspired by Claude-style AI orchestration systems and multi-agent workflows used in modern GenAI applications.

The project is intentionally designed in a beginner-friendly way so even non-technical users can understand how agent-based AI systems operate.

---

# Problem Statement

In real-world AI systems, a single AI model usually does not handle everything alone.

Modern AI applications often need:
- reasoning agents
- external tools
- workflow orchestration
- memory handling
- routing systems
- modular architecture

For example:

A user may ask:

"Why are flights delayed?"

The AI system must:
1. understand the question
2. determine what information is needed
3. choose the correct tool
4. retrieve data
5. generate a final response

This project simulates that workflow using a simplified modular AI architecture.

---

# What This Project Demonstrates

This project demonstrates:

- Multi-agent workflow design
- Planner agent routing
- Tool orchestration
- MCP-style architecture
- Modular Python project structure
- SQL-style tool execution
- Claude-style response generation

---

# High-Level Workflow

User Question
↓
Planner Agent
↓
Tool Selection
↓
Tool Execution
↓
Response Generation

---

# Example Workflow

User asks:

"Why are flights delayed?"

The Planner Agent analyzes the question and determines that flight delay information is needed.

The planner selects the SQL tool.

The SQL tool simulates execution of:

SELECT * FROM flight_delays

The system then generates a Claude-style response:

"Weather congestion caused delays."

---

# Why Modular Architecture Matters

Instead of placing all logic into one large file, the project separates responsibilities into multiple modules.

This is how real-world AI systems are designed because modular systems are:
- easier to maintain
- easier to scale
- easier to debug
- easier to extend

Each component has a dedicated responsibility.

---

# Project Structure