import subprocess
from langchain_core.tools import tool

# -----------------------
# Helper to run shell
# -----------------------
def run_shell(command: str) -> str:
    """Run any shell command and return its output or error message."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stderr or result.stdout
    except Exception as e:
        return str(e)

# -----------------------
# Git Tools
# -----------------------
@tool("git_init", return_direct=True)
def git_init(dummy: str) -> str:
    """Initialize a new Git repository in the current folder."""
    return run_shell("git init")

@tool("git_clone")
def git_clone(url: str) -> str:
    """Clone a remote Git repository from a given URL."""
    return run_shell(f"git clone {url}")

@tool("git_status")
def git_status(dummy: str) -> str:
    """Show the current status of files (staged, unstaged, untracked)."""
    return run_shell("git status")

@tool("git_add")
def git_add(name: str) -> str:
    """Stage files for commit. Use '.' to stage all changes."""
    return run_shell(f"git add {name}")

@tool("git_commit")
def git_commit(message: str) -> str:
    """Commit staged changes with a commit message."""
    return run_shell(f"git commit -m '{message}'")

@tool("git_first_push")
def git_first_push(branch: str) -> str:
    """Push a branch to origin for the first time and set upstream tracking."""
    return run_shell(f"git push -u origin {branch}")

@tool("git_push")
def git_push(dummy: str) -> str:
    """Push committed changes to the remote repository."""
    return run_shell("git push")

@tool("git_pull")
def git_pull(dummy: str) -> str:
    """Fetch and merge the latest changes from the remote repository."""
    return run_shell("git pull")

@tool("git_list_branches")
def git_list_branches(dummy: str) -> str:
    """List all local Git branches."""
    return run_shell("git branch")

@tool("git_create_branch")
def git_create_branch(name: str) -> str:
    """Create a new branch with the given name."""
    return run_shell(f"git branch {name}")

@tool("git_switch_branch")
def git_switch_branch(branch: str) -> str:
    """Switch to a different branch by name."""
    return run_shell(f"git switch {branch}")

@tool("git_merge")
def git_merge(branch: str) -> str:
    """Merge the specified branch into the current branch."""
    return run_shell(f"git merge {branch}")

@tool("git_log")
def git_log(dummy: str) -> str:
    """View the commit history in a compact format."""
    return run_shell("git log --oneline --graph --decorate")

@tool("git_reset")
def git_reset(commit: str) -> str:
    """Reset the repository to a specific commit (dangerous, rewrites history)."""
    return run_shell(f"git reset --hard {commit}")
