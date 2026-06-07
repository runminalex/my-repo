"""
Hermes GitOps Framework - Workflow Demo

A simple demonstration of the multi-agent GitOps workflow:
PM -> Issue -> Branch -> Code -> PR -> Review -> Test -> Merge -> Deploy
"""

import os
import sys
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


class WorkflowState(Enum):
    """States in the GitOps workflow."""
    IDEA = "idea"
    PRD = "prd"
    ISSUE = "issue"
    BRANCH = "branch"
    CODING = "coding"
    PR_OPEN = "pr_open"
    REVIEW = "review"
    FIX = "fix"
    TEST = "test"
    MERGE = "merge"
    DEPLOY = "deploy"
    DONE = "done"


@dataclass
class Task:
    """Represents a unit of work in the workflow."""
    title: str
    description: str
    state: WorkflowState = WorkflowState.IDEA
    branch_name: Optional[str] = None
    pr_number: Optional[int] = None
    review_retries: int = 0
    max_retries: int = 3

    def advance(self) -> bool:
        """Advance the task to the next state. Returns True if more work remains."""
        state_order = list(WorkflowState)
        current_idx = state_order.index(self.state)
        if current_idx < len(state_order) - 1:
            self.state = state_order[current_idx + 1]
            return True
        return False

    def needs_fix(self) -> bool:
        """Mark the task as needing a fix cycle."""
        if self.review_retries < self.max_retries:
            self.state = WorkflowState.FIX
            self.review_retries += 1
            return True
        return False


class WorkflowRunner:
    """Orchestrates the multi-agent GitOps workflow."""

    def __init__(self, repo_name: str):
        self.repo_name = repo_name
        self.tasks: list[Task] = []
        self.completed: list[Task] = []

    def add_task(self, title: str, description: str) -> Task:
        """Add a new task to the workflow."""
        task = Task(title=title, description=description)
        self.tasks.append(task)
        return task

    def run(self) -> None:
        """Execute the workflow for all tasks."""
        print(f"Starting Hermes GitOps workflow for {self.repo_name}")
        print("=" * 50)

        while self.tasks:
            task = self.tasks.pop(0)
            print(f"\nProcessing: {task.title}")
            print(f"  State: {task.state.value}")

            while task.advance():
                print(f"  -> {task.state.value}")

            self.completed.append(task)
            print(f"  ✅ Completed: {task.title}")

        print("\n" + "=" * 50)
        print(f"Workflow complete. {len(self.completed)} tasks processed.")


def main():
    """Main entry point for the workflow demo."""
    runner = WorkflowRunner("runminalex/my-repo")

    # Add a sample task
    task = runner.add_task(
        title="Implement test workflow",
        description="Create a basic workflow runner for the Hermes GitOps framework"
    )

    runner.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
