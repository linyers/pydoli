from .main import *

Database = Database(JSON_PATH)
Pydoli = Todo(Database)

add = Pydoli.add
remove = Pydoli.remove
edit = Pydoli.edit
done = Pydoli.done
list_tasks = Pydoli.list
pydoli_help = Pydoli.help
version = Pydoli.version