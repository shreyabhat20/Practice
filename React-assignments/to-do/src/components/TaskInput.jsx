import { useState } from "react"; // React Hook that lets the component store and update data
import { TextField, Button, Box } from "@mui/material"; // MUI components for input, button, and layout

export default function TaskInput({ onAdd }) { // function component with prop 'onAdd' received from App
  const [task, setTask] = useState(""); 

  const handleAdd = () => { 
    //function runs when user clicks Add button
    if (task.trim() === "") return; //prevents adding empty tasks
    onAdd(task); //calls the parent (App) function to add the task
    setTask(""); //clears the input field after adding
  };

  return (
    <Box display="flex" gap={2} mb={2}> 
      {/* Box is a layout wrapper from MUI (like <div>) with flexbox layout */}
      
      <TextField
        label="Enter task" // text label above the input box
        variant="outlined" // outlined style for input box
        fullWidth // makes the input stretch across available width
        value={task} // connects the input box to the 'task' state
        onChange={(e) => setTask(e.target.value)} // updates 'task' whenever user types
      />

      <Button 
        variant="contained" // filled color button
        onClick={handleAdd} // when clicked, calls handleAdd function
      >
        Add
      </Button>
    </Box>
  );
}
