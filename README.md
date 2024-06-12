<p align="center">
  <picture>
    <img alt="vLLM" src="https://github.com/vincent-haoy/DRPC/assets/53930677/87060f07-abeb-4454-b0e2-87ef2fcd056d" width=55%>
  </picture>
</p>

<h3 align="center">
  <p style="text-align: center;">A <ins>D</ins>istributed <ins>R</ins>esources  <ins>P</ins>rovisioning framework in Container-based <ins>C</ins>lusters</p>
</h3>

<p align="center">
|Parallel|Asynchronous|Efficient|
</p>

---


# About

We have developed a distributed reinforcement learning framework, DRPC, for resource provisioning in container-based autoscaling. This framework precisely models system resources and allocates them dynamically to meet the demands of microservices. Our method combines reinforcement learning with a distributed algorithm that uses domain knowledge through deep imitation learning, enabling efficient and adaptive decision-making for scaling strategies across microservice clusters. 

Additionally, we utilize multiple lightweight neural networks on distributed nodes to handle operations from a central node, reducing its load and speeding up resource allocation. This approach also enhances the accuracy of predicting cloud system behavior. Furthermore, we implemented a Gym-like API to translate Q-values into resource adjustments.

---

# Getting started 

Follow these steps to set up your Kubernetes system with our application:

0. **Install dependencies**: Ensure all the dependencies specified in our paper are installed properly.

1. **Check CgroupV2 Support**: Ensure your Kubernetes system supports CgroupV2. If not, you'll need to use a compatible alternative.

2. **Secure API Configuration**: For security reasons, we have removed all API endpoints and links from this setup. Replace these with the specific details from your own cluster.

3. **Communication and Deployment Configuration**:
   - Write your own communication scripts.
   - Embed the deployment configurations for Docker.
   - Ensure GPU access is enabled, as detailed in the associated paper.

4. **Cluster Configuration**:
   - Modify the cluster array in `setup.py` to include all your cluster nodes.
   - Enable SSH access on all nodes.

5. **Run the Cluster Setup**: Execute the cluster setup process according to the configurations.

---

## Simulating with Jupyter notebook

We also provide a Jupyter notebook file that simulates the provisioning behavior on a single node, achieving up to 90% of the full system's performance.

- **Instructions**: Follow all the setup instructions mentioned above, except for the Docker configuration. 

Run the notebook to simulate this framework on a single node.
