"""Unit tests for the Hermes GitOps Workflow module."""

import pytest
from hermes_workflow import Task, WorkflowRunner, WorkflowState


class TestTask:
    """Tests for the Task dataclass."""

    def test_initial_state(self):
        task = Task(title="Test", description="A test task")
        assert task.state == WorkflowState.IDEA
        assert task.review_retries == 0

    def test_advance(self):
        task = Task(title="Test", description="A test task")
        assert task.advance() is True
        assert task.state == WorkflowState.PRD
        # Advance all the way through
        for _ in range(len(WorkflowState) - 2):  # -2 because we already advanced once
            task.advance()
        assert task.state == WorkflowState.DONE
        # Should not advance past DONE
        assert task.advance() is False

    def test_needs_fix_within_limits(self):
        task = Task(title="Test", description="A test task")
        task.state = WorkflowState.REVIEW
        result = task.needs_fix()
        assert result is True
        assert task.state == WorkflowState.FIX
        assert task.review_retries == 1

    def test_needs_fix_exceeds_max(self):
        task = Task(title="Test", description="A test task", max_retries=2)
        task.state = WorkflowState.REVIEW
        task.needs_fix()  # retry 1
        task.needs_fix()  # retry 2
        result = task.needs_fix()  # should fail
        assert result is False
        assert task.review_retries == 2


class TestWorkflowRunner:
    """Tests for the WorkflowRunner class."""

    def test_add_task(self):
        runner = WorkflowRunner("test/repo")
        task = runner.add_task("Test", "A test")
        assert task in runner.tasks

    def test_run_completes_tasks(self):
        runner = WorkflowRunner("test/repo")
        runner.add_task("Task 1", "First task")
        runner.add_task("Task 2", "Second task")
        runner.run()
        assert len(runner.tasks) == 0
        assert len(runner.completed) == 2

    def test_empty_run(self):
        runner = WorkflowRunner("test/repo")
        runner.run()  # Should not raise
        assert len(runner.completed) == 0
