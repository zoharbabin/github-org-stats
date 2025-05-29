# Changelog

All notable changes to the GitHub Organization Statistics Tool will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-05-29

### Added
- **🚀 Multi-Organization Analysis**: Revolutionary new `--org-ids` parameter enables analyzing multiple organizations in a single command run
  - Format: `--org-ids "org1:install_id1,org2:install_id2,org3:install_id3"`
  - Combines all repository data into unified output files
  - Each repository record includes organization attribution
  - Distributes max-repos limit intelligently across organizations
  - Enhanced Excel output with "Organization_Breakdown" sheet
- **Enhanced Authentication**: Improved environment variable support
  - Automatic detection of `GITHUB_APP_ID` and `GITHUB_PRIVATE_KEY_PATH`
  - Better validation logic for mixed authentication methods
  - Clearer error messages for authentication issues
- **Improved GitHub App Support**: Fixed permission issues with GitHub App authentication
  - Removed unnecessary `/user` endpoint calls that GitHub Apps can't access
  - Direct organization access for better compatibility
  - Enhanced logging for multi-organization authentication flows

### Changed
- **Command Line Interface**: Updated argument structure for multi-organization support
  - `--org` now optional (single organization mode)
  - `--org-ids` added for multi-organization mode (mutually exclusive with `--org`)
  - Enhanced help documentation with multi-organization examples
- **Output File Naming**: Intelligent filename generation based on analysis mode
  - Single org: `github_org_stats_orgname_timestamp.ext`
  - Multi org: `github_org_stats_org1_org2_timestamp.ext` or `github_org_stats_multi_org_N_orgs_timestamp.ext`
- **Excel Output Enhancement**: Additional sheets for multi-organization analysis
  - New "Organization_Breakdown" sheet with per-organization statistics
  - Enhanced summary sheet with total organization count
  - Better data organization and visualization

### Fixed
- **GitHub App Authentication**: Resolved 403 "Resource not accessible by integration" errors
  - Removed problematic `/user` endpoint verification calls
  - Streamlined authentication flow for GitHub Apps
- **Environment Variable Validation**: Fixed authentication validation to properly recognize environment variables
- **Multi-Organization Error Handling**: Enhanced error tracking and reporting across multiple organizations

## [1.0.1] - 2025-05-29

### Fixed
- **Language Name Sanitization**: Fixed C# vs C language detection conflicts in Excel output
  - Added `sanitize_language_names()` function to handle problematic language names
  - C# → CSharp, C++ → CPlusPlus, F# → FSharp transformations
  - Prevents Excel column name conflicts when exporting repository language statistics
  - Preserves original byte counts and statistical accuracy
  - Includes comprehensive logging of transformations applied
- **Excel Compatibility**: Resolved column name sanitization issues that caused data conflicts
- **Data Integrity**: Ensured language statistics remain accurate after name transformations

### Added
- Real-world integration tests for language name sanitization
- Comprehensive test coverage for C#, C++, and F# language handling
- Enhanced error handling and logging for language data processing

## [1.0.0] - 2025-05-28

### Added
- Initial release of the unified GitHub Organization Statistics Tool
- Comprehensive repository analysis and metrics collection
- Support for both Personal Access Token and GitHub App authentication
- Multi-organization support with GitHub Apps
- Advanced bot detection and filtering capabilities
- Multiple output formats (JSON, CSV, Excel) with professional formatting
- Intelligent rate limit management and retry mechanisms
- Robust error handling with detailed logging
- Configuration file support for complex setups
- Comprehensive test suite with 100% success rate
- Detailed documentation including usage guides and migration instructions

### Features
- **Repository Metrics**: Stars, forks, issues, watchers, size, and activity tracking
- **Contributor Analysis**: Top contributors with advanced bot filtering (20+ bot patterns)
- **Code Quality Insights**: Language statistics, dependency analysis from 7+ package managers
- **Security Information**: Branch protection, collaborators, teams, and admin detection
- **GitHub Actions**: Workflow information, recent runs, and configuration analysis
- **Release Tracking**: Latest releases, version information, and release history
- **Advanced Filtering**: Include/exclude forks, archived repos, empty repos, specific repositories
- **Performance Optimization**: Adaptive batch sizing, memory management, and rate limiting
- **Multi-format Output**: Professional Excel with multiple sheets, structured JSON, and CSV formats
- **Submodule Detection**: Git submodule identification and cataloging
- **Dependency Analysis**: Support for npm, pip, gem, maven, gradle, cargo, and go modules
- **Bot Detection**: Configurable bot patterns for dependabot, renovate, github-actions, and more

### Command Line Interface
- **Authentication Arguments**: `--token`, `--app-id`, `--private-key`, `--installation-id`, `--installation-ids`
- **Scope Arguments**: `--org` (required), `--repos`, `--days-back`
- **Output Arguments**: `--output-dir`, `--format`, `--config`
- **Logging Arguments**: `--log-level`, `--log-file`
- **Analysis Arguments**: `--include-forks`, `--include-archived`, `--max-repos`, `--exclude-bots`, `--include-empty`
- **Environment Variables**: `GITHUB_APP_ID`, `GITHUB_PRIVATE_KEY_PATH`, `GITHUB_TOKEN`

### Authentication
- Personal Access Token support for individual use with required permissions (repo, read:org, read:user)
- GitHub App authentication for enterprise deployments with higher rate limits
- Multi-installation support for analyzing multiple organizations simultaneously
- Environment variable configuration for secure credential management
- Secure private key handling with PEM format validation

### Output Formats
- **Excel**: Professional formatting with multiple sheets
  - Repository_Data: Complete repository information
  - Summary: Organization-level statistics
  - Contributors: Top contributors analysis
  - Languages: Language distribution
  - Errors: Error tracking information
- **JSON**: Structured data for programmatic access
- **CSV**: Flattened data for spreadsheet analysis

### Documentation
- Comprehensive README with quick start guide and complete usage documentation
- All authentication methods including Personal Access Token and GitHub App setup
- Command-line arguments reference with examples
- Configuration file documentation with complete example
- Troubleshooting section with common issues and solutions
- Development setup and contribution guidelines
- Example configurations and usage scripts

### Testing
- Complete test suite covering all major functionality
- Authentication system tests
- Data processing and validation tests
- Error handling and recovery tests
- Excel output and formatting tests
- Configuration management tests
- Performance and scaling tests

### Dependencies
- PyGithub >= 1.55.0 (GitHub API client)
- pandas >= 1.3.0 (Data processing)
- numpy >= 1.21.0 (Numerical operations)
- requests >= 2.25.0 (HTTP requests)
- PyJWT >= 2.0.0 (JWT token handling)
- tqdm >= 4.60.0 (Progress bars)
- openpyxl >= 3.0.0 (Excel output)
- pytz >= 2021.1 (Timezone handling)

### Performance
- Intelligent rate limit management
- Adaptive batch sizing based on organization size
- Memory-efficient processing for large datasets
- Configurable limits to prevent resource exhaustion
- Progress tracking with visual indicators

### Security
- Secure token and private key handling
- Input sanitization for all output formats
- Safe JSON parsing and file operations
- Proper error message sanitization
- Multiple authentication method support

## [Unreleased]

### Planned Features
- GraphQL API support for improved performance
- Additional output formats (HTML reports, PDF)
- Advanced analytics and trend analysis
- Integration with CI/CD pipelines
- Docker container support
- Web interface for interactive analysis
- Scheduled analysis and reporting
- Advanced filtering and search capabilities

### Improvements Under Consideration
- Enhanced caching mechanisms
- Parallel processing for large organizations
- Real-time analysis capabilities
- Integration with other development tools
- Advanced visualization options
- Custom report templates
- API endpoint for programmatic access

---

## Version History

### Pre-1.0.0 Development

The GitHub Organization Statistics Tool was developed through the consolidation of three separate scripts:

1. **github_org_stats.py** - Basic organization statistics
2. **github_org_stats_improved.py** - Enhanced repository analysis  
3. **github_multi_org_stats.py** - Multi-organization support

These scripts were unified into a single, comprehensive tool with enhanced features, better error handling, and professional packaging for open-source distribution.

### Migration Path

Users of the original scripts can migrate to version 1.0.0 using the provided migration guide. The unified tool maintains backward compatibility while providing significant improvements in functionality and reliability.

---

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## Support

For support, bug reports, and feature requests, please use the [GitHub Issues](https://github.com/your-org/github-org-stats/issues) page.