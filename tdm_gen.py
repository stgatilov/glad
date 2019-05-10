import os, re

g_output_dir = '../darkmod_src/renderer'

for spec in ['gl', 'wgl', 'glx']:
    parts = [
        'python -m glad',
        '--spec="%s"' % spec,
        '--profile="compatibility"',
        '--reproducible',
        '--generator="c"',
        '--omit-khrplatform',
        '--local-files',
        '--out-path=%s' % g_output_dir,
    ]
    if spec == 'gl':
        parts.append('--api="gl=3.0"')
    cmd = ' '.join(parts);
    print(cmd)
    os.system(cmd)
