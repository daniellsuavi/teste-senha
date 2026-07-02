import string
import secrets

def gerar_senha(comprimento=12, usar_maiusculas=True, usar_numeros=True, usar_especiais=True):
    """
    Gera uma senha segura e aleatória com base nas preferências do usuário.
    """
    
    caracteres = string.ascii_lowercase
    
   
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiais:
        caracteres += string.punctuation


    if not caracteres:
        raise ValueError("Nenhum tipo de caractere foi selecionado!")

    
    senha = ''.join(secrets.choice(caracteres) for _ in range(comprimento))
    return senha


if __name__ == "__main__":
    print("--- GERADOR DE SENHAS SEGUIRAS ---")
    
    try:
       
        tamanho = int(input("Digite o comprimento da senha (ex: 16): "))
        
        senha_gerada = gerar_senha(
            comprimento=tamanho,
            usar_maiusculas=True,
            usar_numeros=True,
            usar_especiais=True
        )
        
        print("\n" + "="*30)
        print(f"Sua senha gerada é: {senha_gerada}")
        print("="*30)
        
    except ValueError:
        print("Por favor, digite um número válido para o comprimento.")