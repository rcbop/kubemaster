# CICD Practice Repository

This repository serves as an exercise to practice Continuous Integration and Continuous Deployment (CICD) pipelines using tools like GitHub Actions and ArgoCD. It includes a sample nginx application, ArgoCD custom resource definitions, and workflows for automating version bumps and environment promotions.

## Repository Structure

The directory structure is organized as follows:

- `app`: Contains a sample nginx server.
- `argocd`: Contains the ArgoCD application custom resource definitions.
- `k8s`: Includes the kustomization base and overlays for the DEV and QA environments.
- `bump_version.py`: A script to bump a given semantic version (e.g., `./bump_version.py PATCH 1.1.0` prints `1.1.1`).

## Workflows

### 1. `cicd.yaml`

This workflow automates the following steps:

#### a. Detect Changes

- It checks for changes in the `app` directory.

#### b. Version Bump

- If changes are detected, it triggers a job to check the commit message.
- If the commit message contains the keywords `MAJOR`, `MINOR`, or `PATCH`, it runs `./bump_version.py` with the respective parameters.
- The script then builds the Docker image, publishes to the container registry and updates the kustomization overlay in DEV, allowing ArgoCD to pick up the changes.

### 2. `promote.yaml`

This workflow automates the promotion of the nginx deployment version from DEV to QA:

- It retrieves the version of the nginx deployment in `k8s/dev/nginx`.
- It replicates this version to create a pull request in `k8s/qa/nginx`.

## How bumping semantic versions works

1. Just add the respective keyword to the commit message and push changes:

```bash
git add .
git commit -m "Bump version [PATCH]"
git push origin main
```

4. Observe the workflow in the "Actions" tab on GitHub.

5. To promote changes to QA, merge the pull request created by the `promote.yaml` workflow.
