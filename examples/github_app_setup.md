# GitHub App Setup Guide

This comprehensive guide walks you through setting up a GitHub App for use with the GitHub Organization Statistics Tool, including the new multi-organization analysis capabilities introduced in v1.1.0.

## 🚀 What's New in v1.1.0

The GitHub Organization Statistics Tool v1.1.0 introduces **revolutionary multi-organization analysis capabilities**, allowing users to analyze multiple GitHub organizations in a single command execution with unified output and organization attribution.

### Key New Features
- **🆕 Multi-Organization Analysis**: `--org-ids "org1:install_id1,org2:install_id2"`
- **🔄 Unified Output**: All repository data combined into single files
- **📊 Enhanced Excel Reports**: Additional "Organization_Breakdown" sheet
- **🔐 Smart Authentication**: Automatic GitHub App token management
- **⚡ Efficient Processing**: Intelligent API limit distribution

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

## 🆕 Multi-Organization Setup (v1.1.0+)

For analyzing multiple organizations in a single command:

1. **Install App in Multiple Organizations**
   - Install your GitHub App in each target organization
   - Note each installation ID

2. **🚀 NEW: Single Command Multi-Organization Analysis**
   ```bash
   # Analyze multiple organizations in one run
   python github_org_stats.py \
     --org-ids "org1:111111,org2:222222,org3:333333" \
     --app-id $GITHUB_APP_ID \
     --private-key $GITHUB_PRIVATE_KEY_PATH \
     --include-forks \
     --include-archived \
     --exclude-bots \
     --max-repos 6000 \
     --days-back 365 \
     --format all \
     --output-dir ./multi_org_reports
   
   # Using environment variables (recommended)
   export GITHUB_APP_ID=123456
   export GITHUB_PRIVATE_KEY_PATH=~/.github-apps/your-app.private-key.pem
   
   github-org-stats \
     --org-ids "kaltura:68242466,kaltura-ps:68357040" \
     --include-forks \
     --include-archived \
     --exclude-bots \
     --max-repos 6000 \
     --days-back 365 \
     --format all \
     --output-dir ./multi_org_reports
   ```

3. **Legacy: Single Organization Mode**
   ```bash
   # Still supported for single organization analysis
   python github_org_stats.py \
     --org primary-org \
     --app-id $GITHUB_APP_ID \
     --private-key $GITHUB_PRIVATE_KEY_PATH \
     --installation-id 111111
   ```

## Configuration File Setup

Create a configuration file for complex setups:

### Multi-Organization Configuration (v1.1.0+)
```json
{
  "authentication": {
    "app_id": 123456,
    "private_key_path": "/path/to/private-key.pem"
  },
  "organizations": {
    "kaltura": 68242466,
    "kaltura-ps": 68357040,
    "partner-org": 333333
  },
  "analysis": {
    "days_back": 365,
    "max_repos": 6000,
    "include_forks": true,
    "include_archived": true,
    "exclude_bots": true,
    "include_empty": true
  },
  "output": {
    "format": "all",
    "output_dir": "./multi_org_reports"
  }
}
```

### Legacy Single Organization Configuration
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

### Usage
```bash
# Multi-organization with config (manual org-ids specification still required)
python github_org_stats.py --config config.json --org-ids "kaltura:68242466,kaltura-ps:68357040"

# Single organization with config
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

## 🎯 Multi-Organization Analysis Benefits

### For Users
- **Time Savings**: Analyze multiple organizations in one command
- **Unified Reports**: Single output files with all data
- **Better Insights**: Cross-organization analysis and comparison
- **Simplified Workflow**: No need for multiple command executions

### For Organizations
- **Enterprise Ready**: Scalable multi-organization analysis
- **Comprehensive Reporting**: Organization breakdown and summaries
- **Efficient Resource Usage**: Optimized API usage across organizations
- **Enhanced Security**: Better GitHub App integration

## 📊 Multi-Organization Output Files

### Generated Files
- `github_org_stats_org1_org2_YYYYMMDD_HHMMSS.xlsx`
- `github_org_stats_org1_org2_YYYYMMDD_HHMMSS.json`
- `github_org_stats_org1_org2_YYYYMMDD_HHMMSS.csv`

### Excel Sheets (Multi-Organization Mode)
1. **Repository_Data**: All repositories with organization attribution
2. **Summary**: Combined statistics across all organizations
3. **Organization_Breakdown**: Per-organization metrics and comparisons
4. **Contributors**: Top contributors across all organizations
5. **Languages**: Language distribution across all organizations
6. **Errors**: Error tracking and debugging information

## 🔄 Migration from Single to Multi-Organization

### Before (Multiple Commands)
```bash
python github_org_stats.py --org org1 --installation-id 111
python github_org_stats.py --org org2 --installation-id 222
python github_org_stats.py --org org3 --installation-id 333
```

### After (Single Command)
```bash
python github_org_stats.py --org-ids "org1:111,org2:222,org3:333"
```

### Backward Compatibility
- All existing single-organization commands continue to work
- No breaking changes to existing functionality
- Legacy `--org` parameter fully supported

## 📈 Performance and Resource Management

### Intelligent Resource Distribution
- Max repositories limit distributed across organizations
- Smart API rate limit management across installations
- Efficient token management and caching
- Graceful error handling per organization

### Enhanced Error Handling
- Per-organization error tracking and reporting
- Graceful failure handling (continues with other orgs if one fails)
- Detailed error logging and debugging information
- Organization-specific error categorization

## 🔮 Future Multi-Organization Enhancements

### Planned Features
- Configuration-driven organization lists
- Advanced cross-organization analytics and comparisons
- Organization comparison reports and dashboards
- Automated multi-organization scheduling and reporting

### Improvements Under Consideration
- Parallel organization processing for faster analysis
- Enhanced caching mechanisms for multi-organization runs
- Advanced filtering and search across organizations
- Custom report templates for multi-organization analysis

## Next Steps

1. **Start with Multi-Organization**: Use the new `--org-ids` parameter for comprehensive analysis
2. **Test with Small Dataset**: Begin with a few repositories per organization
3. **Monitor Usage**: Check rate limits and performance across organizations
4. **Scale Up**: Gradually increase repository count and add more organizations
5. **Leverage Reports**: Use organization breakdown sheets for insights
6. **Automate**: Set up scheduled runs for regular multi-organization analysis
7. **Share Results**: Distribute unified reports across teams and stakeholders

For more information, see the [GitHub Apps documentation](https://docs.github.com/en/developers/apps) and the [project README](../README.md) for comprehensive usage examples.