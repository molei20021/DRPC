import torch as T
import numpy as np

# 导入系统模块
sys.path.append('/home/robbie/code/DRPC/DRPC-main/Central_components')
from env import SystemEnv

# 定义一些可能缺失的类和函数
class Deployment_decision_maker:
    def __init__(self, memory, param):
        self.memory = memory
        self.param = param
    
    def make_decision(self, test):
        # 模拟决策，返回默认值
        return T.tensor([0.5, 0.5, 0.5])
    
    def train(self, epochs):
        # 模拟训练，不执行实际操作
        pass

def scale_action(action, low=-1, high=1):
    action = np.clip(action, -1, 1)
    weight = (high - low) / 2
    bias = (high + low) / 2
    action_ = action * weight + bias
    return action_

class Agent:
    def choose_action(self, observation, train=False):
        # 模拟动作选择，返回默认值
        return np.zeros(3)

class DeploymentBuffer:
    def __init__(self):
        self.memory = [None] * 32
    
    def remember(self, action, env, request, predicted_req):
        # 模拟存储，不执行实际操作
        pass

def decision_maker_make_Decision(env, request, predicted_req, deployment_decision_makers):
    deployment_states = list(env.deployment_states.values())
    allocated_states = list(env.pod_status.current_status.values())
    all_results = T.tensor((), dtype=T.float)
    all_results = all_results.new_zeros((len(deployment_states), 3))
    for i, deployment_state in enumerate(deployment_states):
        if i < len(deployment_decision_makers):
            # deployment states
            test = T.tensor([deployment_state[0], deployment_state[1], allocated_states[i][0], request, predicted_req])
            test = T.unsqueeze(test, 0).to(T.float)
            all_results[i] = deployment_decision_makers[i].make_decision(test)
    return all_results.flatten().tolist()

# 主函数，用于演示和测试
def main():
    # 初始化环境和组件
    env = SystemEnv()
    agent = Agent()
    deploymentbuffer = DeploymentBuffer()
    
    # Initial data retrieved
    observation, _ = env.reset()
    print(observation)
    deploymentbuff_sta_reward = []
    deploymentbuff_sta_usage = []
    SAVECHECKPOINT = 10
    
    # 模拟一些步骤
    for episode in range(0, 10):
        action = agent.choose_action(observation, train=False)
        deploymentbuffer.remember(action, env, observation[0], observation[1])
        action_ = scale_action(action)
        observation_, reward, done, truncated, info = env.step(action_)
        observation = observation_
        deploymentbuff_sta_reward.append(reward)
        deploymentbuff_sta_usage.append(np.array([observation[2], observation[3]]))
        
        if episode % SAVECHECKPOINT == 0:
            recent_usage = deploymentbuff_sta_usage[-SAVECHECKPOINT:] if len(deploymentbuff_sta_usage) >= SAVECHECKPOINT else deploymentbuff_sta_usage
            recent_rewards = deploymentbuff_sta_reward[-SAVECHECKPOINT:] if len(deploymentbuff_sta_reward) >= SAVECHECKPOINT else deploymentbuff_sta_reward
            
            if recent_usage:
                average_observation = np.mean(np.array(recent_usage), axis=0)
                average_reward = np.mean(recent_rewards)
                print('Ep: {} AvgReward: {}, observation: {}'.format(episode // SAVECHECKPOINT, average_reward, average_observation))

    # 这里仅作演示，实际使用时需要提供真实的deploymentbuffer.memory
    # deployment_decision_makers = [Deployment_decision_maker(deploymentbuffer.memory[i], 100) for i in range(32)]
    # for deployment_decision_maker in deployment_decision_makers:
    #     deployment_decision_maker.train(101)

if __name__ == "__main__":
    main()