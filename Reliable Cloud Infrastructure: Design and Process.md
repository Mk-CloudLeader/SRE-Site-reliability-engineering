# Microservices vs. monolithic architecture & Best Practices 


**What is Micoservice & difference from Monolithic applications?**

Microservices divide a large program into multiple smaller, independent services
Architecturally, a monolith or microservices should be modular components with clearly defined boundaries. With a monolith, the deployment is the grouping of the
components, whereas with microservices, the individual components are deployable.

**Stateful services have different challenges than stateless ones**
- Avoid storing shared state in-memory on your servers  => sticky sessions on your LB
- Store state using backend storage services shared by the frontend server (EFS, Firestore, Cloud SQL etc..) 

## Microservice Best Practices
-The Twelve-Factor App is a set of best practices for building web or software-as-a-service applications. Twelve-factor design helps you to decouple components of the application, so that each component can be replaced easily or scaled up or down seamlessly
  01. Codebase :
    - One codebase tracked in revision control, many deploys
    - Use a version control system like Git or SVN.
    - Each app has one code repo and vice versa.
  02. Dependencies :
      - Dependencies should be declared explicitly and stored in version control
      - Dependency tracking is performed by language-specific tools such as Maven for Java and Pip for Python.
      - Container Registry can be used to store the images
  03. Config   : Store config in the environment 
      - Don't put secrets, connection strings, endpoints, etc., in source code.
      - store those in the env variables 

  04. Backing Services :Treat backing services as attached resources
     - Databases, caches, queues,and other services are accessed via URLs.
      For example, when the app writes data to storage, treating the storage as a backing service allows you to seamlessly change the underlying storage type, because it's decoupled from the app. 
  6. Build, release, run :Strictly separate build and run stages
    - **Build** creates a deployment package from the source code.
     - **Release** combines the deployment with configuration in the runtime environment.
     - **Run** executes the application
  8. Processes  : Execute the app as one or more stateless processes
  9. Port binding  :Export services via port binding
  10. Concurrency  :Scale out via the process model
  11. Disposability
      - App instances should scale quickly when needed.  If an instance is not needed, you should be able to turn it off with no side effects.
  13. Dev/prod parity :Keep development, staging, and production as similar as possible
  14. Logs
      - Write log messages to standard output and aggregate all logs to a single source
  16. Admin processes  :Run admin/management tasks as one-off processes
      - Admin processes are usually one-off processes and should be decoupled from the application

### Diagrams        

### Reference 
https://12factor.net
https://cloud.google.com/architecture/twelve-factor-app-development-on-gcp
https://tanzu.vmware.com/content/blog/beyond-the-twelve-factor-app
  
