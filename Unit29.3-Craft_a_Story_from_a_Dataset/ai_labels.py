"""Shared labeling helpers and terminology lists for the GitHub trend notebook."""

from __future__ import annotations
from unicodedata import name

import pandas as pd

# Exact repository names for projects that are specifically agentic/workflow oriented.
AGENTIC_EXACT_NAMES = {
    "adk-go",
    "aichat",
    "agentgpt",
    "agent-zero",
    "awesome-llm-apps",
    "autogen",
    "autogpt",
    "browser-use",
    "claude-code",
    "dify",
    "everything-claude-code",
    "fastmcp",
    "firecrawl",
    "gemini-cli",
    "khoj",
    "langchain",
    "langflow",
    "lobe-chat",
    "markitdown",
    "mcp",
    "metagpt",
    "n8n",
    "openagents",
    "openclaw",
    "openai_agent_swarm",
    "open-webui",
    "opencode",
    "openhands",
    "rd-agent",
    "sim",
    "skills",
    "superpowers",
    "system-prompts-and-models-of-ai-tools",
    "webagent",
    "xagent",
}

# Exact repository names for projects that are specifically AI/ML oriented.
AI_EXACT_NAMES = {
    "aibrix",
    "aisuite",
    "candle",
    "comfyui",
    "deepseek-v3",
    "fooocus",
    "generative-ai-for-beginners",
    "gpt4all",
    "llama.cpp",
    "ollama",
    "prompts.chat",
    "pytorch",
    "stable-diffusion-webui",
    "tensorflow",
    "transformers",
}
# Agentic projects are a subset of AI projects, so we add all agentic exact names to the broader AI list.
AI_EXACT_NAMES.update(AGENTIC_EXACT_NAMES)

# Agentic-specific terminology that may appear in repo names.
AGENTIC_TERMS = [
    "agentgpt",
    "agent-zero",
    "agentic",
    "agent-sdk",
    "agent-swarm",
    "agent_swarm",
    "agents",
    "ai-agent",
    "ai-agents-for-beginners",
    "assistant",
    "autogen",
    "avante.nvim",
    "browser-use",
    "claude-code",
    "codex",
    "cover-agent",
    "crewai",
    "cursor",
    "dify",
    "fastapi_mcp",
    "gpt-engineer",
    "gpt-pilot",
    "jobs_applier_ai_agent",
    "langchain",
    "langflow",
    "langgraph",
    "mcp",
    "metagpt",
    "multi-agent",
    "openagents",
    "openai-agent",
    "openai_agent",
    "openclaw",
    "opencode",
    "open-interpreter",
    "openhands",
    "orchestr",
    "privategpt",
    "rd-agent",
    "screenshot-to-code",
    "swe-agent",
    "tradingagents",
    "webagent",
    "workflow",
    "xagent",
    "zen-mcp-server",
]

# Broad AI terms that are not already covered by `AGENTIC_TERMS`.
AI_TERMS = [
    "ai-assistant",
    "ai-chatbot",
    "ai-code-translator",
    "ai-expert-roadmap",
    "ai-for-beginners",
    "ai-getting-started",
    "ai-hedge-fund",
    "ai-toolkit",
    "aibrix",
    "aigc",
    "airi",
    "aidea",
    "awesome-ai",
    "awesome-chatgpt-prompts",
    "awesome-copilot",
    "awesome-gpts",
    "awesome-llm-apps",
    "chatbot-ui",
    "chatdev",
    "chatgpt",
    "claude",
    "cline",
    "colossalai",
    "computervision",
    "comfyui",
    "controlnet",
    "crawl4ai",
    "dalle-mini",
    "deep-live-cam",
    "deepseek",
    "diffusion",
    "docsgpt",
    "dreambooth-stable-diffusion",
    "edgegpt",
    "fingpt",
    "freedomgpt",
    "gemini",
    "genai",
    "generative-ai",
    "generative_agents",
    "gpt",
    "gpt-",
    "gpt_",
    "gpt3",
    "gpt4",
    "gptme",
    "gpts",
    "krillinai",
    "kubectl-ai",
    "lawgpt",
    "llama",
    "llm",
    "llms-from-scratch",
    "localai",
    "localgpt",
    "lobe-chat",
    "lora",
    "markitdown",
    "machine-learning",
    "memgpt",
    "mi-gpt",
    "mingpt",
    "mistral",
    "moneyprinterturbo",
    "multimodal",
    "nanogpt",
    "neural",
    "next-gpt",
    "open-assistant",
    "open-webui",
    "openai",
    "openai-cookbook",
    "pandas-ai",
    "pydantic-ai",
    "picogpt",
    "prompt",
    "practicalai",
    "rag",
    "roo",
    "scrapegraph-ai",
    "shortgpt",
    "simstudioai/sim",
    "spring-ai",
    "stable-diffusion",
    "text-generation-webui",
    "tinygrad",
    "transformer",
    "vllm",
    "vision-language",
    "whisper.cpp",
    "xcoder",
]
# Agentic-specific terms are a subset of broader AI terms, so we add all agentic terms to the AI list.
AI_TERMS.extend(AGENTIC_TERMS)
AI_TERMS = sorted(set(AI_TERMS))

# Terms for learning-oriented repositories and curriculum-style collections.
LEARNING_TERMS = [
    "100-days",
    "30-days",
    "algorithms",
    "architect-awesome",
    "app-ideas",
    "awesome-",
    "awesome-design",
    "book-of-secret-knowledge",
    "bootcamp",
    "best-websites-a-programmer-should-visit",
    "build-your-own",
    "cheatsheet",
    "cheatsheets",
    "chinatextbook",
    "coding-interview-university",
    "computer-science",
    "course",
    "courses",
    "coursera",
    "cs-notes",
    "cs-self-learning",
    "cs-video-courses",
    "data-engineering-zoomcamp",
    "developer-roadmap",
    "devops-exercises",
    "every-programmer-should-know",
    "first-contributions",
    "for-beginners",
    "free-for-dev",
    "free-programming-books",
    "fucking-algorithm",
    "freecodecamp",
    "git-flight-rules",
    "github-chinese-top-charts",
    "google-interview-university",
    "guide",
    "handbook",
    "hello-algo",
    "hellogithub",
    "howtocook",
    "interview",
    "interviews",
    "javaguide",
    "javascript-algorithms",
    "javascript-questions",
    "leetcode",
    "llm-course",
    "ml-for-beginners",
    "nodebestpractices",
    "python-cheatsheet",
    "project-based-learning",
    "public-apis",
    "questions",
    "roadmap",
    "system-design-primer",
    "tech-interview-handbook",
    "the-art-of-command-line",
    "30-seconds-of-code",
    "web-dev-for-beginners",
    "you-dont-know-js",
]

# Terms for developer tooling, editors, terminals, and infra utilities.
TOOL_TERMS = [
    "dotfiles",
    "atom",
    "bashtop",
    "black",
    "build-your-own-x",
    "code-server",
    "codeedit",
    "croc",
    "cypress",
    "deno",
    "ghidra",
    "helix",
    "imhex",
    "it-tools",
    "lapce",
    "lazyvim",
    "neovim",
    "nano",
    "nvim",
    "nvm",
    "obsidian",
    "ohmyzsh",
    "nuclide",
    "playwright",
    "powertoys",
    "powershell",
    "rustdesk",
    "sherlock",
    "scrcpy",
    "stremio-web",
    "surrealdb",
    "terminal",
    "termux",
    "tool",
    "tooljet",
    "ventoy",
    "vim",
    "vscode",
    "gitignore",
    "winget",
    "youtube-dl",
    "yt-dlp",
]

# Terms for DevOps, cloud, infrastructure, deployment, and ops-heavy utilities.
DEVOPS_TERMS = [
    "airflow",
    "ansible",
    "argo",
    "consul",
    "docker",
    "elasticsearch",
    "frp",
    "grafana",
    "gradle",
    "helm",
    "istio",
    "jenkins",
    "k8s",
    "kafka",
    "kibana",
    "kubernetes",
    "linux",
    "logstash",
    "minikube",
    "nginx",
    "nomad",
    "prometheus",
    "terraform",
    "traefik",
    "vault",
]

# Terms for frontend/backend frameworks plus notable UI libraries and kits.
FRAMEWORK_TERMS = [
    "android",
    "ant-design",
    "angular",
    "bootstrap",
    "chakra-ui",
    "create-react-app",
    "daisyui",
    "device-mockups",
    "django",
    "electron",
    "font-awesome",
    "flutter",
    "godot",
    "headlessui",
    "heroui",
    "ionic-framework",
    "json",
    "kotlin",
    "material-ui",
    "next.js",
    "nprogress",
    "parallax",
    "postal",
    "quill",
    "react",
    "react-native",
    "storybook",
    "svelte",
    "spring-",
    "tabler",
    "tailwindcss",
    "tauri",
    "vue",
    "vue-element-admin",
    "vue-vben-admin",
    "vuetify",
    "webpack",
]

# Terms for popular languages and general-purpose libraries that show up as repo names.
LIBRARIES_TERMS = [
    "alamofire",
    "axios",
    "d3",
    "discord.js",
    "fastapi",
    "flask",
    "golang",
    "node",
    "javascript",
    "julia",
    "matplotlib",
    "numpy",
    "opencv",
    "pandas",
    "protobuf",
    "python",
    "react-hook-form",
    "react-router",
    "rust",
    "rxswift",
    "scikit",
    "three.js",
    "typescript",
]

# Terms for repositories tied to a specific news cycle, moment, or social issue.
CURRENT_TERMS = [
    "996.icu",
    "bitcoin",
    "chia-blockchain",
    "corona-warn-app",
    "coronatracker",
    "covid",
    "covid-19",
    "covid19",
    "doge",
    "dogecoin",
    "gamestonk",
    "gamestonkterminal",
    "jd_seckill",
    "jd_maotai_seckill",
    "maotai",
    "miaosha",
    "reddit-stock-trends",
    "seckill",
    "stock",
    "stock-trends",
    "taobao_seckill",
]

# Organization/developer handles that represent companies or corporate-backed projects.
CORP_DEVS = [
    "amazon",
    "anthropic",
    "apache",
    "apple",
    "bytedance",
    "deepseek",
    "facebook",
    "google",
    "huggingface",
    "ibm",
    "meta",
    "microsoft",
    "azure",
    "mozilla",
    "netflix",
    "nvidia",
    "openai",
    "salesforce",
    "shopify",
    "spotify",
    "tensorflow",
    "tesla",
    "twitter",
    "uber",
]

# VC-funded startup or startup-backed open source organization handles.
STARTUP_DEVS = [
    "activepieces",
    "airbyte",
    "apollo",
    "apollographql",
    "artillery",
    "anysphere",
    "berriai",
    "better-auth",
    "browser-use",
    "bun",
    "calcom",
    "chatwoot",
    "continue",
    "continuedev",
    "comfy-org",
    "evidently",
    "evidentlyai",
    "elementary-data",
    "firecrawl",
    "flowise",
    "flowiseai",
    "grafana",
    "growthbook",
    "highlight",
    "hyperdx",
    "infisical",
    "influxdata",
    "khoj",
    "lancedb",
    "langchain",
    "langfuse",
    "langflow",
    "langgenius",
    "litellm",
    "mastra",
    "mattermost",
    "mem0",
    "mindsdb",
    "mintplex",
    "n8n",
    "ollama",
    "onyx",
    "openreplay",
    "open-webui",
    "oven",
    "paradedb",
    "payload",
    "payloadcms",
    "posthog",
    "questdb",
    "refine",
    "refinedev",
    "reflex",
    "replicate",
    "signoz",
    "skyvern",
    "sst",
    "supabase",
    "supertokens",
    "tooljet",
    "trigger",
    "triggerdotdev",
    "twenty",
    "twentyhq",
    "unsloth",
    "unslothai",
    "wasmer",
    "wasp",
    "windmill",
    "windmill-labs",
]

# Themes that categorize the repositories.
THEMES = [
    "Frameworks and UI",
    "DevOps / infra",
    "Languages / libraries",
    "Learning resources",
    "Developer tools",
    "AI / ML",
    "Agentic",
    "Current events / social",
    "Other",
]

def is_ai_repo(repo_name: str) -> bool:
    """Return True when a repository name looks AI-related."""

    repo_name = str(repo_name).lower()
    if "/" in repo_name:
        repo_name = repo_name.split("/")[-1]
    return repo_name in AI_EXACT_NAMES or any(term in repo_name for term in AI_TERMS)


def is_agentic_repo(repo_name: str) -> bool:
    """Return True when a repository name looks agentic/workflow-oriented."""

    repo_name = str(repo_name).lower()
    if "/" in repo_name:
        repo_name = repo_name.split("/")[-1]
    return repo_name in AGENTIC_EXACT_NAMES or any(term in repo_name for term in AGENTIC_TERMS)


def is_corp_dev(name: str) -> bool:
    """Return True when a developer or repo owner matches a known company handle."""

    dev_name = str(name).strip().lower()
    if "/" in dev_name:
        dev_name = dev_name.split("/", 1)[0]
    return any(corp in dev_name for corp in CORP_DEVS)


def is_startup_dev(name: str) -> bool:
    """Return True when a developer or repo owner matches a known startup handle."""

    dev_name = str(name).strip().lower()
    if "/" in dev_name:
        dev_name = dev_name.split("/", 1)[0]
    return any(startup in dev_name for startup in STARTUP_DEVS)


def classify_theme(repo_name: str) -> list[str]:
    """Return every broad story bucket that matches a repository name."""

    repo_name = str(repo_name).lower()
    if "/" in repo_name:
        repo_name = repo_name.split("/")[-1]
    themes = []

    if repo_name in AI_EXACT_NAMES or any(term in repo_name for term in AI_TERMS):
        themes.append("AI / ML")
    if repo_name in AGENTIC_EXACT_NAMES or any(term in repo_name for term in AGENTIC_TERMS):
        themes.append("Agentic")
    if any(term in repo_name for term in LEARNING_TERMS):
        themes.append("Learning resources")
    if any(term in repo_name for term in TOOL_TERMS):
        themes.append("Developer tools")
    if any(term in repo_name for term in DEVOPS_TERMS):
        themes.append("DevOps / infra")
    if any(term in repo_name for term in LIBRARIES_TERMS):
        themes.append("Languages / libraries")
    if any(term in repo_name for term in FRAMEWORK_TERMS):
        themes.append("Frameworks and UI")
    if any(term in repo_name for term in CURRENT_TERMS):
        themes.append("Current events / social")
    if not themes:
        themes.append("Other")

    return themes


def first_crossing(series: pd.Series, threshold: float, start: str = "2022-01-01") -> str | None:
    """Return the first YYYY-MM where a time-indexed series crosses `threshold`."""

    window = series.copy()
    window.index = pd.to_datetime(window.index)
    window = window.loc[pd.Timestamp(start):]
    hits = window[window >= threshold]
    if hits.empty:
        return None
    return hits.index[0].strftime("%Y-%m")
