def schedule_tasks(task_hierarchy):
    # Base case: If task_hierarchy is empty, return an empty list
    if not task_hierarchy:
        return []


    task_hierarchy.sort(key=lambda task: task.get('priority', 0), reverse=True)

    scheduled_tasks = []

    for task in task_hierarchy:
        # Recursively schedule subtasks first
        if 'subtasks' in task and task['subtasks']:
            subtasks = schedule_tasks(task['subtasks'])
            scheduled_tasks.extend(subtasks)
        
        # Schedule the current task
        scheduled_tasks.append(task)

    return scheduled_tasks

tasks = [
    {'id': 1, 'name': 'Task 1', 'priority': 2, 'subtasks': [
        {'id': 2, 'name': 'Subtask 1.1', 'priority': 1, 'subtasks': []}
    ]},
    {'id': 3, 'name': 'Task 2', 'priority': 1, 'subtasks': [
        {'id': 4, 'name': 'Subtask 2.1', 'priority': 3, 'subtasks': []},
        {'id': 5, 'name': 'Subtask 2.2', 'priority': 2, 'subtasks': []}
    ]}
]

scheduled_tasks = schedule_tasks(tasks)
for task in scheduled_tasks:
    print(f"Task ID: {task['id']}, Name: {task['name']}")


#Space Complexity: The space complexity is (O(n)) due to the recursion stack, where (n) is the depth of the hierarchy.