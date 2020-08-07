#-1 =》 wall, 1 => goal, 0 => path
import numpy as np
board = np.zeros((12, 12))
board[:, 0] = -1
board[:, -1] = -1
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

class Maze:

    def __init__(self, board):
        self.canvas = board
        self.cur_loc = np.array([1, 1])

    def reset(self):
        self.cur_loc = np.array([1, 1])

    def get_value(self, loc):
        return self.canvas[loc[0], loc[1]]

    def get_possible_actions(self, loc):

        possible_actions = []

        if get_value(self.cur_loc - np.array([1, 0])) != -1:   # up
            possible_actions.append(0)
        if get_value(self.cur_loc + np.array([1, 0])) != -1:   # down
            possible_actions.append(1)
        if get_value(self.cur_loc + np.array([0, 1])) != -1:   # right
            possible_actions.append(2)
        if get_value(self.cur_loc - np.array([0, 1])) != -1:   # left
            possible_actions.append(3)

        return possible_actions

    def step(self, action):
        # move agent
        if action == 0:     # up
            self.cur_loc -= np.array([1, 0])
        elif action == 1:    # down
            self.cur_loc += np.array([1, 0])
        elif action == 2:    # right
            self.cur_loc += np.array([0, 1])
        elif action == 3:    # left
            self.cur_loc += np.array([0, 1])

        # reward
        board_value = self.get_value(self.cur_loc)
        if board_value == 1:
            reward = 1
            done = True
            s_ = 'terminal'
        elif board_value == -1:
            reward = -1
            done = False
            s_ = ','.join(self.cur_loc)

        else:
            reward = 0
            done = False
            s_ = ','.join(self.cur_loc)

        return s_, reward, done, self.get_possible_actions(self.cur_loc)

        def render(self):
            time.sleep(0.1)
            self.update()


def update():
    for t in range(10):
        s = env.reset()
        while True:
            env.render()
            a = 1
            s, r, done = env.step(a)
            if done:
                break

if __name__ == '__main__':
    env = Maze(board)
    env.after(100, update)
    env.mainloop()
