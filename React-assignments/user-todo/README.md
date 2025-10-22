A simple React application that fetches **users** and their corresponding **to-dos** from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com).  
Built using **React**, **Material UI (MUI)**, and the **Fetch API**.

---

## Features

- Fetches users from:  
  [`https://jsonplaceholder.typicode.com/users`](https://jsonplaceholder.typicode.com/users)
- Fetches each user’s to-dos from:  
  [`https://jsonplaceholder.typicode.com/todos?userId=<id>`](https://jsonplaceholder.typicode.com/todos?userId=1)
- Displays loading spinners while data is being loaded  
- Shows error messages if something goes wrong  
- Responsive two-column card layout using **MUI Grid**  
- Clean, modern UI built with **MUI Cards** and **Typography**

---

## React Concepts Used

- **useEffect** – for fetching data on component mount  
- **useState** – for managing user and todo data  
- **Conditional Rendering** – for loading/error/empty states  
- **Props** – for passing user and todo information between components  
- **JSX** – to structure UI with MUI components


## Containerized using **Docker** and served with Nginx and pushed to Docker Hub
- https://hub.docker.com/r/shreyabhat20/user-todo-app
