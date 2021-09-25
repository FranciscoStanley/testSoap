from zeep import Client

client = Client('http://www.soapclient.com/xml/soapresponder.wsdl')
result = client.service.Method1(bstrParam1='Hello, World!', bstrParam2='Hello, Python!')

print(result)