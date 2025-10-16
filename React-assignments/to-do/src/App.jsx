import { useState } from "react"; //React Hook that lets component store data that can change over time
import { Container, Typography, Paper } from "@mui/material"; //MUI for layout and styling
import TaskInput from "./components/TaskInput";
import TaskList from "./components/TaskList"; //custom components
import "./App.css";


export default function App() { // function component
  const [tasks, setTasks] = useState([]);
  //tasks → Variable that stores all the tasks.
  //setTasks → Function used to update the tasks.
  // useState([]) → Starts with an empty array.

  const addTask = (text) => {
    const newTask = { id: Date.now(), text, done: false };
    setTasks([...tasks, newTask]); //spread syntax, Adds this new task to the existing tasks array
  };

  const toggleTask = (id) => {
    setTasks(tasks.map((t) => (t.id === id ? { ...t, done: !t.done } : t))); //if id matches, flip done value
  };

  const deleteTask = (id) => {
    setTasks(tasks.filter((t) => t.id !== id)); //filter creates a new array excluding the deleted task
  };

  return (
<Container maxWidth="sm">
  <Paper sx={{ p: 3 }}>
    <Typography variant="h4" mb={2} align="center">
      Task Manager
    </Typography>
    <Typography variant="subtitle1" color="text.secondary" align="center">
      Completed: {tasks.filter(t => t.done).length} / {tasks.length}
    </Typography>

    <TaskInput onAdd={addTask} />
    <TaskList tasks={tasks} onToggle={toggleTask} onDelete={deleteTask} />
  </Paper>
</Container>
  );
}