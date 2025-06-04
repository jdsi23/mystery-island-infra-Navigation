#!/bin/bash

# Exit on any error
set -e

echo "[+] Downloading Terraform 1.7.5..."
curl -O https://releases.hashicorp.com/terraform/1.7.5/terraform_1.7.5_linux_amd64.zip

echo "[+] Unzipping Terraform..."
unzip -o terraform_1.7.5_linux_amd64.zip

echo "[+] Moving Terraform binary to /usr/local/bin..."
sudo mv terraform /usr/local/bin/

echo "[+] Making setup.sh and deploy.sh executable..."
chmod +x setup.sh
chmod +x deploy.sh

echo "[+] Running setup.sh..."
./setup.sh

echo "[+] Running deploy.sh twice..."
./deploy.sh
./deploy.sh

echo "[+] Fetching Load Balancer DNS names..."
aws elbv2 describe-load-balancers \
  --query 'LoadBalancers[*].DNSName' \
  --output text

echo "[✓] All steps completed successfully."
