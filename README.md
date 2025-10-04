# Prompts

Red Team AI prompts

Crafting prompts for AI also referred to as "Prompt Engineering" is one of the keys to success with using AI. This repo will contain prompts in different formats that are meant to be used for performing Red Teaming.

## Basic usage

There're 3 different types of usage

### Prompt files

*.prompt.yml files can be used with the models tab. 

See Resources for more details

### Agent files

The content of *.agent files can be pasted into any AI agent

### CLI tool

Or use the cli (see install and usage below)

## Install requirements for CLI usage (Easy install)

```zsh
python3 -m pip install -r requirements.txt
```

## Using VS Code for development or install (Usage in VSCode)

```zsh
shift + command (⌘) + P -> Python: Create Environment
```

Creates a new environment after following the instructions (all dependencies should be added automatically)

* [Python Environments in VS Code](https://code.visualstudio.com/docs/python/environments)

```zsh
source .venv/bin/activate
```

Activate environment (Automatically loaded when opening VSCode...usually)

## Using terminal for development or install (Terminal only)

```zsh
apt install python3-venv python3-pip
```

Install Python3 Virtual Environments and Python3 pip

```zsh
python3 -m venv .venv
```

Create virtual environment (from Tacticontainer root folder)

```zsh
source .venv/bin/activate
```

Activate environment

## CLI example usage

```zsh

EXPORT GITHUB_TOKEN=<github_PAT_token>

```

Add the GitHub PAT token to your environment variables. Personal Access Token must have models scope (See Resources for more info)

```zsh
python gh_models_cli.py "Create scan that checks for the top 10 open Kubernetes ports"
nmap -p 6443,443,2379,2380,10250,10255,10257,10259,30000-32767 --open -sV TARGET_IP
```

Create a Kubernetes specific scan for top 10 ports (All output by default is one command unless you specify --system)

## Resources
* https://docs.github.com/en/github-models/about-github-models
