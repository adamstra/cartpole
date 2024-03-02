import gym
import numpy as np

# Importe le jeu CartPole
env = gym.make('CartPole-v1')

# Fonction qui renvoie l'action à effectuer
def policy(state):
    # Choisis une action aléatoire
    action = np.random.randint(2)
    return action

# Boucle de jeu
for _ in range(1000):
    # Récupère l'état actuel du jeu
    state = env.reset()

    # Tant que le jeu n'est pas terminé
    while True:
        # Applique l'action choisie
        action = policy(state)
        env.step(action)

        # Récupère l'état suivant et la récompense
        state_prime, reward, done, info, _ = env.step(action)

        # Si le jeu est terminé, quitte la boucle
        if done:
            break

        # Met à jour l'état
        state = state_prime

# Affiche le score final
print(env.step(state))
env.close()
