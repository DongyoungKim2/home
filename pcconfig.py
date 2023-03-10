import pynecone as pc


config = pc.Config(
    app_name="home",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.PROD,
    api_url="0.0.0.0:8000",
    port="80",
)
