from fastapi import FastAPI

app = FastAPI(title="DeployTrack")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "DeployTrack is running"}


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "healthy"}
