from ple.games.flappybird import FlappyBird
from ple import PLE
import numpy as np
import time
from agentes.dq_agent import QAgent

# --- Configuración del Entorno y Agente ---
game = FlappyBird()
env = PLE(game, display_screen=True, fps=30)
env.init()
actions = env.getActionSet()  # Ej: [None, 119 (w), 115 (s)]

# Crear el agente
# Descomenta la línea de load_q_table_path si quieres cargar una tabla pre-entrenada
agent = QAgent(actions, game, epsilon=1.0, min_epsilon=0.05, epsilon_decay=0.995,
               learning_rate=0.2, discount_factor=0.95,
               load_q_table_path="flappy_birds_q_table.pkl")

# agent.load_q_table('./flappy_birds_q_table.pkl')

print("\n--- Ejecutando agente entrenado (modo explotación) ---")
agent.epsilon = 0
env.display_screen = True

for episode in range(5):
    env.reset_game()
    state_dict = env.getGameState()
    done = False
    total_reward_episode = 0
    print(f"Iniciando episodio de prueba {episode+1}")
    while not done:
        action = agent.act(state_dict)
        reward = env.act(action)
        state_dict = env.getGameState()
        done = env.game_over()
        total_reward_episode += reward
        time.sleep(0.03)
    print(f"Recompensa episodio de prueba {episode+1}: {total_reward_episode}")