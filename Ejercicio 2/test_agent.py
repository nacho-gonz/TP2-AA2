from ple.games.flappybird import FlappyBird
from ple import PLE
import time
import argparse
import importlib
import sys
import numpy as np

# --- Configuración del Entorno y Agente ---
# Inicializar el juego
game = FlappyBird()  # Usar FlappyBird en vez de Pong
env = PLE(game, display_screen=True, fps=30) # fps=30 es más normal, display_screen=True para ver


# Inicializar el entorno
env.init()

# Obtener acciones posibles
actions = env.getActionSet()

# --- Argumentos ---
parser = argparse.ArgumentParser(description="Test de agentes para FlappyBird (PLE)")
parser.add_argument('--agent', type=str, required=True, help='Ruta completa del agente, ej: agentes.random_agent.RandomAgent')
args = parser.parse_args()


# --- Carga dinámica del agente usando path completo ---
if args.agent == 'agentes.nn_agent.NNAgent':
    from agentes.nn_agent import NNAgent
    class_name = 'NNAgent'
else:
    try:
        module_path, class_name = args.agent.rsplit('.', 1)
        agent_module = importlib.import_module(module_path)
        AgentClass = getattr(agent_module, class_name)
    except (ValueError, ModuleNotFoundError, AttributeError):
        print(f"No se pudo encontrar la clase {args.agent}")
        sys.exit(1)

# Inicializar el agente
if class_name == 'QAgent':
    agent = AgentClass(actions, game, epsilon=0)
elif class_name == 'NNAgent':
    agent = NNAgent(actions, game)
else:
    agent = AgentClass(actions, game)

recompensas_sesion = []
# Agente con acciones aleatorias
for i in range(100):
    env.reset_game()
    agent.reset()
    state_dict = env.getGameState()
    done = False
    total_reward_episode = 0
    print("\n--- Ejecutando agente ---")
    while not done:
        action = agent.act(state_dict)
        reward = env.act(action)
        state_dict = env.getGameState()
        done = env.game_over()
        total_reward_episode += reward
        time.sleep(0.03)
    recompensas_sesion.append(total_reward_episode)
    print(f"Recompensa episodio: {total_reward_episode}")

print(f'El promedio de recompensas de los 100 episodios es de: {np.mean(recompensas_sesion)}')