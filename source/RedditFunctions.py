import asyncpraw
import os
import asyncio

reddit = asyncpraw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_APP_TOKEN"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent=f"telegram interface by u/{os.getenv("REDDIT_USERNAME")}",
    username=os.getenv("REDDIT_USERNAME"),
)


async def main():
    print(await reddit.user.me())


if __name__=="__main__":
    asyncio.run(main())