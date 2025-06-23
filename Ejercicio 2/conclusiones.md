# Ej 2 - TP2 - Q-Learning

        #     "player_y": self.player.pos_y,
        #     "player_vel": self.player.vel,
            
        #     "next_pipe_dist_to_player": next_pipe.x - self.player.pos_x,
        #     "next_pipe_top_y": next_pipe.gap_start,
        #     "next_pipe_bottom_y": next_pipe.gap_start+self.pipe_gap, 
            
        #     "next_next_pipe_dist_to_player": next_next_pipe.x - self.player.pos_x,
        #     "next_next_pipe_top_y": next_next_pipe.gap_start,
        #     "next_next_pipe_bottom_y": next_next_pipe.gap_start+self.pipe_gap 
        # 

## Discretización de los estados

- Estado crudo del juego:
    - "player_y": Posición Y del centro del jugador
    - "player_vel": Velocidad Y actual del jugador
    - "next_pipe_dist_to_player": Distancia a la siguiente tubería siguiente
    - "next_pipe_top_y": Posición Y del borde superior de la tubería siguiente
    - "next_pipe_bottom_y": Posición Y del borde inferior de la tubería siguiente
    - "next_next_pipe_dist_to_player": Distancia a la tubería siguiente a la tubería siguiente
    - "next_next_pipe_top_y": Posición Y del borde superior de la tubería siguiente a la tubería siguiente
    - "next_next_pipe_bottom_y": Posición Y del borde inferior de la tubería siguiente a la tubería siguiente

- ¿Estoy por debajo o por encima del hueco de las tuberias?
    - Idea: ¿Está el pajaro en el espacio del hueco de las tuberías, por encima o por debajo?

    - Simplificación: En lugar de tener la posición del pajaro en Y, la posición en Y de la parte superior de la tuberia y la posición en Y de la parte inferior de la tuberia, obtengo las posiciones relativas en base a mi pajaro, es decir, la resta entre las posiciones en Y de la parte superior e inferior de la tuberia y mi posición, lo que me da dos variables, con valores positivos o negativos dependiendo de si estoy por encima o por debajo de las tuberias.

    - Importancia: Me dice si necesito saltar o dejarme caer

- 