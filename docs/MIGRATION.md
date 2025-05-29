# Migration Guide - GitHub Organization Statistics Unified Script

This guide helps you migrate from the three original GitHub organization statistics scripts to the new unified script.

## Table of Contents

- [Overview](#overview)
- [Migration from Basic Script](#migration-from-basic-script)
- [Migration from Improved Script](#migration-from-improved-script)
- [Migration from Multi-Org Script](#migration-from-multi-org-script)
- [Command Line Argument Changes](#command-line-argument-changes)
- [New Features and Usage](#new-features-and-usage)
- [Breaking Changes](#breaking-changes)
- [Configuration Migration](#configuration-migration)
- [Output Format Changes](#output-format-changes)
- [Performance Improvements](#performance-improvements)
- [Troubleshooting Migration Issues](#troubleshooting-migration-issues)

## Overview

The unified script combines functionality from three original scripts:

1. **`github_org_stats.py`** - Basic organization statistics
2. **`github_org_stats_improved.py`** - Enhanced repository analysis
3. **`github_multi_org_stats.py`** - Multi-organization support with GitHub Apps

### Benefits of Migration

- **Single Script**: One tool instead of three separate scripts
- **Enhanced Features**: Combined functionality with new capabilities
- **Better Error Handling**: Robust error recovery and reporting
- **Improved Performance**: Optimized data collection and processing
- **Advanced Authentication**: Support for both PAT and GitHub App authentication
- **Rich Output**: Professional Excel formatting with multiple sheets
- **Bot Filtering**: Automatic detection and filtering of bot accounts
- **Comprehensive Logging**: Detailed logging with configurable levels

## Migration from Basic Script

### Original Script: `github_org_stats.py`

**Old Command:**
```bash
python github_org_stats.py --org myorg --token ghp_token
```

**New Command:**
```bash
python github_org_stats_unified.py --org myorg --token ghp_token
```

### Key Changes

| Feature | Old Script | Unified Script | Notes |
|---------|------------|----------------|-------|
| Basic repo stats | ✅ | ✅ | Same functionality |
| Output format | JSON only | JSON, CSV, Excel | More options |
| Error handling | Basic | Advanced | Robust retry logic |
| Rate limiting | Manual | Automatic | Built-in management |
| Logging | Print statements | Structured logging | Configurable levels |

### Migration Steps

1. **Replace script name**: Change `github_org_stats.py` to `github_org_stats_unified.py`
2. **Update dependencies**: Install additional packages if needed
3. **Review output**: Excel format is now default (was JSON)
4. **Check new features**: Consider using bot filtering and enhanced logging

### Example Migration

**Before:**
```bash
python github_org_stats.py \
  --org acme-corp \
  --token ghp_your_token_here
```

**After:**
```bash
python github_org_stats_unified.py \
  --org acme-corp \
  --token ghp_your_token_here \
  --format excel \
  --exclude-bots \
  --log-level INFO
```

## Migration from Improved Script

### Original Script: `github_org_stats_improved.py`

**Old Command:**
```bash
python github_org_stats_improved.py --org myorg --token ghp_token --days 60
```

**New Command:**
```bash
python github_org_stats_unified.py --org myorg --token ghp_token --days-back 60
```

### Key Changes

| Feature | Old Script | Unified Script | Notes |
|---------|------------|----------------|-------|
| Enhanced analytics | ✅ | ✅ | Same functionality |
| Contributor analysis | ✅ | ✅ + Bot filtering | Enhanced |
| Commit statistics | ✅ | ✅ | Same functionality |
| Branch/tag info | ✅ | ✅ | Same functionality |
| Release tracking | ✅ | ✅ | Same functionality |
| Dependency analysis | ✅ | ✅ | Same functionality |

### Argument Changes

| Old Argument | New Argument | Notes |
|--------------|--------------|-------|
| `--days` | `--days-back` | Renamed for clarity |
| `--output` | `--output-dir` | More descriptive |
| `--verbose` | `--log-level DEBUG` | More granular control |

### Migration Steps

1. **Update argument names**: Change `--days` to `--days-back`
2. **Update output specification**: Use `--output-dir` instead of `--output`
3. **Review logging**: Replace `--verbose` with `--log-level`
4. **Consider new features**: Bot filtering, empty repo handling

### Example Migration

**Before:**
```bash
python github_org_stats_improved.py \
  --org acme-corp \
  --token ghp_token \
  --days 90 \
  --output ./reports \
  --verbose
```

**After:**
```bash
python github_org_stats_unified.py \
  --org acme-corp \
  --token ghp_token \
  --days-back 90 \
  --output-dir ./reports \
  --log-level DEBUG \
  --exclude-bots \
  --format all
```

## Migration from Multi-Org Script

### Original Script: `github_multi_org_stats.py`

**Old Command:**
```bash
python github_multi_org_stats.py \
  --org myorg \
  --app-id 12345 \
  --private-key key.pem \
  --installation-ids "org1:111,org2:222"
```

**New Command:**
```bash
python github_org_stats_unified.py \
  --org myorg \
  --app-id 12345 \
  --private-key key.pem \
  --installation-id "org1:111,org2:222"
```

### Key Changes

| Feature | Old Script | Unified Script | Notes |
|---------|------------|----------------|-------|
| GitHub App auth | ✅ | ✅ | Same functionality |
| Multi-installation | ✅ | ✅ | Same functionality |
| Excel output | ✅ | ✅ Enhanced | Better formatting |
| Error tracking | ✅ | ✅ Enhanced | More categories |
| Rate limiting | ✅ | ✅ Enhanced | Better management |

### Argument Changes

| Old Argument | New Argument | Notes |
|--------------|--------------|-------|
| `--installation-ids` | `--installation-id` | Simplified name |
| `--excel-output` | `--format excel` | Consistent with other formats |

### Migration Steps

1. **Update argument names**: Change `--installation-ids` to `--installation-id`
2. **Update output format**: Use `--format excel` instead of `--excel-output`
3. **Review new features**: Enhanced error tracking, bot filtering
4. **Check configuration**: Consider using config files for complex setups

### Example Migration

**Before:**
```bash
python github_multi_org_stats.py \
  --org acme-corp \
  --app-id 12345 \
  --private-key /path/to/key.pem \
  --installation-ids "acme:111,subsidiary:222" \
  --excel-output \
  --max-repos 500
```

**After:**
```bash
python github_org_stats_unified.py \
  --org acme-corp \
  --app-id 12345 \
  --private-key /path/to/key.pem \
  --installation-id "acme:111,subsidiary:222" \
  --format excel \
  --max-repos 500 \
  --exclude-bots \
  --log-level INFO
```

## Command Line Argument Changes

### Complete Argument Mapping

| Category | Old Arguments | New Arguments | Status |
|----------|---------------|---------------|---------|
| **Authentication** | | | |
| | `--token` | `--token` | ✅ Same |
| | `--app-id` | `--app-id` | ✅ Same |
| | `--private-key` | `--private-key` | ✅ Same |
| | `--installation-ids` | `--installation-id` | 🔄 Renamed |
| **Scope** | | | |
| | `--org` | `--org` | ✅ Same |
| | `--repos` | `--repos` | ✅ Same |
| | `--days` | `--days-back` | 🔄 Renamed |
| **Output** | | | |
| | `--output` | `--output-dir` | 🔄 Renamed |
| | `--excel-output` | `--format excel` | 🔄 Changed |
| | `--json-output` | `--format json` | 🔄 Changed |
| | `--csv-output` | `--format csv` | 🔄 Changed |
| **Analysis** | | | |
| | `--include-forks` | `--include-forks` | ✅ Same |
| | `--include-archived` | `--include-archived` | ✅ Same |
| | `--max-repos` | `--max-repos` | ✅ Same |
| | N/A | `--exclude-bots` | ➕ New |
| | N/A | `--include-empty` | ➕ New |
| **Logging** | | | |
| | `--verbose` | `--log-level DEBUG` | 🔄 Enhanced |
| | N/A | `--log-file` | ➕ New |

### Legend
- ✅ Same: No changes required
- 🔄 Renamed/Changed: Update required
- ➕ New: Optional new feature

## New Features and Usage

### Bot Account Filtering

**New Feature**: Automatically detect and filter bot accounts

```bash
# Enable bot filtering (recommended)
python github_org_stats_unified.py \
  --org myorg \
  --token ghp_token \
  --exclude-bots
```

**Detected Bot Patterns:**
- `dependabot`, `renovate[bot]`, `github-actions[bot]`
- `codecov-bot`, `snyk-bot`, `imgbot`
- Custom patterns configurable

### Empty Repository Handling

**New Feature**: Control inclusion of repositories with no recent activity

```bash
# Exclude empty repositories (default behavior)
python github_org_stats_unified.py --org myorg --token ghp_token

# Include empty repositories
python github_org_stats_unified.py \
  --org myorg \
  --token ghp_token \
  --include-empty
```

### Enhanced Logging

**New Feature**: Structured logging with multiple levels

```bash
# Debug logging to file
python github_org_stats_unified.py \
  --org myorg \
  --token ghp_token \
  --log-level DEBUG \
  --log-file analysis.log

# Warning level to console
python github_org_stats_unified.py \
  --org myorg \
  --token ghp_token \
  --log-level WARNING
```

### Configuration Files

**New Feature**: JSON configuration files for complex setups

```json
{
  "authentication": {
    "app_id": 12345,
    "private_key_path": "/path/to/key.pem",
    "installation_mappings": {
      "org1": 111,
      "org2": 222
    }
  },
  "analysis": {
    "days_back": 60,
    "max_repos": 200,
    "exclude_bots": true,
    "include_empty": false
  },
  "output": {
    "format": "all",
    "output_dir": "./reports"
  }
}
```

Usage:
```bash
python github_org_stats_unified.py --config config.json --org myorg
```

## Breaking Changes

### 1. Default Output Format

**Change**: Default output format changed from JSON to Excel

**Impact**: Scripts expecting JSON output by default will need updates

**Migration**:
```bash
# Old behavior (JSON default)
python old_script.py --org myorg --token ghp_token

# New behavior (Excel default)
python github_org_stats_unified.py --org myorg --token ghp_token

# To maintain JSON output
python github_org_stats_unified.py --org myorg --token ghp_token --format json
```

### 2. Argument Name Changes

**Changes**: Several arguments renamed for consistency

**Migration Required**:
- `--days` → `--days-back`
- `--installation-ids` → `--installation-id`
- `--output` → `--output-dir`
- `--verbose` → `--log-level DEBUG`

### 3. Excel Output Structure

**Change**: Excel output now includes multiple sheets with enhanced formatting

**Impact**: Scripts parsing Excel files may need updates

**New Excel Structure**:
- `Repository_Data`: Main repository data
- `Summary`: Organization-level statistics
- `Contributors`: Top contributors analysis
- `Languages`: Language distribution
- `Errors`: Error tracking information

### 4. Error Handling Behavior

**Change**: More robust error handling with categorization

**Impact**: Fewer fatal errors, more graceful degradation

**Migration**: Review error handling in automation scripts

## Configuration Migration

### Environment Variables

**Old Scripts**: Limited environment variable support

**Unified Script**: Enhanced environment variable support

```bash
# Set GitHub App credentials
export GITHUB_APP_ID=12345
export GITHUB_PRIVATE_KEY_PATH=/path/to/key.pem

# Run without specifying credentials
python github_org_stats_unified.py --org myorg --installation-id 67890
```

### Configuration File Migration

**Create configuration file from command line arguments:**

```bash
# Old command line approach
python old_script.py \
  --org myorg \
  --app-id 12345 \
  --private-key key.pem \
  --installation-ids "org1:111,org2:222" \
  --days 90 \
  --max-repos 500 \
  --include-forks \
  --excel-output
```

**New configuration file approach:**

```json
{
  "authentication": {
    "app_id": 12345,
    "private_key_path": "key.pem",
    "installation_mappings": {
      "org1": 111,
      "org2": 222
    }
  },
  "analysis": {
    "days_back": 90,
    "max_repos": 500,
    "include_forks": true,
    "exclude_bots": true
  },
  "output": {
    "format": "excel",
    "output_dir": "./reports"
  }
}
```

```bash
# Simplified command line
python github_org_stats_unified.py --config config.json --org myorg
```

## Output Format Changes

### JSON Output

**Compatibility**: Maintains backward compatibility with original JSON structure

**Enhancements**:
- Additional metadata fields
- Enhanced error information
- Timestamp standardization

### CSV Output

**Changes**: Flattened structure for complex nested data

**Migration**: Review CSV parsing logic for nested fields

### Excel Output

**Major Changes**: Complete redesign with multiple sheets

**Migration Steps**:
1. Update Excel parsing code to handle multiple sheets
2. Review column names (may have changed due to sanitization)
3. Update cell references for summary data
4. Consider using the new Summary sheet for high-level metrics

## Performance Improvements

### Rate Limit Management

**Old Scripts**: Basic rate limiting

**Unified Script**: Advanced rate limit management
- Automatic rate limit detection
- Intelligent waiting strategies
- Rate limit buffer management

### Memory Optimization

**New Features**:
- Adaptive batch sizing
- Memory-efficient processing
- Configurable limits

### Parallel Processing Considerations

**Recommendation**: The unified script is optimized for single-threaded use. For parallel processing:

```bash
# Process different organizations in parallel
python github_org_stats_unified.py --org org1 --token token1 &
python github_org_stats_unified.py --org org2 --token token2 &
python github_org_stats_unified.py --org org3 --token token3 &
wait
```

## Troubleshooting Migration Issues

### Common Migration Problems

#### 1. Authentication Issues

**Problem**: GitHub App authentication fails after migration

**Solution**:
```bash
# Test authentication separately
python -c "
from github_org_stats_unified import GitHubAppTokenManager, load_private_key
token_manager = GitHubAppTokenManager(12345, load_private_key('key.pem'))
print('Authentication successful')
"
```

#### 2. Missing Dependencies

**Problem**: Import errors for new dependencies

**Solution**:
```bash
pip install requests pandas PyGithub PyJWT tqdm openpyxl pytz
```

#### 3. Output Format Issues

**Problem**: Expecting JSON but getting Excel

**Solution**:
```bash
# Explicitly specify JSON format
python github_org_stats_unified.py --org myorg --token ghp_token --format json
```

#### 4. Rate Limit Problems

**Problem**: Rate limits hit more frequently

**Solution**:
```bash
# Use GitHub App authentication for higher limits
python github_org_stats_unified.py \
  --org myorg \
  --app-id 12345 \
  --private-key key.pem \
  --installation-id 67890
```

#### 5. Large Organization Performance

**Problem**: Script times out or runs out of memory

**Solution**:
```bash
# Limit repository count and enable optimizations
python github_org_stats_unified.py \
  --org myorg \
  --token ghp_token \
  --max-repos 100 \
  --exclude-bots \
  --log-level WARNING
```

### Migration Validation

**Test migration with a small subset:**

```bash
# Test with limited repositories
python github_org_stats_unified.py \
  --org myorg \
  --token ghp_token \
  --max-repos 5 \
  --log-level DEBUG \
  --format all
```

**Compare outputs:**

```bash
# Generate both old and new outputs
python old_script.py --org myorg --token ghp_token > old_output.json
python github_org_stats_unified.py --org myorg --token ghp_token --format json

# Compare key metrics
```

### Getting Help

If you encounter issues during migration:

1. **Check the logs**: Use `--log-level DEBUG` for detailed information
2. **Review the README**: Comprehensive documentation available
3. **Run tests**: Use the test suite to validate functionality
4. **Create an issue**: Report problems with detailed information

### Migration Checklist

- [ ] Install required dependencies
- [ ] Update script name in automation
- [ ] Update command line arguments
- [ ] Test authentication methods
- [ ] Validate output formats
- [ ] Update parsing logic for new Excel structure
- [ ] Test with small dataset first
- [ ] Update documentation and runbooks
- [ ] Train team members on new features
- [ ] Monitor performance after migration

## Conclusion

The unified script provides significant improvements while maintaining compatibility with existing workflows. The migration process is straightforward for most use cases, with the main changes being argument names and enhanced output formats.

Key benefits after migration:
- Single tool instead of three separate scripts
- Enhanced error handling and recovery
- Better performance and rate limit management
- Professional Excel output with multiple sheets
- Advanced filtering and analysis options
- Comprehensive logging and debugging capabilities

For complex migrations or enterprise deployments, consider using configuration files to manage settings and reduce command line complexity.