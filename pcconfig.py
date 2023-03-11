import pynecone as pc


config = pc.Config(
    app_name="home",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.PROD,
    api_url="ws://35.212.187.170:8000",
    port="80",
    backend_port="8000",
    deploy_url="https://dykim.dev"
)
