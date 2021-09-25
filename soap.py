from zeep import Client

client = Client('http://www.soapclient.com/xml/soapresponder.wsdl')
result = client.service.Method1(bstrParam1='Hello, World!', bstrParam2='Hello, Python!')

print(result)

'''
Introdução rápida 
Zeep inspeciona o documento WSDL e gera o código correspondente para usar os serviços e tipos no documento. Isso fornece uma interface programática fácil de usar para um servidor SOAP.

A ênfase está em SOAP 1.1 e SOAP 1.2, no entanto, o Zeep também oferece suporte para ligações HTTP Get e Post.

A análise dos documentos XML é feita usando a biblioteca lxml . Esta é a biblioteca XML Python com melhor desempenho e conformidade disponível atualmente. Isso resulta em grandes benefícios de velocidade ao processar grandes respostas SOAP.

As especificações do SOAP são, infelizmente, muito vagas e deixam muitas coisas abertas para interpretação. Devido a isso, há muitos documentos WSDL disponíveis que são inválidos ou servidores SOAP que contêm bugs. O Zeep tenta ser o mais compatível possível, mas pode haver casos em que você terá problemas. Não hesite em enviar um problema neste caso (mas primeiro leia Relatando bugs ).
'''