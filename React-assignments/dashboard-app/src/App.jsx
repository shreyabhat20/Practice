import { useState, useEffect } from "react";
import { Box, Typography } from "@mui/material";
import DataChart from "./Datachart";

function App() {
  console.log("Dashboard rendered")
  const [time, setTime] = useState(new Date().toLocaleTimeString());
  const [chartData] = useState([10, 20, 30]);

  useEffect(() => {
    const timer = setInterval(() => {
      setTime(new Date().toLocaleTimeString());
    }, 1000);

    return () => clearInterval(timer);
  }, []);

//const stableData = useMemo(() => chartData, [chartData]);

//   return (
//     <Box sx={{ p: 2 }}>
//       <Typography variant="h5">Dashboard</Typography>
//       <Typography>Current Time: {time}</Typography>

//       {/* Child component */}
//       <DataChart data={stableData} />
//     </Box>
//   );
// }

  return (
    <Box sx={{ p: 2 }}>
      <Typography variant="h5">Dashboard</Typography>
      <Typography>Current Time: {time}</Typography>
      <DataChart data={chartData} />
    </Box>
  );
}

export default App;