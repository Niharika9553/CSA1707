# vacuum_world.py
# Two-room Vacuum Cleaner problem (rooms: A and B)

class VacuumEnvironment:
    def __init__(self, state_A='dirty', state_B='dirty', agent_loc='A'):
        # state 'clean' or 'dirty'
        self.state = {'A': state_A, 'B': state_B}
        self.agent_loc = agent_loc
        self.step = 0

    def percept(self):
        # returns (location, status)
        return (self.agent_loc, self.state[self.agent_loc])

    def execute(self, action):
        """Execute an action: 'Suck', 'Left', 'Right', 'NoOp'"""
        self.step += 1
        if action == 'Suck':
            self.state[self.agent_loc] = 'clean'
        elif action == 'Left':
            self.agent_loc = 'A'
        elif action == 'Right':
            self.agent_loc = 'B'
        elif action == 'NoOp':
            pass
        else:
            raise ValueError("Unknown action: " + action)

    def is_goal(self):
        return self.state['A'] == 'clean' and self.state['B'] == 'clean'

    def __str__(self):
        return f"Step {self.step:02d}: Loc={self.agent_loc} | A={self.state['A']} | B={self.state['B']}"

# Agents
class SimpleReflexAgent:
    def __init__(self):
        self.name = "SimpleReflexAgent"

    def program(self, percept):
        loc, status = percept
        if status == 'dirty':
            return 'Suck'
        else:
            # if in A go to B, if in B go to A
            return 'Right' if loc == 'A' else 'Left'

class ModelBasedAgent:
    def __init__(self):
        self.name = "ModelBasedAgent"
        # memory: known cleanliness of rooms (None = unknown)
        self.memory = {'A': None, 'B': None}

    def program(self, percept):
        loc, status = percept
        # update memory
        self.memory[loc] = status

        # If current room dirty -> suck
        if status == 'dirty':
            return 'Suck'

        # If both known and clean -> NoOp (done)
        if self.memory['A'] == 'clean' and self.memory['B'] == 'clean':
            return 'NoOp'

        # Otherwise move to the other room to inspect/clean
        return 'Right' if loc == 'A' else 'Left'

# Runner
def run(agent, env, max_steps=50, verbose=True):
    if verbose:
        print(f"\nRunning {agent.name} -- initial: {env}")
    for _ in range(max_steps):
        percept = env.percept()
        action = agent.program(percept)
        if verbose:
            print(f"Percept -> Loc:{percept[0]}, Status:{percept[1]}  => Action: {action}")
        env.execute(action)
        if verbose:
            print(env)
        if action == 'NoOp' or env.is_goal():
            if verbose:
                print("\nGoal reached or NoOp executed.")
            break
    else:
        if verbose:
            print("\nMax steps reached without reaching goal.")
    return env

# Example runs
if __name__ == "__main__":
    # Example 1: Simple Reflex Agent starting in A, A dirty, B dirty
    env1 = VacuumEnvironment(state_A='dirty', state_B='dirty', agent_loc='A')
    run(SimpleReflexAgent(), env1)

    # Example 2: Model-Based Agent starting in B, A dirty, B clean
    env2 = VacuumEnvironment(state_A='dirty', state_B='clean', agent_loc='B')
    run(ModelBasedAgent(), env2)
