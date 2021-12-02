from environs import Env

env = Env()
env.read_env()

API_KEY = env('API_KEY')
WORKSPACE_ID = env('WORKSPACE_ID')
SALARY_BASE = env('SALARY_BASE')
