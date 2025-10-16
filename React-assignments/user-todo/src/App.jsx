import { useEffect, useState } from "react";
import { Container, Typography, CircularProgress, Alert } from "@mui/material";
import UserList from "./components/UserList";

export default function App() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((res) => {
        if (!res.ok) throw new Error("Failed to fetch users");
        return res.json();
      })
      .then((data) => setUsers(data))
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <CircularProgress />;
  if (error) return <Alert severity="error">{error}</Alert>;

  return (
    <Container sx={{ backgroundColor: "#c2d3e8ff", minHeight: "100vh", py: 3 }}>
  <Typography variant="h4" color="#0e1f56ff" gutterBottom>
    Users and To-Dos
  </Typography>
  <UserList users={users} />
</Container>

    // <div style={{ width: "100%", padding: 20 }}>
    //   <UserList users={users} />
    // </div>
  );
}
