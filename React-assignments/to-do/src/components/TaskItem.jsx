import { ListItem, Checkbox, IconButton, Typography } from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";

export default function TaskItem({ task, onToggle, onDelete }) {
  return (
    <ListItem
      secondaryAction={
        <IconButton edge="end" onClick={() => onDelete(task.id)}>
          <DeleteIcon />
        </IconButton>
      }
    >
      <Checkbox checked={task.done} onChange={() => onToggle(task.id)} />   {/* When the checkbox is clicked, it calls onToggle with this task’s ID */}
      <Typography
        sx={{ textDecoration: task.done ? "line-through" : "none" }}
      >
        {task.text}
      </Typography>
    </ListItem>
  );
}
