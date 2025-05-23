# Proyecto Numeros Complejos
Este es un proyecto en Python que contiene funciones para realizar operaciones con números complejos.ademas de contar con un archivo queprueba el correcto funcionamiento de las mismas.

 

## Funciones

 

### Suma de Números Complejos

 

La función `suma(a, b)` toma dos números complejos representados como tuplas `(parte_real, parte_imaginaria)` y devuelve la suma de los dos números complejos .

 

### Producto de Números Complejos

 

La función `producto(a, b)` calcula el producto de dos números complejos y devuelve el resultado en la forma de una tupla `(parte_real, parte_imaginaria)`.

 

### Resta de Números Complejos

 

La función `resta(a, b)` realiza la resta de dos números complejos y devuelve el resultado en una tupla `(parte_real, parte_imaginaria)`.

 

### División de Números Complejos

 

La función `division(a, b)` calcula la división de dos números complejos y devuelve el resultado en la forma de una tupla `(parte_real, parte_imaginaria)`.

 

### Módulo de un Número Complejo

 

La función `modulo(a)` calcula el módulo de un número complejo y devuelve el resultado.

 

### Conjugado de un Número Complejo

 

La función `conjugado(a)` calcula el conjugado de un número complejo y devuelve el resultado en una tupla `(parte_real, parte_imaginaria)`.

 

### Fase de un Número Complejo

 

La función `fase(a)` calcula la fase de un número complejo y devuelve el resultado en grados.

 

## Uso

 

Para utilizar estas funciones, importa el módulo `Libreria_Operaciones_Complejos` en tu script de Python:

 

```pythonfrom operaciones_complejas import suma, producto, resta, division, modulo, conjugado, fase# Luego puedes llamar a las funciones y utilizarlas en tu código para realizar alguna de las operaciones anterioemente mencionadas teniendo en cuenta que tanto como la entrada y  la salida de cada funcion es en una dupla.

```java
return (
        <div className="container">
            <h1>ECI Commerce - Registro de Pago</h1>
            {error && <p className="error">{error}</p>}

            <form onSubmit={submitPayment} className="payment-form">
                <label>
                    ID Usuario:
                    <input
                        type="text"
                        value={userId}
                        onChange={(e) => setUserId(e.target.value)}
                        required
                    />
                </label>

                <label>
                    Fecha de compra (DD-MM-YYYY):
                    <input
                        type="text"
                        value={purchaseDate}
                        onChange={(e) => setPurchaseDate(e.target.value)}
                        placeholder="DD-MM-YYYY"
                        required
                    />
                </label>

                <h3>Items</h3>
                {items.map((item, i) => (
                    <div key={i} className="item-row">
                        <input
                            type="text"
                            placeholder="Descripción"
                            value={item.description}
                            onChange={(e) => handleItemChange(i, 'description', e.target.value)}
                            required
                        />
                        <input
                            type="number"
                            placeholder="Valor unitario"
                            min="0.01"
                            step="0.01"
                            value={item.unitValue}
                            onChange={(e) => handleItemChange(i, 'unitValue', e.target.value)}
                            required
                        />
                        <input
                            type="number"
                            placeholder="Cantidad"
                            min="1"
                            step="1"
                            value={item.quantity}
                            onChange={(e) => handleItemChange(i, 'quantity', e.target.value)}
                            required
                        />
                        {items.length > 1 && (
                            <button type="button" onClick={() => removeItem(i)} className="btn-remove">
                                X
                            </button>
                        )}
                    </div>
                ))}
                <button type="button" onClick={addItem} className="btn-add">
                    + Añadir Item
                </button>

                <label>
                    Valor total:
                    <input
                        type="number"
                        min="0.01"
                        step="0.01"
                        value={totalValue}
                        onChange={(e) => setTotalValue(e.target.value)}
                        required
                    />
                </label>

                <button type="submit" className="btn-submit">
                    Registrar Pago
                </button>
            </form>

            {paymentResponse && (
                <div className="payment-response">
                    <h2>Respuesta del Pago</h2>
                    <pre>{JSON.stringify(paymentResponse, null, 2)}</pre>
                </div>
            )}

            <hr />

            <h2>Consultar Pagos por Usuario</h2>
            <input
                type="text"
                placeholder="ID Usuario"
                value={consultUserId}
                onChange={(e) => setConsultUserId(e.target.value)}
            />
            <button onClick={consultPayments} className="btn-consult">
                Consultar
            </button>

            {consultedPayments.length > 0 && (
                <div className="consult-results">
                    <h3>Pagos Encontrados</h3>
                    <pre>{JSON.stringify(consultedPayments, null, 2)}</pre>
                </div>
            )}
        </div>
    );
}
```
