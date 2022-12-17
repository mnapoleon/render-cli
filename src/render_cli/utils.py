def convert_env_var_file(env_var_file_name):
    """Converts env file into key value for sending to Render."""
    env_vars = []
    with open(env_var_file_name) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            else:
                var, value = line.split("=")
                env_vars.append({"key": var.strip(), "value": value.strip()})
    return env_vars
