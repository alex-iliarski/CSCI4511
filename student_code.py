import sys

sys.path.append('aima-python')
from agents import *


class HW1:
    def __init__(self, agents=None, env=None):
        # Do not modify this, it is used for testing!
        if agents is None:
            (self.reflex_agent, self.model_agent, self.random_agent) = self.get_agents()
        else:
            (self.reflex_agent, self.model_agent, self.random_agent) = agents
            
        if env is None:
            self.environment = self.get_env()
        else:
            self.environment = env

    def get_agents(self):
        '''
        FILL IN AGENTS HERE
        Return all three agents like: return(reflex_agent, model_agent,
        random_agent)
        '''
        agent_1 = TraceAgent(ReflexVacuumAgent())  # reflex agent
        agent_2 = TraceAgent(ModelBasedVacuumAgent())  # model based agent
        agent_3 = TraceAgent(RandomVacuumAgent())  # random agent
        return (agent_1, agent_2, agent_3)

    def get_env(self):
        '''
        FILL IN ENVIRONMENT HERE
        Return the environment like: return environment
        '''
        env = TrivialVacuumEnvironment()  # trivial vac environment
        return env

    def run(self, agent, env, times):
        '''
        Run the environment for the given number of times and return the
        performance of the agent.
        Utilize the helper function to run the environment for the given number of
        times.
        Make sure the agent is added to the environment before running the
        environment.
        Return the status of the environment after the run.
        '''
        # step 1: get agent in the env
        env.add_thing(agent)
        # step 2: run the env for the given times
        env.run(times)
        # step 3: set to status variable
        # step 4: return the status of the env after the run
        # status = None
        return env.status

    def problem_1(self):
        '''
        Call your run function with the reflex agent and the trivial vac
        environment and return the result
        '''
        return self.run(self.reflex_agent, self.environment, 20)

    def problem_2(self):
        '''
        Call your run function with the model based agent and the trivial vac
        environment and return the result
        '''
        return self.run(self.model_agent, self.environment , 20)

    def problem_3(self):
        '''
        Call your run function with the random agent and the trivial vac
        environment and return the result
        '''
        return self.run(self.random_agent, self.environment, 20)

    def problem_4(self):
        '''
        Compare the performance of the reflex agent, the model based agent, and
        random agent in the trivial vac environment.
        You will have to pass the agents and the environment to the comparison
        function,
        this will require reviewing the documentation because the process is a
        little different.
        '''
        agents = [self.reflex_agent.__init__, self.model_agent.__init__, self.random_agent.__init__]
        
        env = TrivialVacuumEnvironment
        agents = [ReflexVacuumAgent, ModelBasedVacuumAgent, RandomVacuumAgent]
        results = compare_agents(env, agents)
        
        return results


def main():
    hw1 = HW1()
    print("Problem 1:", hw1.problem_1())
    print("Problem 2:", hw1.problem_2())
    print("Problem 3:", hw1.problem_3())
    print("Problem 4:", hw1.problem_4())


if __name__ == '__main__':
    main()
