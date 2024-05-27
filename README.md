# ai-assistant-customer-service

E2E AI Assistant for Customer Service

## Getting Started

### Prerequisites

- [Conda](https://conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
- [OpenAI API Key](https://platform.openai.com/api-keys/)

### Installation (using conda)

```bash
# Setup conda
conda init zsh # Optional: Initialize conda for zsh
conda config --add channels conda-forge # Add conda-forge channel to install tiktoken and python-dotenv

# Create a new conda environment "ai-dev"
conda create -n ai-dev python=3.11 openai tiktoken python-dotenv python-dotenv-with-cli
conda info --envs

# Activate the conda environment
conda activate ai-dev

```

> Note: When using VS Code, click on the Python version and select the conda environment and then you can use the "Run" button on the top right.

### Environment Variables

Create a `.env` file in the root directory of the project and add the following environment variables:

```bash
OPENAI_API_KEY=your-openai-api-key
```

### Usage

```bash
python main.py
```
