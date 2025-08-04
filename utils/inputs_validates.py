import re

def validar_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Primeiro dígito verificador
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto1 = 11 - (soma1 % 11)
    digito1 = 0 if resto1 >= 10 else resto1

    # Segundo dígito verificador
    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto2 = 11 - (soma2 % 11)
    digito2 = 0 if resto2 >= 10 else resto2

    return cpf[-2:] == f"{digito1}{digito2}"

def validar_oab(oab: str) -> bool:
    """
    Valida o formato do número de OAB.
    Formatos aceitos: UF + número (1-6 dígitos) + letra opcional.
    Pode conter hífen ou espaço entre UF e número.
    """
    # Remove espaços extras e deixa padrão
    oab = oab.strip().upper().replace('-', '').replace(' ', '')

    # Regex para UF (2 letras), número (1-6 dígitos), letra opcional
    pattern = r'^[A-Z]{2}\d{1,6}[A-Z]?$'
    return bool(re.match(pattern, oab))

