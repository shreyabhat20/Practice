import { useEffect, useState } from "react";
import { Card, CardContent, Typography, CircularProgress, Alert } from "@mui/material";
import TodoList from "./TodoList";

export default function UserCard({ user }) {
  const [todos, setTodos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`https://jsonplaceholder.typicode.com/todos?userId=${user.id}`)
      .then((res) => {
        if (!res.ok) throw new Error("Failed to fetch todos");
        return res.json();
      })
      .then((data) => setTodos(data))
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, [user.id]);

  return (
    <Card className="Card" variant="outlined" sx={{ maxWidth: 300, mx: "auto", backgroundColor: "#e3f2fd", borderRadius: 2, boxShadow: 3, "&:hover": { boxShadow: 6, transform: "scale(1.02)" },
    transition: "all 0.2s ease-in-out", }}>
      <CardContent sx={{ p: 1 }}>
        <Typography variant="h6">{user.name}</Typography>
        <Typography variant="body2" color="text.secondary">
          {user.email}
        </Typography>

        {loading && <CircularProgress size={40} />}
        {error && <Alert severity="error">{error}</Alert>}
        {!loading && !error && <TodoList todos={todos} />}
      </CardContent>
    </Card>
  );
}
