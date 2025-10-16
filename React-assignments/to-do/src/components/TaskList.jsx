import { List, Typography } from "@mui/material";
import TaskItem from "./TaskItem";

export default function TaskList({ tasks, onToggle, onDelete }) {
  if (tasks.length === 0)
    return <Typography variant="body1">No tasks yet!</Typography>;

  return (
    <List>
      {tasks.map((t) => (
        <TaskItem key={t.id} task={t} onToggle={onToggle} onDelete={onDelete} /> 
      ))}  {/*loops through the tasks array and returns a TaskItem for each task */}
    </List>
  );
}
