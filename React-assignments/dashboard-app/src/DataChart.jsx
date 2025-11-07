// import { useMemo } from "react";
import { Box, Typography } from "@mui/material";

// export default function DataChart({ data }) {
//   const processed = useMemo(() => {
//     return data.map((num) => num ** 2);
//   }, [data]);

export default function DataChart({ data }) {
  console.log("DataChart rendered")
  const processed = data.map((num) => num ** 2); 

  return (
    <Box sx={{ mt: 2, p: 2, border: "1px solid gray", borderRadius: 1 }}>
      <Typography variant="subtitle1">Data Chart</Typography>
      <Typography>Processed: {processed.join(", ")}</Typography>
    </Box>
  );
}