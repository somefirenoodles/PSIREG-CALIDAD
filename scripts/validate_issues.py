import json
import os
import re
import sys
import urllib.request

REPO = os.environ.get('GITHUB_REPOSITORY', 'somefirenoodles/VSEST-Lite')
TOKEN = os.environ.get('GITHUB_TOKEN')
VALID_PREFIXES = ('[ARTEFACTO]', '[RIESGO]', '[ZAP]', '[EVALUACION]')
VALID_STATES = {'Pendiente', 'En elaboracion', 'En revision', 'Con observaciones', 'Aprobado', 'Cerrado', 'No ejecutable'}
VALID_PHASES = {'Identificacion', 'Planificacion', 'Elaboracion', 'Revision', 'Correccion', 'Validacion', 'Cierre'}


def api(path):
    url = f'https://api.github.com/repos/{REPO}{path}'
    headers = {'Accept': 'application/vnd.github+json'}
    if TOKEN:
        headers['Authorization'] = f'Bearer {TOKEN}'
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as res:
        return json.loads(res.read().decode('utf-8'))


def field(body, name):
    if not body:
        return ''
    pattern = rf'### {re.escape(name)}\s*\n\s*(.+?)(?=\n### |\Z)'
    match = re.search(pattern, body, re.S | re.I)
    if match:
        return match.group(1).strip()
    return ''


def is_structured(title):
    return any((title or '').startswith(prefix) for prefix in VALID_PREFIXES)


def main():
    errors = []
    issues = api('/issues?state=open&per_page=100')
    for issue in issues:
        if 'pull_request' in issue:
            continue
        body = issue.get('body') or ''
        title = issue.get('title') or ''
        number = issue.get('number')

        if not is_structured(title):
            continue

        if not field(body, 'Codigo'):
            errors.append(f'Issue #{number}: sin Codigo')

        estado = field(body, 'Estado')
        fase = field(body, 'Fase')
        evidencia = field(body, 'Evidencia')

        if title.startswith('[ARTEFACTO]'):
            if fase and fase not in VALID_PHASES:
                errors.append(f'Issue #{number}: Fase invalida: {fase}')
            if estado and estado not in VALID_STATES:
                errors.append(f'Issue #{number}: Estado invalido: {estado}')
            if estado in {'Aprobado', 'Cerrado'} and not evidencia:
                errors.append(f'Issue #{number}: aprobado/cerrado sin Evidencia')

        if title.startswith('[RIESGO]'):
            for required in ['Riesgo', 'Probabilidad', 'Impacto', 'Prioridad', 'Mitigacion']:
                if not field(body, required):
                    errors.append(f'Issue #{number}: riesgo sin {required}')

        if title.startswith('[ZAP]'):
            for required in ['Severidad', 'Confianza', 'Estado', 'Evidencia']:
                if not field(body, required):
                    errors.append(f'Issue #{number}: ZAP sin {required}')

        if title.startswith('[EVALUACION]'):
            for required in ['Caracteristica', 'Criterio', 'Resultado', 'Evidencia']:
                if not field(body, required):
                    errors.append(f'Issue #{number}: evaluacion sin {required}')

    if errors:
        print('\n'.join(errors))
        sys.exit(1)
    print('Validacion documental completada')


if __name__ == '__main__':
    main()
