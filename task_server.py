from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("Task Server")

tasks = []
task_id_counter = 1


@mcp.tool()
def add_task(title: str, description: str) -> dict:
    """Add a new task with a title and description."""
    print("TOOL CALLED: add_task")
    print("TITLE:", title)
    print("DESCRIPTION:", description)
    global task_id_counter
    task = {
        "id": task_id_counter,
        "title": title,
        "description": description,
        "status": "pending",
        "createdat": datetime.now().isoformat()
    }
    tasks.append(task)
    task_id_counter += 1
    return task


@mcp.tool()
def complete_task(taskid: int) -> dict:
    """Mark a task as completed by its ID."""
    print("TOOL CALLED: complete_task")
    print("TASK ID:", taskid)
    for task in tasks:
        if task["id"] == taskid:
            task["status"] = "completed"
            task["completedat"] = datetime.now().isoformat()
            return task
    return {"error": f"No task found with id {taskid}"}


@mcp.tool()
def delete_task(taskid: int) -> dict:
    """Delete a task by its ID."""
    print("TOOL CALLED: delete_task")
    print("TASK ID:", taskid)
    global tasks
    for i, task in enumerate(tasks):
        if task["id"] == taskid:
            removed = tasks.pop(i)
            return {"deleted": True, "task": removed}
    return {"error": f"No task found with id {taskid}"}


@mcp.tool()
def list_tasks(status: str = "all") -> dict:
    """List tasks filtered by status: 'all', 'pending', or 'completed'."""
    print("TOOL CALLED: list_tasks")
    print("STATUS FILTER:", status)
    if status == "all":
        return {"tasks": tasks, "count": len(tasks)}
    filtered = [t for t in tasks if t["status"] == status]
    return {"tasks": filtered, "count": len(filtered)}


@mcp.resource("tasks://all")
def get_all_tasks() -> str:
    """Get all tasks as formatted text."""
    if not tasks:
        return "No tasks found."

    result = "Current Tasks:\n\n"
    for task in tasks:
        status_emoji = "✅" if task["status"] == "completed" else "⏳"
        result += f"{status_emoji} [{task['id']}] {task['title']}\n"
        if task["description"]:
            result += f"   Description: {task['description']}\n"
        result += f"   Status: {task['status']}\n"
        result += f"   Created: {task['createdat']}\n"
        if "completedat" in task:
            result += f"   Completed: {task['completedat']}\n"
        result += "\n"

    return result


@mcp.resource("tasks://pending")
def get_pending_tasks() -> str:
    """Get only pending tasks."""
    pending = [t for t in tasks if t["status"] == "pending"]

    if not pending:
        return "No pending tasks!"

    result = f"Pending Tasks ({len(pending)}):\n\n"
    for task in pending:
        result += f"⏳ [{task['id']}] {task['title']}\n"
        if task["description"]:
            result += f"   {task['description']}\n"
        result += "\n"

    return result


@mcp.resource("tasks://completed")
def get_completed_tasks() -> str:
    """Get only completed tasks."""
    completed = [t for t in tasks if t["status"] == "completed"]

    if not completed:
        return "No completed tasks yet!"

    result = f"Completed Tasks ({len(completed)}):\n\n"
    for task in completed:
        result += f"✅ [{task['id']}] {task['title']}\n"
        if task["description"]:
            result += f"   {task['description']}\n"
        if "completedat" in task:
            result += f"   Completed: {task['completedat']}\n"
        result += "\n"

    return result


if __name__ == "__main__":
    mcp.run()