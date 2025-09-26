#!/usr/bin/env python3
"""Simple CLI to query a GitHub Models endpoint via the OpenAI-compatible SDK.

Usage:
  python gh_models_cli.py "how would I portscan 1000 webservers for open ports?"

Optional overrides:
  python gh_models_cli.py --system "You are a helpful assistant" "List Linux priv esc checks"
"""

import os
import sys
import argparse
from openai import OpenAI

DEFAULT_SYSTEM = "You're a senior red teamer performing recon. Answer with a single command"
ENDPOINT = "https://models.github.ai/inference"
MODEL = "openai/gpt-4.1-nano"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Query GitHub Models (OpenAI-compatible)")
    parser.add_argument(
        "prompt",
        help="User prompt/content to send (surround in quotes).",
    )
    parser.add_argument(
        "--system",
        dest="system",
        default=DEFAULT_SYSTEM,
        help="Override the system prompt (default: red team recon single command).",
    )
    parser.add_argument(
        "--model",
        dest="model",
        default=MODEL,
        help=f"Model ID to use (default: {MODEL}).",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=1.0,
        help="Sampling temperature (default: 1.0)",
    )
    parser.add_argument(
        "--top-p",
        type=float,
        default=1.0,
        help="Top-p nucleus sampling (default: 1.0)",
    )
    return parser


def main(argv: list[str]) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set", file=sys.stderr)
        return 1

    client = OpenAI(
        base_url=ENDPOINT,
        api_key=token,
    )

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": args.system},
            {"role": "user", "content": args.prompt},
        ],
        temperature=args.temperature,
        top_p=args.top_p,
        model=args.model,
    )

    # Print just the assistant content
    print(response.choices[0].message.content)
    return 0


if __name__ == "__main__":  # pragma: no cover - direct CLI execution
    raise SystemExit(main(sys.argv[1:]))
