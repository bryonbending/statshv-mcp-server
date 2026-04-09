# Planning MCP Server with VeoliaSecureGPT

## Overview
This MCP Server exposes the `planning` MySQL database (MySQL 8.0.43) as a set of
structured tools consumable by any MCP-compatible LLM client. It integrates with
**VeoliaSecureGPT** for natural language understanding and SQL generation.

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
