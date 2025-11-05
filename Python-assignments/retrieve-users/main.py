'''Use Jsonplaceholder APIs.  Please design GET API to retrieve 10 users which should contains the posts they made and the comments they posted and their next to dos'''

from fastapi import FastAPI
import requests
import time

app = FastAPI()
base_url = "https://jsonplaceholder.typicode.com"

@app.get("/users")
def users():
    start=time.time()
    users = requests.get(f"{base_url}/users", verify=False).json()[:10]
    all_posts = requests.get(f"{base_url}/posts", verify=False).json()
    all_comments = requests.get(f"{base_url}/comments", verify=False).json()
    all_todos = requests.get(f"{base_url}/todos", verify=False).json()

    users_data = []
    for user in users:
        user_id = user["id"]
        posts = [p for p in all_posts if p["userId"] == user_id]
        post_ids = [p["id"] for p in posts]
        comments = [c for c in all_comments if c["postId"] in post_ids]
        todos = [t for t in all_todos if t["userId"] == user_id and not t["completed"]]

        users_data.append({
            "user_id": user_id,
            "name": user["name"],
            "posts": posts,
            "comments": comments,
            "next_todos": todos
        })
    end=time.time()
    time_taken=round(end-start)
    print(f"Time taken to fetch and process users: {time_taken} seconds")

    return {"Time taken": time_taken,"user_count": len(users_data),"users": users_data}