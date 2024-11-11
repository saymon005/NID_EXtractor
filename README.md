Technical Documentation: NID Image to Text Extraction Service for Global office automation limited
Client: Global office automation limited
Service Provider: Smart Technologies (BD) Limited
Project Team: Goal hunter [Kazi Riad Uddin, Saymon Islam Iftikar, Mashbul Haidar Ovi, Jubaida Jahan Jubary]

Problem Scenario: Grameenphone, a leading telecommunications service provider in Bangladesh, is seeking to enhance its user registration process for the "GP Apps" platform by automating the extracting of information from the users' National Identity Documents (NIDs). The goal is to streamline the data collection process and store essential user data securely. To achieve this, Grameenphone has approached Smart Technologies (BD) Limited to develop an Image-to-text extraction service. 
Objectives:
•  Purpose: To automate the extraction of information from users' National Identity Documents (NIDs) for the "GP Apps" platform, enhancing the user registration process.
•  Scope: This document covers the technical specifications, architecture, and implementation details for the Image to Text extraction service.
Introduction: Grameenphone, a leading telecommunications service provider in Bangladesh, has identified the need to optimize its registration process to provide a seamless user experience. By leveraging advanced technologies such as FastAPI, Docker, and Google Cloud Run, this project aims to deliver a robust and scalable solution. The following sections detail the problem scenario, objectives, solution architecture, and cost estimation, providing a comprehensive overview of the project.
Solution: To address the problem scenario and achieve the outlined objectives, the following solution has been designed, encompassing both backend and frontend workflows to ensure a seamless and efficient NID image-to-text extraction service.

Backend Workflow:
Gemini API is connected through FastAPI and fine-tuned:
The Gemini API is connected to through FastAPI, and fine-tuning is carried out to meet the specific requirements of the application.
A Docker container is created:
The backend, once ready, is containerized using Docker. All dependencies are included to ensure consistency across different environments.
The Docker image is pushed to the Artifact Registry:
After the container is created, the Docker image is pushed to the artifact registry, a cloud-based repository where it is stored for deployment.
The container is deployed to Cloud Run:
The Docker image is then deployed to Google Cloud Run, where it is managed and automatically scaled based on the incoming requests.
Communication is handled through the API:
The backend, now running on Cloud Run, communicates with the frontend by using exposed API endpoints.

![Project](https://github.com/user-attachments/assets/942d5853-8054-47fe-b8ef-25a59ecb1793)

Frontend Workflow:
The frontend is developed using Django:
The frontend application is built using Django, which is a web framework known for building robust web applications.
The frontend code is pushed to a GitHub repository:
Once the frontend is ready, it is pushed to a GitHub repository for version control and storage.
The VM environment is prepared:
A virtual machine environment is prepared, and the code from the GitHub repository is pulled into the VM to host the server.
A firewall rule is created to allow the port:
A firewall rule is created to enable access through a specific port, allowing external requests to reach the web server.
Requests and responses are handled by the client:
Requests are sent by the client to the frontend server, which communicates with the backend API, and the responses are returned to the client.

Solution validity:
Microservices: The backend (FastAPI) and frontend (Django) are separate, making it easier to update, scale, and maintain each part independently without affecting the other.
Containerization: Using Docker ensures the application runs consistently across environments and uses fewer resources compared to traditional methods.
Cloud Run: The backend is deployed to Google Cloud Run, which automatically scales based on demand and only charges when the app is used, saving costs.
VM for Frontend: As the requirements for hosting the front end are known thus it was easy to configure a lightweight VM. The frontend is hosted on a VM, giving full control over configurations, security, and persistent availability. It allows flexibility in hosting and managing traffic securely with firewall rules.
Modularity: Keeping services independent ensures that issues in one service don’t crash the whole system. Each part can be updated or scaled as needed.
This solution maximizes resource utilization, simplifies maintenance, and ensures consistent performance across environments, making the system highly efficient.
