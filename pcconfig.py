import pynecone as pc


config = pc.Config(
    app_name="home",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.PROD,
    api_url="ws://10.138.0.7:8080",
    port="80",
    backend_port="8080",
    deploy_url="https://dykim.dev"
)
