import pynecone as pc


config = pc.Config(
    app_name="home",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.PROD,
    bun_path="$HOME/.bun/bin/bun",
    api_url="ws://35.212.232.153:8000",
    port="80"
)
