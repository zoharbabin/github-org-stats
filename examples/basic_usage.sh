#!/bin/bash
# GitHub Organization Statistics Tool - Basic Usage Examples

echo "GitHub Organization Statistics Tool - Usage Examples"
echo "===================================================="

# Basic usage with personal access token
echo "1. Basic analysis with personal access token:"
echo "python github_org_stats.py --org your-org --token ghp_your_token_here"
echo ""

# GitHub App authentication
echo "2. GitHub App authentication:"
echo "python github_org_stats.py \\"
echo "  --org your-org \\"
echo "  --app-id 12345 \\"
echo "  --private-key /path/to/private-key.pem \\"
echo "  --installation-id 67890"
echo ""

# Advanced filtering
echo "3. Advanced filtering options:"
echo "python github_org_stats.py \\"
echo "  --org your-org \\"
echo "  --token ghp_token \\"
echo "  --include-forks \\"
echo "  --include-archived \\"
echo "  --exclude-bots \\"
echo "  --max-repos 50"
echo ""

# Multiple output formats
echo "4. Generate all output formats:"
echo "python github_org_stats.py \\"
echo "  --org your-org \\"
echo "  --token ghp_token \\"
echo "  --format all \\"
echo "  --output-dir ./reports"
echo ""

# Custom time range and logging
echo "5. Custom time range with debug logging:"
echo "python github_org_stats.py \\"
echo "  --org your-org \\"
echo "  --token ghp_token \\"
echo "  --days-back 90 \\"
echo "  --log-level DEBUG \\"
echo "  --log-file analysis.log"
echo ""

# Using configuration file
echo "6. Using configuration file:"
echo "python github_org_stats.py \\"
echo "  --config config/example_config.json \\"
echo "  --org your-org"
echo ""

# Multi-organization with GitHub App
echo "7. Multi-organization analysis:"
echo "python github_org_stats.py \\"
echo "  --org your-org \\"
echo "  --app-id 12345 \\"
echo "  --private-key key.pem \\"
echo "  --installation-id \"org1:111,org2:222,org3:333\""
echo ""

# Specific repositories only
echo "8. Analyze specific repositories:"
echo "python github_org_stats.py \\"
echo "  --org your-org \\"
echo "  --token ghp_token \\"
echo "  --repos repo1 repo2 repo3"
echo ""

echo "For more detailed usage information, see docs/USAGE.md"