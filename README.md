# Patient Dashboard OpenShift Deployment

Build and deploy locally using Podman and OpenShift internal registry.

## Prerequisites

- OpenShift access
- oc CLI installed
- podman installed

## Build locally

```bash
cd /path/to/this/project
podman build -t patient-dashboard:latest .
```

## Login to OpenShift internal registry

```bash
oc login ...
oc whoami -t

podman login --tls-verify=false -u kubeadmin -p $(oc whoami -t) \
  default-route-openshift-image-registry.apps.<your-cluster-domain>
```

## Tag and push image

```bash
podman tag patient-dashboard:latest \
  default-route-openshift-image-registry.apps.<your-cluster-domain>/myproject/patient-dashboard:latest

podman push --tls-verify=false \
  default-route-openshift-image-registry.apps.<your-cluster-domain>/myproject/patient-dashboard:latest
```

## Deploy to OpenShift

```bash
oc apply -f patient-dashboard-deploy.yaml
oc rollout status deployment/patient-dashboard
oc get route patient-dashboard
```

## Access app

The app will be available at the route URL.
