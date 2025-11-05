import { useState } from "react";
import { Box, TextField, Button, Typography, Paper } from "@mui/material";

export default function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isRegistered, setIsRegistered] = useState(false);
  const [error, setError] = useState("");

  const isUsernameValid = username.length >= 3;
  const isPasswordValid = password.length >= 8;
  const isFormValid = isUsernameValid && isPasswordValid;

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const res = await fetch("http://127.0.0.1:8000/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });

      if (!res.ok) {
        const errorData = await res.json();
        setError(errorData.detail || "Registration failed");
        return;
      }

      const data = await res.json();
      if (data.success) {
        setIsRegistered(true);
      }
    } catch (err) {
      setError("Server not reachable");
    }
  };

  if (isRegistered) {
    return (
      <Box textAlign="center" mt={10}>
        <Typography variant="h5" color="success.main">
          Registration Successful!
        </Typography>
      </Box>
    );
  }

  return (
    <Box display="flex" justifyContent="center" mt={10}>
      <Paper sx={{ p: 4, width: 350 }}>
        <Typography variant="h5" gutterBottom>
          Registration Form
        </Typography>

        <Box component="form" onSubmit={handleSubmit}>
          <TextField
            fullWidth
            label="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            error={username && !isUsernameValid}
            helperText={username && !isUsernameValid ? "At least 3 characters" : ""}
            sx={{ mb: 2 }}
          />

          <TextField
            fullWidth
            type="password"
            label="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            error={password && !isPasswordValid}
            helperText={password && !isPasswordValid ? "At least 8 characters" : ""}
            sx={{ mb: 2 }}
          />

          {error && (
            <Typography color="error" variant="body2" sx={{ mb: 2 }}>
              {error}
            </Typography>
          )}

          <Button type="submit" variant="contained" fullWidth disabled={!isFormValid}>
            Submit
          </Button>
        </Box>
      </Paper>
    </Box>
  );
}
