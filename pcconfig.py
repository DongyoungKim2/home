import pynecone as pc


config = pc.Config(
    app_name="home",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.PROD,
    api_url="ws://dykim.dev:8000",
    port="80",
)
