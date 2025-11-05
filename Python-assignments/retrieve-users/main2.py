from fastapi import FastAPI
import aiohttp
import asyncio
import time

app = FastAPI()
base_url = "https://jsonplaceholder.typicode.com"

@app.get("/users")
async def get_users():
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        users_task = session.get(f"{base_url}/users", ssl=False)
        posts_task = session.get(f"{base_url}/posts", ssl=False)
        comments_task = session.get(f"{base_url}/comments", ssl=False)
        todos_task = session.get(f"{base_url}/todos", ssl=False)

        responses = await asyncio.gather(users_task, posts_task, comments_task, todos_task)

        users = (await responses[0].json())[:10]
        all_posts = await responses[1].json()
        all_comments = await responses[2].json()
        all_todos = await responses[3].json()

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

    time_taken= round(time.time() - start_time, 3)
    print(f"Time taken to fetch and process users: {time_taken} seconds")

    return {
        "time_taken_seconds": time_taken,
        "user_count": len(users_data),
        "users": users_data
    }
