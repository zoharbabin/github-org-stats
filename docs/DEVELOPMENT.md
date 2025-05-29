# Development Guide

This guide provides information for developers who want to contribute to the GitHub Organization Statistics Tool.

## Table of Contents

- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Code Style](#code-style)
- [Testing](#testing)
- [Contributing](#contributing)
- [Release Process](#release-process)

## Development Setup

### Prerequisites

- Python 3.7 or higher
- Git
- Virtual environment tool (venv, conda, etc.)

### Setup Instructions

1. **Fork and Clone the Repository**
   ```bash
   git clone https://github.com/your-username/github-org-stats.git
   cd github-org-stats
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

4. **Verify Installation**
   ```bash
   python github_org_stats.py --help
   ```

## Project Structure

```
github-org-stats/
├── README.md                 # Main project documentation
├── LICENSE                   # MIT license
├── requirements.txt          # Production dependencies
├── requirements-dev.txt      # Development dependencies
├── setup.py                  # Package setup and installation
├── github_org_stats.py       # Main application script
├── config/
│   └── example_config.json   # Example configuration file
├── docs/
│   ├── USAGE.md             # User documentation
│   ├── MIGRATION.md         # Migration guide
│   └── DEVELOPMENT.md       # This file
├── tests/
│   ├── __init__.py
│   ├── test_github_org_stats.py  # Main test suite
│   └── test_results.md      # Test execution results
└── examples/
    ├── basic_usage.sh       # Basic usage examples
    ├── github_app_setup.md  # GitHub App setup guide
    └── sample_output.xlsx   # Sample output file
```

## Code Style

### Python Style Guidelines

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use [Black](https://black.readthedocs.io/) for code formatting
- Use [flake8](https://flake8.pycqa.org/) for linting
- Use [mypy](http://mypy-lang.org/) for type checking

### Code Formatting

```bash
# Format code with Black
black github_org_stats.py tests/

# Check linting with flake8
flake8 github_org_stats.py tests/

# Type checking with mypy
mypy github_org_stats.py
```

### Documentation Standards

- Use docstrings for all functions and classes
- Follow [Google docstring format](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Include type hints for function parameters and return values
- Update README.md for user-facing changes

## Testing

### Running Tests

```bash
# Run all tests
cd tests
python test_github_org_stats.py

# Run specific test categories
python test_github_org_stats.py --category auth
python test_github_org_stats.py --category data
python test_github_org_stats.py --category excel

# Run with verbose output
python test_github_org_stats.py --verbose

# Stop on first failure
python test_github_org_stats.py --failfast
```

### Test Categories

- **Authentication Tests**: GitHub App and PAT authentication
- **Bot Detection Tests**: Bot account filtering
- **Data Processing Tests**: Repository data collection
- **Excel Output Tests**: Data sanitization and formatting
- **Error Handling Tests**: Error tracking and recovery
- **Configuration Tests**: Config loading and validation
- **Integration Tests**: End-to-end workflows
- **Performance Tests**: Scaling and optimization

### Writing New Tests

1. Add test methods to appropriate test classes in `test_github_org_stats.py`
2. Use descriptive test method names: `test_feature_specific_behavior`
3. Include docstrings explaining what the test validates
4. Use mocking for external API calls
5. Test both success and failure scenarios

### Test Coverage

Aim for high test coverage across all major functionality:
- Authentication systems
- Data processing functions
- Error handling mechanisms
- Configuration management
- Output generation

## Contributing

### Contribution Workflow

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**
   - Write code following style guidelines
   - Add or update tests
   - Update documentation

3. **Test Changes**
   ```bash
   python test_github_org_stats.py
   black github_org_stats.py
   flake8 github_org_stats.py
   ```

4. **Commit Changes**
   ```bash
   git add .
   git commit -m "Add feature: description of changes"
   ```

5. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

### Commit Message Guidelines

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests when applicable

### Pull Request Guidelines

- Provide clear description of changes
- Include test results
- Update documentation if needed
- Ensure all tests pass
- Follow code review feedback

## Release Process

### Version Management

- Use [Semantic Versioning](https://semver.org/) (MAJOR.MINOR.PATCH)
- Update version in `setup.py` and `github_org_stats.py`
- Create git tags for releases

### Release Checklist

1. **Pre-release Testing**
   - Run full test suite
   - Test with real GitHub organizations
   - Verify all output formats
   - Check documentation accuracy

2. **Version Update**
   - Update version numbers
   - Update CHANGELOG.md
   - Update documentation

3. **Create Release**
   - Create git tag
   - Build distribution packages
   - Upload to PyPI (if applicable)
   - Create GitHub release

4. **Post-release**
   - Update documentation
   - Announce release
   - Monitor for issues

### Building Distribution

```bash
# Build source and wheel distributions
python setup.py sdist bdist_wheel

# Check distribution
twine check dist/*

# Upload to PyPI (maintainers only)
twine upload dist/*
```

## Development Tools

### Recommended IDE Setup

- **VS Code** with Python extension
- **PyCharm** Professional or Community
- Configure linting and formatting tools
- Set up debugging configuration

### Useful Development Commands

```bash
# Install in development mode
pip install -e .

# Run with debugging
python -m pdb github_org_stats.py --org test-org --token token

# Profile performance
python -m cProfile github_org_stats.py --org test-org --token token

# Generate documentation
python -m pydoc github_org_stats
```

## Debugging

### Common Issues

1. **Authentication Failures**
   - Verify token permissions
   - Check GitHub App installation
   - Validate private key format

2. **Rate Limit Issues**
   - Use GitHub App authentication
   - Implement proper delays
   - Monitor rate limit status

3. **Memory Issues**
   - Reduce batch sizes
   - Enable bot filtering
   - Limit repository count

### Debug Mode

Enable debug logging for troubleshooting:

```bash
python github_org_stats.py \
  --org your-org \
  --token your-token \
  --log-level DEBUG \
  --log-file debug.log
```

## Getting Help

- **Documentation**: Check existing documentation first
- **Issues**: Search existing GitHub issues
- **Discussions**: Use GitHub Discussions for questions
- **Code Review**: Request reviews from maintainers

## Code of Conduct

Please follow our Code of Conduct in all interactions:
- Be respectful and inclusive
- Focus on constructive feedback
- Help create a welcoming environment
- Report inappropriate behavior

---

Thank you for contributing to the GitHub Organization Statistics Tool!