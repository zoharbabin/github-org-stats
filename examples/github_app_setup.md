# GitHub App Setup Guide

This guide walks you through setting up a GitHub App for use with the GitHub Organization Statistics Tool.

## Why Use GitHub Apps?

GitHub Apps provide several advantages over Personal Access Tokens:

- **Higher Rate Limits**: 5,000 requests per hour per installation
- **Fine-grained Permissions**: Only request the permissions you need
- **Organization-wide Access**: Can be installed across multiple organizations
- **Better Security**: Tokens are scoped to specific installations
- **Audit Trail**: Better tracking of API usage

## Step 1: Create a GitHub App

1. **Navigate to GitHub App Settings**
   - Go to your organization settings
   - Click on "Developer settings" in the left sidebar
   - Click on "GitHub Apps"
   - Click "New GitHub App"

2. **Configure Basic Information**
   - **GitHub App name**: `GitHub Org Stats Tool`
   - **Description**: `Tool for analyzing GitHub organization statistics`
   - **Homepage URL**: `https://github.com/your-org/github-org-stats`
   - **Webhook URL**: Leave blank (not needed for this tool)
   - **Webhook secret**: Leave blank

3. **Set Permissions**
   
   **Repository permissions:**
   - Contents: Read
   - Metadata: Read
   - Pull requests: Read
   - Issues: Read
   - Actions: Read
   
   **Organization permissions:**
   - Members: Read
   - Administration: Read (optional, for advanced features)

4. **Where can this GitHub App be installed?**
   - Select "Only on this account" for organization-specific use
   - Select "Any account" if you want to share the app

5. **Create the App**
   - Click "Create GitHub App"
   - Note down the **App ID** (you'll need this later)

## Step 2: Generate Private Key

1. **Generate Private Key**
   - In your newly created GitHub App settings
   - Scroll down to "Private keys"
   - Click "Generate a private key"
   - Download the `.pem` file and store it securely

2. **Store Private Key Securely**
   ```bash
   # Create a secure directory
   mkdir -p ~/.github-apps
   chmod 700 ~/.github-apps
   
   # Move the private key
   mv ~/Downloads/your-app-name.*.private-key.pem ~/.github-apps/
   chmod 600 ~/.github-apps/*.pem
   ```

## Step 3: Install the GitHub App

1. **Install in Your Organization**
   - Go to your GitHub App settings
   - Click "Install App" in the left sidebar
   - Select your organization
   - Choose repositories:
     - "All repositories" for complete analysis
     - "Selected repositories" for specific repos only
   - Click "Install"

2. **Note the Installation ID**
   - After installation, check the URL
   - It will look like: `https://github.com/settings/installations/12345678`
   - The number at the end (`12345678`) is your **Installation ID**

## Step 4: Configure Environment Variables

Set up environment variables for easy use:

```bash
# Add to your ~/.bashrc or ~/.zshrc
export GITHUB_APP_ID=123456
export GITHUB_PRIVATE_KEY_PATH=~/.github-apps/your-app.private-key.pem
export GITHUB_INSTALLATION_ID=12345678
```

## Step 5: Test Your Setup

Test the GitHub App authentication:

```bash
# Basic test
python github_org_stats.py \
  --org your-org \
  --app-id $GITHUB_APP_ID \
  --private-key $GITHUB_PRIVATE_KEY_PATH \
  --installation-id $GITHUB_INSTALLATION_ID \
  --max-repos 5

# Using environment variables
python github_org_stats.py \
  --org your-org \
  --installation-id $GITHUB_INSTALLATION_ID \
  --max-repos 5
```

## Multi-Organization Setup

For analyzing multiple organizations:

1. **Install App in Multiple Organizations**
   - Install your GitHub App in each target organization
   - Note each installation ID

2. **Use Multiple Installation IDs**
   ```bash
   python github_org_stats.py \
     --org primary-org \
     --app-id $GITHUB_APP_ID \
     --private-key $GITHUB_PRIVATE_KEY_PATH \
     --installation-id "org1:111111,org2:222222,org3:333333"
   ```

## Configuration File Setup

Create a configuration file for complex setups:

```json
{
  "authentication": {
    "app_id": 123456,
    "private_key_path": "/path/to/private-key.pem",
    "installation_mappings": {
      "primary-org": 111111,
      "secondary-org": 222222,
      "partner-org": 333333
    }
  },
  "analysis": {
    "days_back": 90,
    "max_repos": 500,
    "exclude_bots": true
  },
  "output": {
    "format": "excel",
    "output_dir": "./reports"
  }
}
```

Use with:
```bash
python github_org_stats.py --config config.json --org primary-org
```

## Security Best Practices

1. **Private Key Security**
   - Store private keys in secure locations
   - Use restrictive file permissions (600)
   - Never commit private keys to version control
   - Consider using secret management tools

2. **Minimal Permissions**
   - Only grant necessary permissions
   - Regularly review and audit permissions
   - Remove unused installations

3. **Access Control**
   - Limit who can manage the GitHub App
   - Use organization-level access controls
   - Monitor app usage through audit logs

## Troubleshooting

### Common Issues

1. **Authentication Failed**
   - Verify App ID is correct
   - Check private key file path and permissions
   - Ensure installation ID matches the organization

2. **Permission Denied**
   - Check GitHub App permissions
   - Verify app is installed in the target organization
   - Ensure user has access to the organization

3. **Rate Limit Issues**
   - GitHub Apps have higher limits than PATs
   - Check rate limit status in debug logs
   - Consider spreading requests across time

### Debug Commands

```bash
# Test JWT token generation
python -c "
from github_org_stats import GitHubAppTokenManager, load_private_key
token_manager = GitHubAppTokenManager(123456, load_private_key('key.pem'))
print('JWT Token generated successfully')
"

# Test installation token
python github_org_stats.py \
  --org your-org \
  --app-id 123456 \
  --private-key key.pem \
  --installation-id 12345678 \
  --log-level DEBUG \
  --max-repos 1
```

## Rate Limits

GitHub App rate limits:
- **5,000 requests per hour** per installation
- **15,000 requests per hour** for GitHub App (across all installations)
- **30 requests per minute** for search API

Compare to Personal Access Token:
- **5,000 requests per hour** per token
- **30 requests per minute** for search API

## Next Steps

1. **Test with Small Dataset**: Start with a few repositories
2. **Monitor Usage**: Check rate limits and performance
3. **Scale Up**: Gradually increase repository count
4. **Automate**: Set up scheduled runs for regular analysis
5. **Share Results**: Use the generated reports for insights

For more information, see the [GitHub Apps documentation](https://docs.github.com/en/developers/apps).