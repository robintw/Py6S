# Py6S Modernization: Roadmap to Modern, Maintainable, Testable Python Code

## Executive Summary

Py6S is a stable, production-ready wrapper for the 6S Radiative Transfer Model with ~10,847 lines of Python code across 31 files. While the package functions correctly, the codebase contains numerous patterns from the Python 2/early Python 3 era (circa 2012-2015) that are now outdated. This issue provides a comprehensive analysis of the current state and a prioritized roadmap for modernizing Py6S to align with current Python best practices (2024-2025).

**Current Version:** 1.9.2
**Python Support:** 3.6, 3.7, 3.8, 3.9, 3.10 (tested)
**Test Coverage:** 54 test functions across 6 test files

---

## Current State Analysis

### Project Structure
```
Py6S/
├── Py6S/                      # Main package (~8,723 lines)
│   ├── sixs.py               # Core wrapper (17,051 lines - contains wavelength data)
│   ├── outputs.py            # Output parsing (17,727 lines - contains large lookup tables)
│   ├── Params/               # Parameter configuration (7 modules)
│   └── SixSHelpers/          # Helper utilities (5 modules)
├── tests/                    # Test suite (2,124 lines, pytest + unittest)
├── doc/                      # Sphinx documentation (RST format)
├── .github/workflows/        # GitHub Actions CI/CD
└── setup.py                  # Traditional setup configuration
```

### Key Dependencies
- **Core:** numpy, scipy, pysolar (>=0.9)
- **Testing:** pytest, pytest-cov, unittest (hybrid approach)
- **Documentation:** Sphinx with autodoc
- **Code Quality:** Black, isort (pre-commit hooks configured but outdated)

---

## Outdated Patterns and Technical Debt

### 1. **Package Management & Build System** 🔴 HIGH PRIORITY

**Current Issues:**
- Using legacy `setup.py` instead of modern `pyproject.toml` (PEP 517/518)
- References to deprecated `nose` test collector: `test_suite="nose.collector"` (setup.py:53)
- No dependency pinning or lockfiles for reproducible builds
- Minimal package metadata compared to modern standards

**Evidence:**
```python
# setup.py:43-66
setup(
    name="Py6S",
    packages=["Py6S", "Py6S.Params", "Py6S.SixSHelpers"],
    install_requires=REQS,
    python_requires=">=3",
    version="1.9.2",
    test_suite="nose.collector",  # nose is deprecated since 2015
    # ...
)
```

**Modern Standards:**
- PEP 621 (pyproject.toml for project metadata)
- PEP 517/518 (build system independence)
- Poetry/PDM/Hatch for dependency management
- Semantic versioning with automated releases

---

### 2. **Type Annotations** 🔴 HIGH PRIORITY

**Current Issues:**
- **Zero type hints** found across the entire codebase
- No `typing` module imports detected
- No mypy/pyright configuration for type checking
- Parameters and return types documented only in docstrings

**Impact:**
- No IDE autocomplete/IntelliSense for parameters
- No static type checking to catch errors before runtime
- Harder for new contributors to understand expected types
- Cannot leverage modern type-aware tooling

**Example from sixs.py:125-136:**
```python
def __init__(self, path=None):
    """Initialises the class and finds the right 6S executable to use.

    Arguments:
    * ``path`` -- (Optional) The path to the 6S executable
    """
    # Should be: def __init__(self, path: Optional[str] = None) -> None:
```

**Modern Standards:**
- PEP 484 (type hints)
- PEP 526 (variable annotations)
- PEP 604 (union types with `|` syntax for Python 3.10+)
- Type stubs for better IDE support

---

### 3. **Python 2/3 Compatibility Shims** 🟡 MEDIUM PRIORITY

**Current Issues:**
- Python 2 compatibility code still present despite Python 3-only requirement
- Manual `basestring` workaround for Python 3

**Evidence:**
```python
# sixs.py:40-42
# Fix for Python 3 where basestring is not available
if sys.version_info[0] >= 3:
    basestring = str
```

**Impact:**
- Unnecessary code complexity
- Confusion for new contributors
- Python 2 reached EOL on January 1, 2020

---

### 4. **Outdated Class Definitions** 🟡 MEDIUM PRIORITY

**Current Issues:**
- Using `class Foo(object):` syntax (Python 2 style)
- Found in 5 occurrences across 3 core files

**Evidence:**
```python
# sixs.py:45
class SixS(object):  # Should be: class SixS:

# outputs.py
class Outputs(object):  # Should be: class Outputs:
```

**Modern Standards:**
- In Python 3, all classes inherit from `object` by default
- Modern style omits explicit `(object)` inheritance

---

### 5. **String Formatting** 🟢 LOW PRIORITY (High Impact)

**Current Issues:**
- Heavy use of old-style `%` formatting (77 occurrences across 17 files)
- No f-strings (Python 3.6+ feature) detected

**Evidence:**
```python
# aeroprofile.py:50
return "%d" % type  # Should be: return f"{type}"

# Params/ground_reflectance.py (23 occurrences)
# Params/wavelength.py (6 occurrences)
# sixs.py (10 occurrences)
```

**Modern Standards:**
- f-strings (PEP 498) for readability and performance
- `.format()` for complex formatting
- Avoid `%` formatting except for logging

---

### 6. **File Path Handling** 🟡 MEDIUM PRIORITY

**Current Issues:**
- Using `os.path` module throughout instead of `pathlib.Path`
- Zero imports of `pathlib` detected
- Manual path manipulation with string operations

**Evidence:**
```python
# sixs.py:164-198
def _find_path(self, path=None):
    # Manual path searching and validation
    def is_exe(fpath):
        return os.path.exists(fpath) and os.access(fpath, os.X_OK)

    for path in os.environ["PATH"].split(os.pathsep):
        exe_file = os.path.join(path, program)
        # ...
```

**Modern Standards:**
- `pathlib.Path` for object-oriented path manipulation (Python 3.4+)
- `shutil.which()` for finding executables (instead of manual `_which()`)

---

### 7. **Test Infrastructure** 🟡 MEDIUM PRIORITY

**Current Issues:**
- Hybrid pytest + unittest approach (inefficient)
- All test classes inherit from `unittest.TestCase`
- Not leveraging pytest fixtures, parametrization, or modern features
- Tests use `self.assertEqual()` instead of simple `assert` statements

**Evidence:**
```python
# tests/test_general.py:39-42
class SimpleTests(unittest.TestCase):
    def test_inbuilt_test(self):
        result = SixS.test()
        self.assertEqual(result, 0)  # Should be: assert result == 0
```

**Modern Standards:**
- Pure pytest with fixtures and parametrization
- Simpler assertions without unittest boilerplate
- Pytest plugins for parallel execution, coverage, etc.

---

### 8. **CI/CD Configuration** 🟡 MEDIUM PRIORITY

**Current Issues:**
- Outdated `tox.ini` targeting Python 2.7 and 3.4 (both EOL)
- Legacy `.travis.yml` file (Travis CI for open source deprecated)
- Pre-commit hooks using old package versions
- No automated dependency updates (Dependabot/Renovate)

**Evidence:**
```ini
# tox.ini:1-2
[tox]
envlist = py27,py34  # Both EOL (2.7 in 2020, 3.4 in 2019)
```

```yaml
# .travis.yml (still present despite migration to GitHub Actions)
python:
  - "3.5"  # EOL September 2020
  - "3.6"  # EOL December 2021
```

```yaml
# .pre-commit-config.yaml
- repo: https://github.com/python/black
  rev: 20.8b1  # From 2020, current is 24.x
  language_version: python3.7  # Outdated target
```

**Modern Standards:**
- GitHub Actions only (already partially migrated)
- Test against actively supported Python versions (3.9-3.13)
- Automated dependency updates
- Nox instead of tox for more flexible test orchestration

---

### 9. **Code Organization & Modern Patterns** 🟢 LOW PRIORITY

**Current Issues:**
- No use of `dataclasses` for parameter objects (Python 3.7+)
- Factory methods using `@classmethod` instead of dedicated factory classes
- No use of `Enum` for constants (e.g., `AeroProfile.Continental = 1`)
- Parameter validation scattered across methods

**Evidence:**
```python
# Params/aeroprofile.py:25-36
class AeroProfile:
    NoAerosols = 0        # Should be Enum members
    Continental = 1
    Maritime = 2
    Urban = 3
    # ...

    @classmethod
    def PredefinedType(cls, type):
        return "%d" % type
```

**Modern Standards:**
- `dataclasses` for data containers with automatic `__init__`, `__repr__`, etc.
- `Enum` or `IntEnum` for typed constants
- `attrs` library for more advanced cases
- Pydantic for validation-heavy parameter classes

---

### 10. **Documentation** 🟢 LOW PRIORITY

**Current Issues:**
- Using reStructuredText (`.rst`) for all documentation
- Sphinx configuration from 2015-2016 era
- Mock imports in conf.py for handling dependencies
- Python 3.7 hardcoded in ReadTheDocs config (outdated)

**Evidence:**
```yaml
# .readthedocs.yaml:7-8
build:
  os: ubuntu-20.04
  tools:
    python: "3.7"  # Current Python is 3.13
```

**Modern Standards:**
- Markdown with MyST-Parser for Sphinx (more accessible)
- Modern Sphinx themes (Furo, Book theme)
- Auto-generated API docs from type hints
- Docstring format: Google or NumPy style

---

## Modernization Roadmap

### Phase 1: Foundation (Critical Path) 🔴

**Priority:** Address build system and type safety fundamentals

1. **Migrate to `pyproject.toml`**
   - Create PEP 621-compliant `pyproject.toml`
   - Choose modern build backend (Hatchling, PDM, or Poetry)
   - Add comprehensive project metadata
   - Deprecate `setup.py` (keep for backward compatibility initially)
   - **Benefit:** Future-proof packaging, better tooling support

2. **Add Type Annotations**
   - Start with public API (`SixS` class, `Outputs`, `Params` classes)
   - Add `py.typed` marker file for type stub distribution
   - Configure mypy with strict mode
   - Add type checking to CI/CD pipeline
   - Target: 100% coverage of public API, 80% overall
   - **Benefit:** Better IDE support, catch bugs at development time, improved documentation

3. **Modernize CI/CD**
   - Remove `.travis.yml` (GitHub Actions already in use)
   - Update `tox.ini` for Python 3.9-3.13 or migrate to `nox`
   - Update pre-commit hooks to latest versions
   - Add automated dependency updates (Dependabot)
   - Add type checking (mypy) to CI
   - **Benefit:** Test against current Python versions, automated maintenance

4. **Remove Python 2 Compatibility**
   - Remove `basestring = str` shim
   - Remove version checks for Python 2 vs 3
   - Update minimum Python version to 3.9 (current stable baseline)
   - **Benefit:** Cleaner codebase, reduce confusion

**Estimated Effort:** 2-3 weeks for experienced contributor
**Breaking Changes:** None if done carefully (may bump minimum Python version)

---

### Phase 2: Code Quality Improvements 🟡

**Priority:** Modernize code patterns and improve maintainability

5. **Modernize String Formatting**
   - Replace all `%` formatting with f-strings
   - Target files: `Params/*.py`, `sixs.py`, `outputs.py`
   - Use automated tools (flynt) where possible
   - **Benefit:** More readable code, slight performance improvement

6. **Adopt `pathlib` for Path Operations**
   - Replace `os.path` with `pathlib.Path` throughout
   - Replace manual `_which()` with `shutil.which()`
   - Update file I/O to use Path objects
   - **Benefit:** More Pythonic, cross-platform path handling

7. **Update Class Definitions**
   - Remove explicit `(object)` inheritance from all classes
   - Run automated fixer: `pyupgrade --py39-plus **/*.py`
   - **Benefit:** Modern Python 3 style, reduced noise

8. **Modernize Test Suite**
   - Convert `unittest.TestCase` classes to pure pytest
   - Replace `self.assertEqual()` with `assert` statements
   - Add pytest fixtures for common setup
   - Introduce parametrized tests for similar test cases
   - Add `pytest-xdist` for parallel test execution
   - **Benefit:** Faster tests, more maintainable test code

**Estimated Effort:** 1-2 weeks
**Breaking Changes:** None (internal changes only)

---

### Phase 3: Advanced Modernization 🟢

**Priority:** Optional improvements for long-term maintainability

9. **Introduce Modern Python Patterns**
   - Convert constant classes to `Enum` (e.g., `AeroProfile` types)
   - Consider `dataclasses` for simple parameter containers
   - Add runtime parameter validation with Pydantic (optional)
   - **Benefit:** Type-safe constants, better validation, clearer intent

10. **Improve Documentation Infrastructure**
    - Upgrade ReadTheDocs Python version to 3.11+
    - Consider MyST (Markdown) for new documentation
    - Update Sphinx theme to modern option (Furo)
    - Auto-generate API docs from type hints
    - **Benefit:** Better looking docs, easier to maintain

11. **Add Development Tooling**
    - Configure `ruff` for fast linting (replaces flake8, isort, more)
    - Add `pre-commit.ci` for automated pre-commit updates
    - Consider `commitizen` for conventional commits
    - Add PR templates and issue templates
    - **Benefit:** Consistent code style, easier contributions

12. **Performance Profiling & Optimization**
    - Add benchmarks for common operations
    - Profile and optimize hot paths
    - Consider Cython for performance-critical sections (if needed)
    - **Benefit:** Faster execution for large-scale simulations

**Estimated Effort:** 2-3 weeks
**Breaking Changes:** Minimal (mostly additions)

---

## Implementation Strategy

### Recommended Approach

**Option 1: Incremental (Recommended)**
- Tackle one phase at a time
- Each phase results in a minor version bump
- Allows community feedback and testing between phases
- Less risky, easier to review

**Option 2: Big Bang**
- Implement all changes in a feature branch
- Single major version bump (2.0.0)
- More disruptive but faster completion
- Requires extensive testing

### Breaking Changes Policy

**Proposed Minimum Python Version:**
- Current: `>=3` (effectively 3.6+)
- Proposed: `>=3.9` (EOL: October 2025)
- Rationale: Enables modern type hints, pattern matching, better performance

**API Compatibility:**
- Maintain backward compatibility for all public APIs
- Deprecate old patterns with warnings before removal
- Follow semantic versioning strictly

---

## Benefits of Modernization

### For Users
1. **Better IDE Support**: Type hints enable autocomplete and inline documentation
2. **Faster Bug Detection**: Type checking catches errors before runtime
3. **Performance**: Modern Python versions are faster (~10-30% improvement)
4. **Security**: Stay on supported Python versions with security updates

### For Maintainers
1. **Easier Maintenance**: Modern patterns reduce boilerplate
2. **Better Tooling**: Modern build system, faster linters (ruff)
3. **Automated Updates**: Dependabot keeps dependencies current
4. **Clearer Code**: f-strings, pathlib, type hints improve readability

### For Contributors
1. **Lower Barrier to Entry**: Modern Python patterns are what newcomers learn
2. **Better Documentation**: Type hints serve as inline documentation
3. **Faster Development**: Better IDE support accelerates contribution
4. **Standard Practices**: Aligns with ecosystem best practices

---

## Success Metrics

- [ ] Type hints: 100% of public API, 80%+ overall
- [ ] Test coverage: Maintain or exceed current coverage
- [ ] CI/CD: All tests passing on Python 3.9-3.13
- [ ] Build system: Successful pyproject.toml-based builds
- [ ] Documentation: API docs auto-generated from type hints
- [ ] Code quality: Ruff linter with zero errors
- [ ] Performance: No regression (within 5% of current performance)

---

## Community Input Needed

1. **Python Version Support**: Agree on minimum Python version (recommend 3.9+)
2. **Breaking Changes**: Tolerance for API changes (prefer backward compatible)
3. **Build Backend**: Poetry vs PDM vs Hatchling vs setuptools with pyproject.toml
4. **Timeline**: Phased approach vs. single major release
5. **Priorities**: Which phases are most important to users?

---

## Related Issues & PRs

- None yet - this is the foundational modernization tracking issue

---

## References

- [PEP 517 - Build System Independence](https://peps.python.org/pep-0517/)
- [PEP 518 - pyproject.toml](https://peps.python.org/pep-0518/)
- [PEP 621 - Project Metadata](https://peps.python.org/pep-0621/)
- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/)
- [Python 3.9-3.13 What's New](https://docs.python.org/3/whatsnew/)
- [Python Support Lifecycle](https://devguide.python.org/versions/)

---

## How to Contribute

Interested in helping? Here's how:

1. **Comment below** with your thoughts on priorities and breaking changes
2. **Claim a task** from Phase 1 to get started
3. **Open a PR** referencing this issue
4. **Join the discussion** on Python version support and tooling choices

Let's bring Py6S into 2025! 🚀
