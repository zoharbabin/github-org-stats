# GitHub Organization Statistics - Unified Script

A comprehensive tool for analyzing GitHub organization statistics including repository metrics, contributor activity, code quality insights, and multi-organization support with GitHub Apps.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Authentication](#authentication)
- [Usage](#usage)
- [Configuration](#configuration)
- [Output Formats](#output-formats)
- [Advanced Features](#advanced-features)
- [Troubleshooting](#troubleshooting)
- [Migration Guide](#migration-guide)
- [Contributing](#contributing)

## Overview

The GitHub Organization Statistics Unified Script combines the functionality of three original scripts into a single, powerful tool that provides comprehensive analysis of GitHub organizations. It supports both Personal Access Token and GitHub App authentication, making it suitable for both individual use and enterprise deployments.

### Key Capabilities

- **Repository Analysis**: Comprehensive metrics including stars, forks, issues, languages, and activity
- **Contributor Insights**: Detailed contributor analysis with bot filtering capabilities
- **Code Quality Metrics**: Language statistics, dependency analysis, and security insights
- **Multi-Organization Support**: GitHub App authentication for analyzing multiple organizations
- **Flexible Output**: JSON, CSV, and Excel formats with rich formatting
- **Advanced Filtering**: Include/exclude forks, archived repos, empty repos, and bot accounts
- **Rate Limit Management**: Intelligent rate limiting and retry mechanisms
- **Error Handling**: Robust error handling with detailed logging and recovery

## Features

### Merged from Original Scripts

This unified script combines features from three original scripts:

1. **Basic Organization Stats** (`github_org_stats.py`)
   - Repository enumeration and basic metrics
   - Star, fork, and issue counts
   - Language detection and statistics

2. **Enhanced Repository Analysis** (`github_org_stats_improved.py`)
   - Advanced contributor analysis
   - Commit statistics and activity tracking
   - Branch and tag information
   - Release tracking

3. **Multi-Organization Support** (`github_multi_org_stats.py`)
   - GitHub App authentication
   - Multiple installation ID support
   - Enterprise-grade error handling
   - Advanced Excel output with formatting

### New Unified Features

- **Bot Detection and Filtering**: Automatically detect and optionally exclude bot accounts
- **Empty Repository Handling**: Option to include or exclude repositories with no recent activity
- **Enhanced Error Tracking**: Comprehensive error categorization and reporting
- **Adaptive Processing**: Dynamic batch sizing based on repository count
- **Rich Excel Output**: Professional formatting with summary sheets and data validation
- **Comprehensive Logging**: Detailed logging with configurable levels and file output

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Required Dependencies

Install all required dependencies using pip:

```bash
pip install requests pandas PyGithub PyJWT tqdm openpyxl pytz
```

Or install from a requirements file:

```bash
pip install -r requirements.txt
```

### Requirements File Content

Create a `requirements.txt` file with:

```
requests>=2.25.0
pandas>=1.3.0
PyGithub>=1.55.0
PyJWT>=2.0.0
tqdm>=4.60.0
openpyxl>=3.0.0
pytz>=2021.1
```

## Authentication

The script supports two authentication methods:

### 1. Personal Access Token (PAT)

For individual use or small-scale analysis:

```bash
python github_org_stats_unified.py --org myorg --token ghp_your_token_here
```

**Required Token Permissions:**
- `repo` (for private repositories)
- `read:org` (for organization data)
- `read:user` (for user information)

### 2. GitHub App Authentication

For enterprise use and multi-organization analysis:

```bash
python github_org_stats_unified.py \
  --org myorg \
  --app-id 12345 \
  --private-key /path/to/private-key.pem \
  --installation-id 67890
```

**GitHub App Setup:**
1. Create a GitHub App in your organization settings
2. Generate and download a private key
3. Install the app in target organizations
4. Note the App ID and Installation ID(s)

**Required App Permissions:**
- Repository permissions: `metadata`, `contents` (read)
- Organization permissions: `members` (read)

## Usage

### Basic Usage

Analyze a single organization with default settings:

```bash
python github_org_stats_unified.py --org myorg --token ghp_your_token
```

### Advanced Usage Examples

#### Multi-Organization Analysis

```bash
# Single installation ID for multiple orgs
python github_org_stats_unified.py \
  --org myorg \
  --app-id 12345 \
  --private-key key.pem \
  --installation-id 67890

# Multiple installation IDs
python github_org_stats_unified.py \
  --org myorg \
  --app-id 12345 \
  --private-key key.pem \
  --installation-id "org1:111,org2:222,org3:333"
```

#### Filtering Options

```bash
# Include forks and archived repositories
python github_org_stats_unified.py \
  --org myorg \
  --token ghp_token \
  --include-forks \
  --include-archived

# Exclude bot accounts and empty repositories
python github_org_stats_unified.py \
  --org myorg \
  --token ghp_token \
  --exclude-bots \
  --max-repos 50

# Analyze specific repositories only
python github_org_stats_unified.py \
  --org myorg \
  --token ghp_token \
  --repos repo1 repo2 repo3
```

#### Output Customization

```bash
# Generate all output formats
python github_org_stats_unified.py \
  --org myorg \
  --token ghp_token \
  --format all \
  --output-dir ./reports

# Custom time range and logging
python github_org_stats_unified.py \
  --org myorg \
  --token ghp_token \
  --days-back 90 \
  --log-level DEBUG \
  --log-file analysis.log
```

### Command Line Arguments

#### Authentication
- `--token`: GitHub personal access token
- `--app-id`: GitHub App ID for authentication
- `--private-key`: Path to GitHub App private key file
- `--installation-id`: GitHub App installation ID(s)

#### Scope
- `--org`: GitHub organization name to analyze (required)
- `--repos`: Specific repositories to analyze (space-separated)
- `--days-back`: Number of days to look back for activity (default: 30)

#### Output
- `--output-dir`: Output directory for reports (default: output)
- `--format`: Output format - json, csv, excel, or all (default: excel)
- `--config`: Configuration file path (JSON format)

#### Analysis Options
- `--include-forks`: Include forked repositories
- `--include-archived`: Include archived repositories
- `--include-empty`: Include repositories with no recent commits
- `--exclude-bots`: Exclude bot accounts from analysis
- `--max-repos`: Maximum number of repositories to analyze (default: 100)

#### Logging
- `--log-level`: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `--log-file`: Log file path (default: console only)

## Configuration

### Configuration File

Use a JSON configuration file for complex setups:

```json
{
  "authentication": {
    "app_id": 12345,
    "private_key_path": "/path/to/private-key.pem",
    "installation_mappings": {
      "org1": 111,
      "org2": 222,
      "org3": 333
    }
  },
  "analysis": {
    "days_back": 60,
    "max_repos": 200,
    "include_forks": false,
    "include_archived": false,
    "exclude_bots": true,
    "include_empty": false
  },
  "output": {
    "format": "all",
    "output_dir": "./reports",
    "timezone": "America/New_York"
  },
  "logging": {
    "level": "INFO",
    "file": "github_analysis.log"
  }
}
```

Use the configuration file:

```bash
python github_org_stats_unified.py --config config.json --org myorg
```

### Environment Variables

Set GitHub App credentials via environment variables:

```bash
export GITHUB_APP_ID=12345
export GITHUB_PRIVATE_KEY_PATH=/path/to/private-key.pem

python github_org_stats_unified.py --org myorg --installation-id 67890
```

## Output Formats

### Excel Output (Default)

The Excel output includes multiple sheets:

1. **Repository_Data**: Complete repository information
2. **Summary**: High-level organization statistics
3. **Contributors**: Top contributors across all repositories
4. **Languages**: Language distribution analysis
5. **Errors**: Any errors encountered during analysis

**Excel Features:**
- Professional formatting with colors and borders
- Data validation and filtering
- Frozen headers for easy navigation
- Conditional formatting for key metrics

### JSON Output

Structured JSON with complete data hierarchy:

```json
{
  "organization": "myorg",
  "analyzed_at": "2024-01-15T10:30:00Z",
  "total_repositories": 25,
  "repositories": [
    {
      "name": "repo1",
      "full_name": "myorg/repo1",
      "description": "Repository description",
      "private": false,
      "stargazers_count": 42,
      "contributors": [...],
      "languages": {...},
      "commit_stats": {...}
    }
  ]
}
```

### CSV Output

Flattened data suitable for spreadsheet analysis and data processing tools.

## Advanced Features

### Bot Detection

The script automatically detects bot accounts using pattern matching:

- Accounts ending in `bot` or `[bot]`
- Known service accounts (dependabot, renovate, github-actions, etc.)
- Configurable exclusion with `--exclude-bots`

### Rate Limit Management

Intelligent rate limiting features:

- Automatic rate limit detection and waiting
- Configurable rate limit buffer
- Retry logic with exponential backoff
- Real-time rate limit status reporting

### Error Handling and Recovery

Comprehensive error handling:

- Categorized error tracking
- Graceful degradation for inaccessible repositories
- Detailed error reporting in output
- Continuation after non-fatal errors

### Multi-Installation Support

For GitHub Apps with multiple installations:

```bash
# Format: "org1:installation_id1,org2:installation_id2"
--installation-id "acme-corp:12345,subsidiary:67890"
```

### Memory Optimization

Adaptive processing for large organizations:

- Dynamic batch sizing based on repository count
- Memory-efficient data processing
- Configurable limits to prevent resource exhaustion

## Troubleshooting

### Common Issues

#### Authentication Errors

**Problem**: `Authentication verification failed`
**Solution**: 
- Verify token has required permissions
- Check GitHub App installation status
- Ensure private key file is accessible and valid

#### Rate Limit Issues

**Problem**: `Rate limit exceeded`
**Solution**:
- Use GitHub App authentication (higher limits)
- Reduce `--max-repos` value
- Run analysis during off-peak hours

#### Memory Issues

**Problem**: Script runs out of memory with large organizations
**Solution**:
- Reduce `--max-repos` value
- Use `--exclude-bots` to reduce data volume
- Process repositories in smaller batches

#### Permission Errors

**Problem**: `Access forbidden` for certain repositories
**Solution**:
- Verify GitHub App has required permissions
- Check if repositories are private and token has access
- Review organization member permissions

### Debug Mode

Enable detailed logging for troubleshooting:

```bash
python github_org_stats_unified.py \
  --org myorg \
  --token ghp_token \
  --log-level DEBUG \
  --log-file debug.log
```

### Validation Commands

Test authentication without full analysis:

```bash
# Test GitHub App authentication
python -c "
from github_org_stats_unified import GitHubAppTokenManager, load_private_key
token_manager = GitHubAppTokenManager(12345, load_private_key('key.pem'))
print('JWT Token:', token_manager.get_jwt_token()[:50] + '...')
"
```

## Migration Guide

### From Original Scripts

See [`MIGRATION_GUIDE.md`](MIGRATION_GUIDE.md) for detailed migration instructions from the three original scripts.

### Breaking Changes

1. **Command Line Arguments**: Some argument names have changed for consistency
2. **Output Format**: Excel output structure has been enhanced
3. **Authentication**: GitHub App authentication flow has been streamlined
4. **Error Handling**: More granular error categorization

### Backward Compatibility

The script maintains backward compatibility for:
- Basic command line arguments
- JSON output format structure
- Core functionality and metrics

## Performance Considerations

### Optimization Tips

1. **Use GitHub App Authentication**: Higher rate limits and better performance
2. **Filter Repositories**: Use `--max-repos` and filtering options
3. **Exclude Bots**: Reduces processing time and data volume
4. **Batch Processing**: Script automatically optimizes batch sizes
5. **Parallel Processing**: Consider running multiple instances for different organizations

### Expected Performance

- **Small Organizations** (< 50 repos): 2-5 minutes
- **Medium Organizations** (50-200 repos): 5-15 minutes  
- **Large Organizations** (200+ repos): 15+ minutes

Performance varies based on:
- Repository activity levels
- Network connectivity
- GitHub API response times
- Enabled analysis features

## Contributing

### Development Setup

1. Clone the repository
2. Install development dependencies: `pip install -r requirements-dev.txt`
3. Run tests: `python -m pytest tests/`
4. Follow PEP 8 style guidelines

### Reporting Issues

When reporting issues, please include:
- Command line arguments used
- Error messages and stack traces
- Log output (with `--log-level DEBUG`)
- Organization size and characteristics
- Python and dependency versions

### Feature Requests

Feature requests are welcome! Please include:
- Use case description
- Expected behavior
- Potential implementation approach
- Impact on existing functionality

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Check the troubleshooting section above
- Review existing GitHub issues
- Create a new issue with detailed information
- Consult the migration guide for upgrade questions

---

**Version**: 1.0.0  
**Last Updated**: 2024-01-15  
**Compatibility**: Python 3.7+, GitHub API v3/v4