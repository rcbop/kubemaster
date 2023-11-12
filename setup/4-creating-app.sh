#!/usr/bin/env bash
kubectl config set-context --current --namespace=argocd
kubectl apply -f argocd/argocd-app.yaml