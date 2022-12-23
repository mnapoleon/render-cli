"""Utility for dealing with env vars."""


def convert_env_var_file(env_var_file_name: str) -> dict:
    """Converts env file into key value for sending to Render."""
    env_vars_from_file = {}
    with open(env_var_file_name) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            else:
                var, value = line.split("=")
                env_vars_from_file[var.strip()] = value.strip()
    return env_vars_from_file


def convert_from_render_env_format(env_vars) -> dict:
    """Converts json response from env vars to dict of env vars."""
    evs = {}
    for env_var in env_vars:
        ev = env_var["envVar"]
        evs[ev["key"]] = ev["value"]
    return evs


def convert_to_render_env_format(env_vars: dict) -> list[dict]:
    """Converts a dict to a list[dict] with format for render api."""
    results = []
    for key, value in env_vars.items():
        results.append({"key": key, "value": value})
    return results
