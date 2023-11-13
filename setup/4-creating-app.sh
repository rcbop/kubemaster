#!/usr/bin/env bash
kubectl config set-context --current --namespace=argocd
kubectl create namespace dev
kubectl create namespace qa
kubectl apply -f argocd/argocd-app-dev.yaml
kubectl apply -f argocd/argocd-app-qa.yaml