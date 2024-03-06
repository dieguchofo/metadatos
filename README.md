Esto va a hacer un .json que tenga una entrada por trabajo de titulación con:
    - nombre de lx autorx
    - título del trabajo
    - año de publicación
    - nombre del pdf (ej. 0842757.pdf)

Para hacer esto necesito:
1. con python (requests + beautifulSoup) una especie de crawler que descargue la sopa de cada página de resultados de tesiunam
2. contar con que hay trabajos que no tienen links a los textos con algún loop 
3. ordenar las sopas en un .json

### CÓMO FUNCIONA ###
1.py 
    input: urls_manuales.txt, en donde cada línea debe ser el url de una página de resultados de tesiunam.
    output: sopa.txt, que es todo el html de todas las páginas de resultados pegadas.

2.py 
    input: sopa.txt
    output: metadatos.json, un .json con una entrada para cada trabajo de titulación. Tiene
        nombre, titulo, año y doc_num (ej. 0607538). Todos son strings.


### QUÉ ESTOY HACIENDO AHORA ### 
NADA, ESTO ESTÁ TERMINADO

### SOLUCIONADO ###
## 1 ##
Corrí 1.py para ver si me puedo conectar a tesiunam. No pude. Este es el error:
[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1123)

# SOLUCIÓN
ignoré ssl con "response = requests.get(url.strip(), verify=False)", verify=false no verifica nada