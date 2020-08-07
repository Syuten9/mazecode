import numpy as np
from maze_env import Maze
from RL_brain import QLearningTable


def run(n_episode=100):
    for episode in range(n_episode):

        print('Episode {}'.format(episode+1))

        # initial observation
        observation = env.reset()
        possible_actions = env.get_possible_actions()

        step = 0
        while True:
            # RL choose action based on observation
            action = RL.choose_action(str(observation), possible_actions)

            # RL take action and get next observation and reward
            observation_, reward, done, possible_actions = env.step(action)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_ if isinstance(observation_, str) else observation_.copy()

            step += 1

            # break while loop when end of this episode
            if done:
                break

        print('Episode {} ends in {} steps.'.format(episode+1, step))

    # end of game
    print('game over')


if __name__ == "__main__":
    board = np.zeros((12, 12))
    board[:, 0] = -1
    board[0, :] = -1
    board[-1, :] = -1
    board[3, 1] = -1
    board[6, 1: 4] = -1
    board[8, 2: 6] = -1
    board[9, 5] = -1
    board[10, 3] = -1
    board[0: 3, 3] = -1
    board[2: 3, 5] = -1
    board[3: 7, 6] = -1
    board[3, 7] = -1
    board[2: 3, 8] = -1
    board[6: 10, 8] = -1
    board[2, 9] = -1
    board[-2, -2] = 1

    env = Maze(board)
    RL = QLearningTable(actions=list(range(4)))

    run(n_episode=100)