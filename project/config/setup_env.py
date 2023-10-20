env_file = 'config/.env'

with open('config/openrc-files/admin-openrc.sh', 'r') as rc_file, open(env_file, 'w') as env_out:
    env_out.write(f'OS_PASSWORD=nomoresecret\n')
    for line in rc_file:
        line = line.strip()
        if line.startswith('export '):
            parts = line[len('export '):].split('=')
            if len(parts) == 2:
                key = parts[0]
                value = parts[1].strip('"')
                if key != 'OS_PASSWORD':
                    env_out.write(f'{key}={value}\n')


print(f'Environment variables were written to {env_file} file')
