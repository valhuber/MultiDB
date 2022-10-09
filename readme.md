# Experiment with Multiple Databases, using Bind

Create the `venv`, and use `API Logic Server` launch config.  

# Recent Changes
Revised 10/9:
* App rebuilt for API Logic Server 6.2 - this is a substantial cleanup of the `api_logic_server_run.py` code
* Thomas' fixes merged in


# Status

1. The API Starts
2. Admin App runs (eg, Categories)
3. Swagger runs, and can GET (eg, Categories)
4. Swagger shows `ToDos` (from db #2)
5. `ToDos` fails with __No Such Table__

```
{
  "errors": [
    {
      "title": "Generic Error: (sqlite3.OperationalError) no such table: todos\n[SQL: SELECT todos.task AS todos_task, todos.category AS todos_category, todos.date_added AS todos_date_added, todos.date_completed AS todos_date_completed, todos.status AS todos_status, todos.position AS todos_position, todos.id AS todos_id \nFROM todos ORDER BY todos.id\n LIMIT ? OFFSET ?]\n[parameters: (10, 0)]\n(Background on this error at: https://sqlalche.me/e/14/e3q8)",
      "detail": "Generic Error: (sqlite3.OperationalError) no such table: todos\n[SQL: SELECT todos.task AS todos_task, todos.category AS todos_category, todos.date_added AS todos_date_added, todos.date_completed AS todos_date_completed, todos.status AS todos_status, todos.position AS todos_position, todos.id AS todos_id \nFROM todos ORDER BY todos.id\n LIMIT ? OFFSET ?]\n[parameters: (10, 0)]\n(Background on this error at: https://sqlalche.me/e/14/e3q8)",
      "code": 500
    }
  ]
}
```

# Bacgrkound Info

Key code is in `api_logic_server_run.py`, as noted in /images.

Search for `multi_db`.