# How to Run

Follow these steps to set up your Kubernetes system with our application:

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

### Simulating with Jupyter Notebook

We also provide a Jupyter notebook file that simulates the provisioning behavior on a single node, achieving up to 90% of the full system's performance.

- **Instructions**: Follow all the setup instructions mentioned above, except for the Docker configuration. 

Run the notebook to simulate the environment on a single node.
