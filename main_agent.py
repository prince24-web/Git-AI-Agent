# -*- coding: utf-8 -*-
import getpass
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI

# import all your Git tools
from functions import (
    git_add, git_clone, git_commit, git_create_branch, git_first_push,
    git_init, git_list_branches, git_log, git_merge, git_pull,
    git_push, git_reset, git_status, git_switch_branch
)

# ----------------------------
# 1. Load environment variables
# ----------------------------
load_dotenv()

import os
if not os.getenv("GEMINI_API_KEY"):
    os.environ["GEMINI_API_KEY"] = getpass.getpass("Enter your Gemini API key: ")

# ----------------------------
# 2. Setup LLM
# ----------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# ----------------------------
# 3. Register tools
# ----------------------------
tools = [
    git_init,
    git_clone,
    git_status,
    git_add,
    git_commit,
    git_first_push,
    git_push,
    git_pull,
    git_list_branches,
    git_create_branch,
    git_switch_branch,
    git_merge,
    git_log,
    git_reset,
]

# ----------------------------
# 4. Initialize Agent
# ----------------------------
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# ----------------------------
# 5. Test Agent
# ----------------------------
agent.run("what is my git status")