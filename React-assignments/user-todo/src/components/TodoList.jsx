import { List, ListItem, ListItemText, Checkbox } from "@mui/material";

export default function TodoList({ todos }) {
  return (
    <List dense>
      {todos.map((todo) => (
        <ListItem key={todo.id}>
          <Checkbox checked={todo.completed} disabled />
          <ListItemText primary={todo.title} />
        </ListItem>
      ))}
    </List>
  );
}
