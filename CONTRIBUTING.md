# Contributing to GitHub Organization Statistics Tool

Welcome to the GitHub Organization Statistics Tool project! We're excited that you're interested in contributing. This guide will help you get started with contributing to our comprehensive tool for analyzing GitHub organization statistics.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Testing](#testing)
- [Documentation](#documentation)
- [Release Process](#release-process)
- [Code of Conduct](#code-of-conduct)
- [Getting Help](#getting-help)

## 🚀 Project Overview

The GitHub Organization Statistics Tool is a comprehensive, open-source Python application that analyzes GitHub organization statistics including:

- Repository metrics (stars, forks, issues, languages)
- Contributor activity and insights
- Code quality metrics and dependency analysis
- Multi-organization support with GitHub Apps
- Advanced filtering and bot detection
- Multiple output formats (JSON, CSV, Excel)

### Key Features
- **Multi-authentication**: Supports both Personal Access Tokens and GitHub Apps
- **Advanced Analytics**: Dependency analysis, submodule detection, GitHub Actions integration
- **Performance Optimized**: Adaptive batch sizing, rate limit management, memory optimization
- **Production Ready**: Comprehensive error handling, logging, and testing

## 🏁 Getting Started

### Prerequisites

Before contributing, ensure you have:

- **Python 3.7+** (we support Python 3.7-3.12)
- **Git** for version control
- **pip** package manager
- A **GitHub account** for testing and contributions

### Quick Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/github-org-stats.git
   cd github-org-stats
   ```

3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/zoharbabin/github-org-stats.git
   ```

## 🛠️ Development Setup

### Installation for Development

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install in development mode** with all dependencies:
   ```bash
   pip install -e .[dev]
   ```

   This installs:
   - **Core dependencies**: PyGithub, pandas, numpy, requests, PyJWT, tqdm, openpyxl, pytz
   - **Development tools**: pytest, pytest-cov, black, flake8, mypy

### Development Dependencies

Our development stack includes:

- **[pytest](https://pytest.org/)** (≥6.0.0) - Testing framework
- **[pytest-cov](https://pytest-cov.readthedocs.io/)** (≥2.10.0) - Coverage reporting
- **[black](https://black.readthedocs.io/)** (≥21.0.0) - Code formatting
- **[flake8](https://flake8.pycqa.org/)** (≥3.8.0) - Linting
- **[mypy](https://mypy.readthedocs.io/)** (≥0.800) - Type checking

### Running Tests

Run the comprehensive test suite:

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=github_org_stats --cov-report=html

# Run specific test categories
python tests/test_github_org_stats.py --category auth
python tests/test_github_org_stats.py --category data
python tests/test_github_org_stats.py --category excel
```

### Code Formatting and Linting

We maintain high code quality standards:

```bash
# Format code with Black
black .

# Check linting with flake8
flake8 github_org_stats.py tests/

# Type checking with mypy
mypy github_org_stats.py
```

### Configuration

Our code style configuration is defined in [`pyproject.toml`](pyproject.toml):

- **Black**: 88 character line length, Python 3.7+ target
- **pytest**: Configured for `tests/` directory with verbose output
- **mypy**: Strict type checking enabled

## 🤝 Contributing Guidelines

### How to Report Bugs

1. **Check existing issues** first to avoid duplicates
2. **Use the bug report template** when creating new issues
3. **Include detailed information**:
   - Python version and operating system
   - Command used and expected vs actual behavior
   - Complete error messages and stack traces
   - Minimal reproduction steps

**Example Bug Report:**
```
**Bug Description**: Rate limit exceeded when analyzing large organizations

**Environment**:
- Python 3.9.0
- macOS 12.0
- github-org-stats v1.0.0

**Command Used**:
```bash
python github_org_stats.py --org large-org --token ghp_xxx --max-repos 1000
```

**Error Message**:
```
RateLimitExceededException: API rate limit exceeded
```

**Expected**: Should handle rate limits gracefully with retries
**Actual**: Script crashes with unhandled exception
```

### How to Suggest Features

1. **Check the roadmap** and existing feature requests
2. **Open a feature request issue** with:
   - Clear description of the proposed feature
   - Use cases and benefits
   - Potential implementation approach
   - Any breaking changes or considerations

### Pull Request Process

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/amazing-feature
   ```

2. **Make your changes** following our coding standards

3. **Add or update tests** for your changes

4. **Run the full test suite**:
   ```bash
   python -m pytest tests/
   black .
   flake8 github_org_stats.py tests/
   mypy github_org_stats.py
   ```

5. **Update documentation** if needed

6. **Commit your changes** with clear messages:
   ```bash
   git commit -m "feat: add dependency vulnerability scanning
   
   - Add support for scanning package.json, requirements.txt
   - Include vulnerability count in repository metrics
   - Add tests for vulnerability detection
   - Update documentation with new feature"
   ```

7. **Push to your fork** and **create a pull request**

8. **Address review feedback** promptly

### Code Style Guidelines

#### Python Code Standards

- **Follow PEP 8** with Black formatting (88 character line length)
- **Use type hints** for all function parameters and return values
- **Write docstrings** for all public functions and classes
- **Keep functions focused** and under 50 lines when possible
- **Use meaningful variable names** and avoid abbreviations

#### Example Code Style:

```python
def get_repository_metrics(
    repo: Repository, 
    days_back: int = 30,
    exclude_bots: bool = True
) -> Dict[str, Any]:
    """
    Collect comprehensive metrics for a GitHub repository.
    
    Args:
        repo: PyGithub Repository object
        days_back: Number of days to analyze for activity metrics
        exclude_bots: Whether to exclude bot accounts from statistics
        
    Returns:
        Dictionary containing repository metrics including stars, forks,
        issues, contributors, and activity statistics
        
    Raises:
        GitHubException: If repository access fails
        ValueError: If days_back is negative
    """
    if days_back < 0:
        raise ValueError("days_back must be non-negative")
        
    metrics = {
        'name': repo.name,
        'stars': repo.stargazers_count,
        'forks': repo.forks_count,
        'issues': repo.open_issues_count,
    }
    
    # Add activity metrics
    commit_stats = get_commit_stats(repo, days_back, exclude_bots)
    metrics.update(commit_stats)
    
    return metrics
```

### Commit Message Conventions

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- **feat**: New features
- **fix**: Bug fixes
- **docs**: Documentation changes
- **style**: Code style changes (formatting, etc.)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

**Examples:**
```
feat: add support for GitHub Enterprise Server
fix: handle rate limit exceeded gracefully
docs: update installation instructions for Windows
test: add integration tests for multi-org analysis
refactor: extract authentication logic into separate class
```

## 🧪 Testing

### Test Structure

Our test suite is comprehensive and organized by functionality:

```
tests/
├── __init__.py
└── test_github_org_stats.py  # Main test file with all test classes
```

### Test Categories

- **Authentication Tests**: GitHub App and PAT authentication
- **Bot Detection Tests**: Bot account filtering and detection
- **Data Processing Tests**: Repository analysis and metrics collection
- **Excel Output Tests**: Data sanitization and Excel generation
- **Error Handling Tests**: Error tracking and recovery
- **Configuration Tests**: Argument parsing and config loading
- **Integration Tests**: End-to-end workflow testing
- **Performance Tests**: Scaling and optimization features

### Writing Tests

When adding new functionality:

1. **Add unit tests** for individual functions
2. **Add integration tests** for complete workflows
3. **Test error conditions** and edge cases
4. **Mock external dependencies** (GitHub API calls)
5. **Maintain test coverage** above 80%

**Example Test:**

```python
def test_get_repository_metrics_with_valid_repo(self):
    """Test repository metrics collection with valid repository."""
    mock_repo = Mock()
    mock_repo.name = "test-repo"
    mock_repo.stargazers_count = 100
    mock_repo.forks_count = 25
    mock_repo.open_issues_count = 5
    
    metrics = get_repository_metrics(mock_repo, days_back=30)
    
    self.assertEqual(metrics['name'], "test-repo")
    self.assertEqual(metrics['stars'], 100)
    self.assertEqual(metrics['forks'], 25)
    self.assertEqual(metrics['issues'], 5)
```

### Running Specific Tests

```bash
# Run authentication tests only
python tests/test_github_org_stats.py --category auth

# Run with verbose output
python tests/test_github_org_stats.py --verbose

# Stop on first failure
python tests/test_github_org_stats.py --failfast
```

## 📚 Documentation

### Updating Documentation

When contributing, please update relevant documentation:

1. **README.md**: For new features, installation changes, or usage updates
2. **CHANGELOG.md**: For all user-facing changes
3. **Code comments**: For complex logic or algorithms
4. **Docstrings**: For all public functions and classes

### Documentation Standards

- **Use clear, concise language**
- **Include code examples** for new features
- **Update command-line help** for new arguments
- **Add troubleshooting sections** for common issues

### Examples and Guides

When adding new features, consider adding:

- **Usage examples** in the README
- **Configuration examples** in `config/`
- **Setup guides** in `examples/`

## 🚀 Release Process

### Versioning

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Workflow

1. **Update version** in [`pyproject.toml`](pyproject.toml)
2. **Update CHANGELOG.md** with release notes
3. **Create release branch**: `release/v1.1.0`
4. **Run full test suite** and quality checks
5. **Create pull request** to main branch
6. **Tag release** after merge: `git tag v1.1.0`
7. **Create GitHub release** with release notes

### Release Checklist

- [ ] All tests pass
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Version bumped in pyproject.toml
- [ ] No breaking changes without major version bump
- [ ] Examples and guides tested

## 📜 Code of Conduct

### Our Standards

We are committed to providing a welcoming and inclusive environment:

- **Be respectful** and considerate in all interactions
- **Be collaborative** and help others learn and grow
- **Be patient** with newcomers and different experience levels
- **Be constructive** in feedback and criticism
- **Focus on what's best** for the community and project

### Unacceptable Behavior

- Harassment, discrimination, or offensive comments
- Personal attacks or trolling
- Publishing private information without consent
- Spam or off-topic discussions

### Enforcement

Project maintainers are responsible for clarifying standards and will take appropriate action for unacceptable behavior. This may include warnings, temporary bans, or permanent removal from the project.

### Reporting

Report unacceptable behavior to the project maintainers via:
- **GitHub Issues** (for public matters)
- **Email** to project maintainers (for private matters)

## 🆘 Getting Help

### Where to Ask Questions

1. **GitHub Discussions**: For general questions and community support
2. **GitHub Issues**: For bug reports and feature requests
3. **README.md**: For usage instructions and examples
4. **Code Comments**: For implementation details

### Common Questions

**Q: How do I set up GitHub App authentication?**
A: See our comprehensive [GitHub App Setup Guide](examples/github_app_setup.md)

**Q: How do I analyze multiple organizations?**
A: Use the `--installation-id` parameter with multiple mappings: `"org1:id1,org2:id2"`

**Q: Why is my analysis slow?**
A: Try reducing `--max-repos`, using `--exclude-bots`, or switching to JSON output format

**Q: How do I contribute a new output format?**
A: Add the format logic to the main script, update argument parsing, add tests, and update documentation

### Debug Mode

For troubleshooting contributions:

```bash
python github_org_stats.py \
  --org test-org \
  --token your-token \
  --log-level DEBUG \
  --log-file debug.log \
  --max-repos 5
```

### Development Resources

- **[PyGithub Documentation](https://pygithub.readthedocs.io/)** - GitHub API wrapper
- **[pandas Documentation](https://pandas.pydata.org/docs/)** - Data manipulation
- **[pytest Documentation](https://docs.pytest.org/)** - Testing framework
- **[GitHub API Documentation](https://docs.github.com/en/rest)** - REST API reference

---

## 🙏 Thank You

Thank you for contributing to the GitHub Organization Statistics Tool! Your contributions help make this tool better for everyone in the open-source community.

**Questions?** Don't hesitate to ask in [GitHub Discussions](https://github.com/zoharbabin/github-org-stats/discussions) or open an issue.

**Happy Contributing!** 🎉

---

*This contributing guide is a living document. Please suggest improvements via pull requests or issues.*