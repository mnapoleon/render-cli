"""Package-wide test fixtures."""


def pytest_configure(config):
    """Pytest configuration hook."""
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")
