"""
Validation script for the Rich Todo Console Application
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.main import TodoApp
from src.operations import TaskOperations


def validate_rich_todo():
    """
    Validate that the Rich Todo Console Application works as expected
    """
    print("Validating Rich Todo Console Application...")

    # Test 1: Verify basic functionality
    print("\n1. Testing basic functionality...")
    app = TodoApp()

    # Test operations directly
    ops = app.operations

    # Add a task
    task_id = ops.add_task("Test Task", "Test Description")
    assert task_id == 1, f"Expected ID 1, got {task_id}"
    print("   [PASS] Task creation with auto-incrementing ID works")

    # List tasks
    tasks = ops.list_tasks()
    assert len(tasks) == 1, f"Expected 1 task, got {len(tasks)}"
    assert tasks[0].title == "Test Task", f"Expected 'Test Task', got {tasks[0].title}"
    print("   [PASS] Task listing works")

    # Update task
    success = ops.update_task(task_id, title="Updated Task")
    assert success == True, "Update should succeed"
    updated_task = ops.get_task_by_id(task_id)
    assert updated_task.title == "Updated Task", f"Expected 'Updated Task', got {updated_task.title}"
    print("   [PASS] Task update works")

    # Toggle status
    success = ops.toggle_task_status(task_id)
    assert success == True, "Toggle should succeed"
    toggled_task = ops.get_task_by_id(task_id)
    assert toggled_task.completed == True, "Task should be completed after toggle"
    print("   [PASS] Task status toggle works")

    # Delete task
    success = ops.delete_task(task_id)
    assert success == True, "Delete should succeed"
    deleted_task = ops.get_task_by_id(task_id)
    assert deleted_task is None, "Task should not exist after deletion"
    print("   [PASS] Task deletion works")

    # Test 2: Verify data model
    print("\n2. Testing data model...")
    from src.models import Task

    task = Task(id=1, title="Test", description="Description")
    assert task.id == 1
    assert task.title == "Test"
    assert task.description == "Description"
    assert task.completed == False  # Default value
    print("   [PASS] Task data model works correctly")

    # Test 3: Verify in-memory storage
    print("\n3. Testing in-memory storage...")
    ops1 = TaskOperations()
    ops1.add_task("Task 1", "Description 1")
    ops1.add_task("Task 2", "Description 2")

    # Create a new operations instance (simulating a new session)
    ops2 = TaskOperations()
    assert len(ops2.list_tasks()) == 0, "New operations should have no tasks (in-memory only)"
    print("   [PASS] In-memory storage works correctly (no persistence)")

    # Test 4: Verify error handling
    print("\n4. Testing error handling...")
    # Try to update non-existent task
    success = ops.update_task(999, title="Non-existent")
    assert success == False, "Update should fail for non-existent task"

    # Try to delete non-existent task
    success = ops.delete_task(999)
    assert success == False, "Delete should fail for non-existent task"

    # Try to toggle non-existent task
    success = ops.toggle_task_status(999)
    assert success == False, "Toggle should fail for non-existent task"
    print("   [PASS] Error handling works correctly")

    print("\n[SUCCESS] All validation tests passed!")
    print("The Rich Todo Console Application is working as expected.")


if __name__ == "__main__":
    validate_rich_todo()