from fastapi import FastAPI

app = FastAPI(title="DeployTrack")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "DeployTrack is running"}
