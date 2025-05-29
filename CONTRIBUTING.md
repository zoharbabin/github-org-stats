# Contributing to GitHub Organization Statistics Tool

Thank you for your interest in contributing to the GitHub Organization Statistics Tool! This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Process](#development-process)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Community](#community)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

### Our Pledge

- **Be Respectful**: Treat everyone with respect and kindness
- **Be Inclusive**: Welcome newcomers and help them get started
- **Be Constructive**: Provide helpful feedback and suggestions
- **Be Patient**: Remember that everyone has different experience levels

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Git
- GitHub account
- Basic understanding of GitHub API and Python

### Development Setup

1. **Fork the Repository**
   ```bash
   # Fork on GitHub, then clone your fork
   git clone https://github.com/your-username/github-org-stats.git
   cd github-org-stats
   ```

2. **Set Up Development Environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

3. **Verify Setup**
   ```bash
   # Run tests
   cd tests
   python test_github_org_stats.py
   
   # Test basic functionality
   python ../github_org_stats.py --help
   ```

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **Bug Reports**: Help us identify and fix issues
- **Feature Requests**: Suggest new functionality
- **Code Contributions**: Implement features or fix bugs
- **Documentation**: Improve or add documentation
- **Testing**: Add or improve test coverage
- **Examples**: Provide usage examples and tutorials

### Reporting Issues

When reporting bugs or requesting features:

1. **Search Existing Issues**: Check if the issue already exists
2. **Use Issue Templates**: Follow the provided templates
3. **Provide Details**: Include relevant information:
   - Python version
   - Operating system
   - Command used
   - Error messages
   - Expected vs actual behavior

### Suggesting Features

For feature requests:

1. **Describe the Problem**: What problem does this solve?
2. **Propose a Solution**: How should it work?
3. **Consider Alternatives**: What other approaches could work?
4. **Implementation Ideas**: Any thoughts on how to implement it?

## Development Process

### Workflow

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b bugfix/issue-description
   ```

2. **Make Changes**
   - Write code following our coding standards
   - Add or update tests
   - Update documentation

3. **Test Your Changes**
   ```bash
   # Run all tests
   python test_github_org_stats.py
   
   # Run specific test categories
   python test_github_org_stats.py --category auth
   
   # Test with real data (if possible)
   python github_org_stats.py --org test-org --token test-token --max-repos 5
   ```

4. **Commit Changes**
   ```bash
   git add .
   git commit -m "Add feature: clear description of changes"
   ```

5. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

### Pull Request Process

1. **Create Pull Request**
   - Use descriptive title and description
   - Reference related issues
   - Include test results
   - Add screenshots if applicable

2. **Code Review**
   - Respond to feedback promptly
   - Make requested changes
   - Keep discussions constructive

3. **Merge**
   - Maintainers will merge approved PRs
   - Delete feature branch after merge

## Coding Standards

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use [Black](https://black.readthedocs.io/) for formatting
- Use [flake8](https://flake8.pycqa.org/) for linting
- Include type hints where appropriate

### Code Quality

```bash
# Format code
black github_org_stats.py tests/

# Check linting
flake8 github_org_stats.py tests/

# Type checking (optional but recommended)
mypy github_org_stats.py
```

### Documentation Standards

- Use docstrings for all functions and classes
- Follow Google docstring format
- Include examples in docstrings when helpful
- Update README.md for user-facing changes

### Example Function Documentation

```python
def get_repo_stats(repo, days_back: int = 30) -> Dict[str, Any]:
    """
    Get comprehensive statistics for a repository.
    
    Args:
        repo: GitHub repository object
        days_back: Number of days to look back for activity
        
    Returns:
        Dictionary containing repository statistics
        
    Example:
        >>> stats = get_repo_stats(repo, days_back=60)
        >>> print(stats['total_commits'])
        42
    """
```

## Testing Guidelines

### Test Categories

- **Unit Tests**: Test individual functions
- **Integration Tests**: Test component interactions
- **End-to-End Tests**: Test complete workflows
- **Performance Tests**: Test scalability and performance

### Writing Tests

1. **Test Structure**
   ```python
   def test_feature_specific_behavior(self):
       """Test that feature behaves correctly in specific scenario."""
       # Arrange
       input_data = create_test_data()
       
       # Act
       result = function_under_test(input_data)
       
       # Assert
       self.assertEqual(result, expected_value)
   ```

2. **Use Mocking**
   ```python
   @patch('github_org_stats.requests.get')
   def test_api_call(self, mock_get):
       """Test API call handling."""
       mock_get.return_value.json.return_value = {'test': 'data'}
       result = make_api_call()
       self.assertEqual(result['test'], 'data')
   ```

3. **Test Edge Cases**
   - Empty inputs
   - Invalid inputs
   - Network failures
   - Rate limit scenarios

### Running Tests

```bash
# All tests
python test_github_org_stats.py

# Specific category
python test_github_org_stats.py --category auth

# Verbose output
python test_github_org_stats.py --verbose

# Stop on first failure
python test_github_org_stats.py --failfast
```

## Documentation

### Types of Documentation

1. **Code Documentation**: Docstrings and comments
2. **User Documentation**: README, usage guides
3. **Developer Documentation**: Contributing, development setup
4. **API Documentation**: Function and class references

### Documentation Updates

- Update documentation with code changes
- Include examples for new features
- Keep documentation current and accurate
- Use clear, concise language

## Community

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Questions and general discussion
- **Pull Requests**: Code review and collaboration

### Getting Help

- **Documentation**: Check existing documentation first
- **Search Issues**: Look for similar problems
- **Ask Questions**: Use GitHub Discussions
- **Be Specific**: Provide context and details

### Helping Others

- **Answer Questions**: Help other users
- **Review Code**: Provide constructive feedback
- **Improve Documentation**: Fix typos and unclear sections
- **Share Examples**: Provide usage examples

## Recognition

Contributors are recognized in several ways:

- **Contributors List**: Listed in project documentation
- **Release Notes**: Mentioned in release announcements
- **GitHub Contributors**: Shown on repository page
- **Special Thanks**: Acknowledged for significant contributions

## Release Process

### Version Management

- Use [Semantic Versioning](https://semver.org/)
- Update version in relevant files
- Create git tags for releases

### Release Checklist

1. Update version numbers
2. Update CHANGELOG.md
3. Run full test suite
4. Create release notes
5. Tag release
6. Update documentation

## Questions?

If you have questions about contributing:

1. Check this document and other documentation
2. Search existing issues and discussions
3. Create a new discussion or issue
4. Be patient and respectful

Thank you for contributing to the GitHub Organization Statistics Tool!

---

**Happy Contributing! 🎉**