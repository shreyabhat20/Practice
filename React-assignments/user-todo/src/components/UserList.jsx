import { Grid } from "@mui/material";
import UserCard from "./UserCard";

export default function UserList({ users }) {
  return (
    <Grid container spacing={2} justifyContent="center" alignItems="stretch">
      {users.map((user) => (
        <Grid item xs={24} key={user.id}>
          <UserCard user={user} />
        </Grid>
      ))}
    </Grid>

    
  );
}
